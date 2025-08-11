import datetime
import os
from openai import OpenAI
from state_dispatcher import state_dispatcher
from context_collector import context_collector
from prompt_generator import prompt_generator
from update_memory import update_memory

# Load API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

brain_state = state_dispatcher()
where, when, who_what, memory_block = context_collector(brain_state)

system_prompt = prompt_generator(where, when, who_what, memory_block)

# Output the generated prompt
print(system_prompt)

# 3. Initialize chat history with system message only
chat_history = [{"role": "system", "content": system_prompt}]

# 4. Assistant starts the conversation
response = client.chat.completions.create(
    model="gpt-4o",
    messages=chat_history
)
assistant_reply = response.choices[0].message.content
print("Assistant:", assistant_reply)

# Add assistant's first message to chat history
chat_history.append({"role": "assistant", "content": assistant_reply})

# 5. Start conversation loop

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "stop"]:
        print("Exiting the chat.")
        break

    # Add user's message to chat history
    chat_history.append({"role": "user", "content": user_input})

    # Get next assistant reply
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=chat_history
    )
    assistant_reply = response.choices[0].message.content
    print("Assistant:", assistant_reply)

    # Add assistant's reply to chat history
    chat_history.append({"role": "assistant", "content": assistant_reply})

update_memory(where, when, chat_history)
