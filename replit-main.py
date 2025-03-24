"""
Replit entry point for N8N Voice Interface
"""
import os
import sys

# Add the current directory to the path so we can import modules
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Set default STT model if not already set
if "STT_MODEL" not in os.environ:
    os.environ["STT_MODEL"] = "whisper-1"

# Import FastAPI app
try:
    # Try importing directly (if backend is in the current directory)
    from backend.app import app
    print("Successfully imported app module from backend directory")
except ModuleNotFoundError:
    # If that fails, try with n8n-voice-interface-v1 path
    try:
        sys.path.append(os.path.join(current_dir, "n8n-voice-interface-v1"))
        from n8n_voice_interface_v1.backend.app import app
        print("Successfully imported app module from n8n-voice-interface-v1/backend directory")
    except ModuleNotFoundError:
        # Print all directories in the current path to help debug
        print("Current directory:", current_dir)
        print("Files in current directory:", os.listdir(current_dir))
        print("Python path:", sys.path)
        raise Exception("Could not import the app module. Please check your directory structure.")

import uvicorn

if __name__ == "__main__":
    # Get port from environment (Replit sets this)
    port = int(os.environ.get("PORT", 8080))
    
    print("Starting N8N Voice Interface...")
    print(f"Using STT model: {os.environ.get('STT_MODEL')}")
    print(f"Port: {port}")
    
    # Run the application
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=port,
        reload=False
    )
