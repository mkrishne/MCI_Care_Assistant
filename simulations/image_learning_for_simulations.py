import os
import base64
from openai import OpenAI

# Initialize client
IMAGE_PATH = "image_for_learning_for_simulations.jpeg"
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)  # Use the key in your OpenAI client

# Create the directory if it doesn't exist
output_directory = "image_learning_results"
os.makedirs(output_directory, exist_ok=True)

# Read and encode the image to base64
with open(IMAGE_PATH, "rb") as f:
    img_base64 = base64.b64encode(f.read()).decode("utf-8")

# Loop 50 times to make 101 API requests
for i in range(1, 111):
    # Create the request
    response = client.chat.completions.create(
        model="gpt-4o",  # Ensure you use the correct model name
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Use the image and please describe what I am currently seeing in front of me"},
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

    # Extract the content from the response
    content = response.choices[0].message.content

    # Print the content to the console
    print(f"Try {i}: {content}")

    # Log the content into a file with dynamic filename in the designated directory
    log_filename = os.path.join(output_directory, f"recognition_result_{i}.txt")
    with open(log_filename, "w") as file:
        file.write(f"Result {i}:\n")
        file.write(content)
        file.write("\n\n")

    print(f"Logged Result {i} content to {log_filename}")
    break
