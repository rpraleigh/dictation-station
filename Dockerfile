# Use Python 3.10
FROM python:3.10-slim

# Install system dependencies (ffmpeg is required for Whisper)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /app

# Copy files
COPY requirements.txt .
COPY app.py .

# Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Streamlit runs on
EXPOSE 8501

# Run the app
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]