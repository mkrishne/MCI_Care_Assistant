# MCI Assistant Chatbot

MCI Assistant Chatbot is designed to simulate a conversation between an **elderly person with Mild Cognitive Impairment (MCI)** and an **assistant** using OpenAI's **GPT-4** model. The assistant provides conversational support based on the brain state of the elderly person, which can be in one of three states:

- **Rest**: No interaction.
- **Learning**: Helping the elderly person recognize or learn objects or surroundings.
- **Memory**: Helping recall memories.

The chatbot also includes the ability to collect contextual information such as the **environment** (e.g., room name, objects in the room) and the elderly person's **current cognitive state**.

---

## System Components

### 1. `state_dispatcher.py`

This module determines the **brain state** of the elderly person. The brain state can be one of the following:

- **"learning"**: The elderly person needs help learning or recognizing something.
- **"memory"**: The elderly person needs help recalling something from memory.
- **"rest"**: The elderly person is resting and does not require assistance.

The `state_dispatcher()` function checks the current brain state and returns the corresponding state.

#### Usage:
- You can manually set the `brain_state` variable to one of these values in `state_dispatcher.py`.

### 2. `context_collector.py`

This module gathers the necessary **context** for the assistant to interact with the elderly person. It takes inputs such as:

- **Current Location**: The room or environment where the elderly person is located.
- **Image of Surroundings**: A visual input (e.g., from a camera or image file) that helps the assistant identify objects and people in the environment.

The `context_collector(brain_state)` function returns:

- **where**: The current location.
- **when**: The current time.
- **who_what**: Information about people and objects in the surroundings.
- **memory_block**: Relevant memory data that can help assist the elderly person in **"memory"** state.

### 3. `prompt_generator.py`

This module generates the **system prompt** for the assistant. It constructs the prompt based on the context provided (e.g., location, objects in the surroundings, and brain state) to guide the assistant in generating appropriate responses.

### 4. `update_memory.py`

This module **updates the memory block** with the **chat summary** after each conversation. The memory block helps the assistant remember important details about the user and use them in future interactions to assist the elderly person.

### 5. **Main Script - `mci_assistant.py`** (Simulation)

The main script runs the **conversation simulation** between the assistant and the elderly person, interacting with the OpenAI API. It incorporates the different modules and manages the back-and-forth conversation.

---

## Installation & Setup

### 1. Install Dependencies:

Make sure you have **Python** installed and then install the required packages using `pip`:

```bash
pip install openai

### 2. Set Up API Key:
Ensure that you have a valid OpenAI API key. Set the environment variable OPENAI_API_KEY to your API key or add it directly in the code.
```bash
export OPENAI_API_KEY="your_api_key_here"

### 3. Directory Structure:
Ensure the following directory structure is in place:
├── mci_assistant.py                # Main simulation script
├── state_dispatcher.py             # Brain state handling
├── context_collector.py            # Collecting contextual information
├── prompt_generator.py             # Generating system prompts
├── update_memory.py                # Updating memory
├── conversation_samples/           # Folder for logged conversations
└── image_recognition_results/      # Folder for image recognition results

### 4. Image Input:
- Place the image file (e.g., "image_for_recognition.png") in the same directory or specify the correct path in context_collector.py.
- Ensure the image contains objects or people that the assistant can recognize.

## Running the Simulation
### 1. Configure the Brain State:
In the state_dispatcher.py file, set the brain_state variable to one of the following:
- **rest**
- **learning**
- **memory**

### 2. Run the Script:
To start the conversation simulation, run the following command in your terminal:
```bash
python mci_assistant.py

### 3. Interacting with the Simulation:
- The assistant will prompt you with a conversation.
- Type your input in the terminal. You can ask questions or provide responses, and the assistant will reply based on the context.
- To end the simulation, type exit, quit, or stop.

## License
This project is licensed under the MIT License - see the LICENSE file for details.



