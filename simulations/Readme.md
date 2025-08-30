# MCI Assistant Chat Simulations

This module runs **simulation tests** to observe how different instances of the **MCI Assistant Chatbot** respond to the same scenario.  
The aim is to check the **consistency** of responses when the chatbot behaves as both:

1. **MCI Assistant** – supporting the elderly person as before.  
2. **Elderly person with MCI in the learning state** – in this simulation, the elderly person chooses a drink in front of them.

---

## 🧪 Simulation Overview

A total of **100 simulations** are run:

1. **Image Description Phase** – The system repeatedly analyzes the same image (`image_for_learning_for_simulations.jpeg`) to get descriptions.
2. **Chat Simulation Phase** – For each description, a simulated conversation is run where:
   - The assistant plays its usual role.
   - The elderly person is in **learning** mode and picks a drink.
3. **Logging Results** – Each simulation’s conversation is stored for further analysis.

---

## 📂 System Components

### 1. `image_learning_for_simulations.py`
- Reads the image `image_for_learning_for_simulations.jpeg`.
- Uses GPT-based vision capabilities to **describe the image**.
- This process is repeated **100 separate times** to generate descriptions for each simulation run.

**Output:**  
Generates 100 image descriptions (one per run) in the folder `image_learning_results/` for use in the chat simulation phase.


### 2. `mci_assistant_simulations.py`
- Runs the **conversation simulation** for each image description.
- Roles in each simulation:
  - **MCI Assistant**: Guides the conversation.
  - **Elderly Person (Learning State)**: Chooses a drink from the scene.
- Conversations are stored in the `conversation_samples/` folder.

### 3. `mci_assistant_simulations_no_resp_prompting.py`
- Runs the **conversation simulation** for each image description.
- Roles in each simulation:
  - **MCI Assistant**: When the MCI assistant does not receive any initial response from the patient, it continues prompting in a friendly manner to encourage a reply. 
  - **Elderly Person (Learning State)**: Chooses a drink from the scene.
- Conversations are stored in the `conversation_samples_no_resp_prompting/` folder.

## 🚀 Running the Simulations

### 1. Prepare the Environment
Make sure dependencies are installe and api key set as for chat-bot

### 2. Run the Image Description Phase
```
python image_learning_for_simulations.py
```

### 3. Run the Chat Simulation Phase
```
python mci_assistant_simulations.py
```

### 4. Run the Chat Simulation Phase with possible no initial response from the elderly
```
python mci_assistant_simulations_no_resp_prompting.py
```

## 📁 Directory Structure
```
├── image_learning_for_simulations.py       		 # Generates image descriptions
├── image_for_learning_for_simulations.jpeg 		 # Input image
├── image_learning_results/							 # Stores image description results
├── mci_assistant_simulations.py           			 # Runs chat simulations
├── mci_assistant_simulations_no_resp_prompting.py   # Runs chat simulations with possibly no initial response from the elderly
├── prompt_generator_for_assistant_in_simulations/   # generates the prompts for mci_assistant
├── context_collector_simulations.py				 # generates 4W prompts
├── conversation_samples/                   		 # Stores conversation logs
├── conversation_samples_no_resp_prompting/    		 # Stores conversation logs for no response simulations
```





