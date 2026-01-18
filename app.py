import streamlit as st
import os
from streamlit_mic_recorder import mic_recorder
from faster_whisper import WhisperModel
from openai import OpenAI
import tempfile

st.set_page_config(page_title="Dictation Station", page_icon="🎙️")
st.title("🎙️ Docker Dictation Station")

# 1. SETUP CLIENTS
# Connect to LM Studio on the Mac host
client = OpenAI(base_url="http://host.docker.internal:1234/v1", api_key="lm-studio")

# Load Whisper
@st.cache_resource
def load_whisper():
    return WhisperModel("small", device="cpu", compute_type="int8")

whisper = load_whisper()

# --- NEW SECTION: DYNAMIC PROMPT ---
# We use an expander so it doesn't clutter the screen if you don't need it.
with st.expander("⚙️ AI Instructions (System Prompt)", expanded=True):
    system_prompt = st.text_area(
        "Tell the AI how to process your text:",
        value="You are an expert editor. Fix grammar, remove filler words (ums, ahs), and improve the flow. Maintain the original tone. Do not summarize.",
        height=100
    )
# -----------------------------------

c1, c2 = st.columns([1, 4])
with c1:
    st.write("Record:")
    audio = mic_recorder(
        start_prompt="⏺️ Record",
        stop_prompt="⏹️ Stop",
        key='recorder'
    )

if audio:
    st.divider()
    
    # Save audio for Whisper
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_file:
        tmp_file.write(audio['bytes'])
        tmp_path = tmp_file.name

    # Transcribe
    with st.spinner("📝 Transcribing audio..."):
        segments, _ = whisper.transcribe(tmp_path)
        raw_text = " ".join([segment.text for segment in segments])
    
    st.subheader("Raw Transcript")
    st.info(raw_text)

    # Clean up (Using the Dynamic Prompt)
    with st.spinner("✨ Processing with LM Studio..."):
        try:
            response = client.chat.completions.create(
                model="local-model",
                messages=[
                    # HERE IS THE CHANGE: We use the variable 'system_prompt'
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": raw_text}
                ],
                temperature=0.7
            )
            clean_text = response.choices[0].message.content
            
            st.subheader("Result")
            st.success(clean_text)
            
            # Helper to copy text easily
            st.text_area("Copyable Output", value=clean_text, height=200)
            
        except Exception as e:
            st.error(f"Could not connect to LM Studio. Is the server running? Error: {e}")

    # Cleanup file
    os.remove(tmp_path)