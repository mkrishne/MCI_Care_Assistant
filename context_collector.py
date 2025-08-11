import datetime
import os
import json
from PIL import Image
from openai import OpenAI
import base64

# Set up your OpenAI API key (make sure it is set in the environment or passed here directly)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Global variables
MEMORY_FILE = "memory_block.json"

CURRENT_LOCATION = "Room 202, elderly care center, West Lafayette"
IMAGE_PATH = "image_for_learning.png"  # Global image path

#CURRENT_LOCATION = "Northwestern Avenue, West Lafayette"
#IMAGE_PATH = "image_for_memory.jpg"  # Global image path

def load_memory():
    """Load memory block from a file"""
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def recognize_image():
    """Send image to GPT model for recognition and extract objects and persons"""
    # For the purpose of this example, we're using GPT image recognition.
    # Normally, you would use a specific model like GPT-4o Vision or an API for image recognition.
    
    # Assuming you're sending the image to OpenAI's image recognition model (hypothetical here)
    try:
        with open(IMAGE_PATH, "rb") as f:
            img_base64 = base64.b64encode(f.read()).decode("utf-8")
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "I have a camera on my body and this image shows everything I am currently seeing. Please describe what I am currently seeing"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{img_base64}"
                            }
                        }
                    ]
                }
            ]
        )
        # Get textual response, assuming the model can describe the image
        image_description = response.choices[0].message.content
        
        # Now return image description
        return image_description
        
    except Exception as e:
        print("Error with image recognition:", e)
        return [], []

def context_collector(brain_state):
    """Collect context based on brain state"""
    where = CURRENT_LOCATION
    when = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    who_what = recognize_image()  # Now dynamically recognizing objects and persons
    
    # Step 2: Handle memory state
    if brain_state == "memory":
        memory_block = load_memory()

    # Return all necessary context
    return where, when, who_what, memory_block if brain_state == "memory" else None