# Dictation Station 🎙️

A privacy-focused web app that records your voice, transcribes it locally using **Faster-Whisper**, and cleans up the text using your local LLM (via **LM Studio**).

## Prerequisites
1. **Docker Desktop** installed and running.
2. **[LM Studio](https://lmstudio.ai/)**:
   * **Download a Model:** Click the Search icon (🔍), type a model name (like `Llama 3`), and download one (e.g., `Meta-Llama-3-8B-Instruct`).
   * **Start Server:** Go to the **Local Server** tab (<->) and start the server on Port `1234`.
   * **Load Model:** Select your downloaded model from the top dropdown menu to load it into memory.

---

## Installation & Setup

### 🪟 Windows (PowerShell)
1. **Install Git:**
   Open PowerShell and run:
   ```powershell
   winget install --id Git.Git -e --source winget
   ```
   *(Close and reopen PowerShell after this step).*

2. **Download:**
   Navigate to where you want the project (e.g., Documents) and clone it:
   ```powershell
   cd Documents
   git clone https://github.com/rpraleigh/dictation-station.git
   cd dictation-station
   ```

3. **Run:**
   ```powershell
   docker compose up --build
   ```

### 🍎 Mac (Terminal)
1. **Install Git:**
   Open Terminal and check if Git is installed:
   ```bash
   git --version
   ```
   *(If missing, macOS will prompt you to install it).*

2. **Download:**
   Navigate to your projects folder and clone:
   ```bash
   cd Documents
   git clone https://github.com/rpraleigh/dictation-station.git
   cd dictation-station
   ```

3. **Run:**
   ```bash
   docker compose up --build
   ```

### 🐧 Linux (Ubuntu/Debian)
1. **Install Tools:**
   ```bash
   sudo apt-get update && sudo apt-get install -y docker.io docker-compose-v2 git
   sudo service docker start
   ```

2. **Download:**
   ```bash
   cd Documents
   git clone https://github.com/rpraleigh/dictation-station.git
   cd dictation-station
   ```

3. **Run:**
   ```bash
   sudo docker compose up --build
   ```

---

## Usage
1. Open your browser to **[http://localhost:8501](http://localhost:8501)**.
2. (Optional) Edit the **AI Instructions** in the text box to change how the text is cleaned (e.g., "Make this a bulleted list").
3. Click **Record**.
4. Speak, then click **Stop**.
5. The app will transcribe your audio and send the text to LM Studio for cleanup.
