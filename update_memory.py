# update_memory.py
import json
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MEMORY_FILE = "memory_block.json"

def generate_conversation_summary(chat_history):
    """Generate a summary of the conversation using GPT-4."""
    conversation_text = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in chat_history])
    
    summary_prompt = f"""
    Please provide a concise 1-2 sentence summary of the following conversation:
    {conversation_text}
    """
    
    response = client.chat.completions.create(
        model="gpt-4",  # Or gpt-3.5-turbo based on your choice
        messages=[{"role": "system", "content": summary_prompt}]
    )

    summary = response.choices[0].message.content.strip()
    return summary

def update_memory(where, when, chat_history):
    """Update memory with a summary of the conversation."""
    # Load the current memory from the file
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            memory_block = json.load(f)
    else:
        memory_block = []
        
    conversation_summary = generate_conversation_summary(chat_history)
    # Create a memory entry with the summary
    memory_entry = {
        "location": where,
        "time": when,
        "info": conversation_summary
    }
    print(memory_entry)
    # Add the new entry to the memory block
    memory_block.append(memory_entry)

    # Save the updated memory block to the file
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory_block, f, indent=2)
