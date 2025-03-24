"""
Replit entry point for N8N Voice Interface
"""
import os
import sys
import subprocess

# Change the current directory to the project directory
project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "n8n-voice-interface-v1")
os.chdir(project_dir)
print(f"Changed working directory to: {project_dir}")

# First, install the required dependencies
print("Installing required dependencies...")
requirements_path = os.path.join(project_dir, "backend", "requirements.txt")

if os.path.exists(requirements_path):
    # Install dependencies using pip
    print(f"Installing dependencies from {requirements_path}")
    result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", requirements_path])
    
    if result.returncode != 0:
        print("Failed to install dependencies! Trying to continue anyway...")
    else:
        print("Dependencies installed successfully!")
else:
    print(f"Requirements file not found at {requirements_path}")
    print("Attempting to install key dependencies directly...")
    subprocess.run([sys.executable, "-m", "pip", "install", "fastapi", "uvicorn", "python-multipart", 
                   "aiohttp", "requests", "python-dotenv", "pydantic"])

# Add the project directory to Python path
sys.path.append(project_dir)
sys.path.append(os.path.join(project_dir, "backend"))

# Set default models if not already set
if "STT_MODEL" not in os.environ:
    os.environ["STT_MODEL"] = "gpt-4o-transcribe"

if "TTS_MODEL" not in os.environ:
    os.environ["TTS_MODEL"] = "gpt-4o-mini-tts"

# Create tmp directory for audio files if it doesn't exist
tmp_audio_dir = os.path.join(tempfile.gettempdir(), "audio_files")
os.makedirs(tmp_audio_dir, exist_ok=True)
print(f"Created audio files directory at: {tmp_audio_dir}")

# Show diagnostics about the environment
print("\n--- Environment Diagnostics ---")
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")
print(f"Contents of backend directory: {os.listdir('backend')}")
print("-------------------------------\n")

# Run the application
print("Starting N8N Voice Interface...")
print(f"Using STT model: {os.environ.get('STT_MODEL')}")
print(f"Using TTS model: {os.environ.get('TTS_MODEL')}")
port = int(os.environ.get("PORT", 8080))
print(f"Port: {port}")

# Run uvicorn directly using subprocess to avoid import issues
print("Launching uvicorn server...")
cmd = [
    sys.executable, "-m", "uvicorn",
    "backend.app:app",
    "--host", "0.0.0.0",
    "--port", str(port)
]
print(f"Running command: {' '.join(cmd)}")
subprocess.run(cmd)
