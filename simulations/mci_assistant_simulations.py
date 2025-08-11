import datetime
import os
import re
from openai import OpenAI
from state_dispatcher_simulations import state_dispatcher
from context_collector_simulations import context_collector
from prompt_generator_for_assistant_in_simulations import prompt_generator

def log_conversation_to_file(chat_history, filename_index): 
    """Log the entire conversation to a file"""
    filename = f"conversation_samples/mci_conversation_{filename_index}.txt" 
    
    # Ensure the directory exists before writing the file
    os.makedirs("conversation_samples", exist_ok=True)

    with open(filename, "w", encoding="utf-8") as file:
        file.write("Conversation between MCI Assistant and Elderly Person with MCI:\n\n")
        
        # Write the conversation history from both roles
        for message in chat_history:
            role = message["role"]
            content = message["content"]

            # Check the role and format accordingly
            if role == "assistant":
                file.write(f"MCI Assistant: {content}\n")
            elif role == "user":
                file.write(f"Elderly Person with MCI: {content}\n\n")
    
    print(f"Conversation logged in {filename}")

# Load API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

brain_state = state_dispatcher()
for filename in os.listdir("image_learning_results"):
    if filename.endswith(".txt"):  # Check for text files
        # Construct the full file path
        file_path = os.path.join("image_learning_results", filename)
    where, when, who_what, memory_block = context_collector(brain_state,file_path)

    system_prompt_assistant  = prompt_generator(where, when, who_what, memory_block)

    # Output the generated prompt
    print(system_prompt_assistant )

    # 3. Initialize chat history with system message only
    chat_history_assistant  = [{"role": "system", "content": system_prompt_assistant}]

    # 4. Assistant starts the conversation
    response_assistant = client.chat.completions.create(
        model="gpt-4o",  # or use the relevant model
        messages=chat_history_assistant
    )
    assistant_reply = response_assistant.choices[0].message.content
    print("MCI Assistant:", assistant_reply)

    # Add assistant's first message to chat history
    chat_history_assistant.append({"role": "assistant", "content": assistant_reply})

    system_prompt_mci = "Behave like an elderly person with Mild Cognitive Impairment (MCI) having a conversation with a family member. Try to choose one of the drinks placed in front of you using family member's help. Keep each response very simple, concise and straightforward."
    chat_history_mci = [{"role": "system", "content": system_prompt_mci}]  # MCI system message
    chat_history_mci.append({"role": "user", "content": assistant_reply})
    response_mci = client.chat.completions.create(
        model="gpt-4",  # or use the relevant model
        messages=chat_history_mci
    )
    mci_reply = response_mci.choices[0].message.content
    print("Elderly Person with MCI:", mci_reply)

    chat_history_mci.append({"role": "assistant", "content": mci_reply})
    chat_history_assistant.append({"role": "user", "content": mci_reply})

    # 3. Start conversation loop between the assistant and the elderly person (MCI)
    for i in range(5):  # Limit the conversation to 5 exchanges for now
        # Assistant responds to MCI's message
        response_assistant = client.chat.completions.create(
            model="gpt-4o",  # or use the relevant model
            messages=chat_history_assistant
        )
        assistant_reply = response_assistant.choices[0].message.content
        print("MCI Assistant:", assistant_reply)

        # Add assistant's reply to the chat history
        chat_history_assistant.append({"role": "assistant", "content": assistant_reply})
        chat_history_mci.append({"role": "user", "content": assistant_reply})

        # Elderly person (MCI) responds to the assistant
        response_mci = client.chat.completions.create(
            model="gpt-4",  # or use the relevant model
            messages=chat_history_mci
        )
        mci_reply = response_mci.choices[0].message.content
        print("Elderly Person with MCI:", mci_reply)

        # Add MCI's reply to the chat history
        chat_history_mci.append({"role": "assistant", "content": mci_reply})
        chat_history_assistant.append({"role": "user", "content": mci_reply})

    match = re.match(r"recognition_result_(\d+)", filename)
    if match:
        # Extract the index (the number after 'recognition_result_')
        index = match.group(1)
    log_conversation_to_file(chat_history_assistant, index)