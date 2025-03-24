"""
Replit entry point for N8N Voice Interface
"""
import os
import sys

# Change the current directory to the project directory
project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "n8n-voice-interface-v1")
os.chdir(project_dir)
print(f"Changed working directory to: {project_dir}")

# Add the project directory to Python path
sys.path.append(project_dir)
print(f"Added {project_dir} to Python path")

# Set default STT model if not already set
if "STT_MODEL" not in os.environ:
    os.environ["STT_MODEL"] = "whisper-1"

# Import the app
try:
    print(f"Current working directory: {os.getcwd()}")
    print(f"Files in current directory: {os.listdir('.')}")
    
    # Add backend directory to path
    sys.path.append(os.path.join(project_dir, "backend"))
    
    # Try to import the app
    from backend.app import app
    print("Successfully imported app module!")
except Exception as e:
    print(f"Error during import: {e}")
    print(f"Current Python path: {sys.path}")
    print("Trying alternative import method...")
    
    # Alternative import approach - import from full path
    sys.path.insert(0, os.path.join(project_dir, "backend"))
    from app import app

import uvicorn

if __name__ == "__main__":
    # Get port from environment (Replit sets this)
    port = int(os.environ.get("PORT", 8080))
    
    print("Starting N8N Voice Interface...")
    print(f"Using STT model: {os.environ.get('STT_MODEL')}")
    print(f"Port: {port}")
    
    # Install required dependencies if not already installed
    os.system("pip install -r backend/requirements.txt")
    
    # Run the application
    uvicorn.run(
        "backend.app:app", 
        host="0.0.0.0", 
        port=port,
        reload=False
    )
