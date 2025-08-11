def prompt_generator(where, when, who_what, memory_block):
    """Generate a prompt based on the given context and memory."""
    
    if memory_block is None:
        # Generate a prompt when there is no memory block (recognition mode)
        system_prompt = f"""
            I am in {where}. The current time is {when}.
            {who_what}.  
            Please behave like a helpful family member who gently initiates a conversation with me based on this context. Keep the conversation short, with about 4 to 5 messages exchanged.
            """
    else:
        # Generate a prompt when there is a memory block (memory mode)
        system_prompt = f"""
            I am in {where}. The current time is {when}.
            {who_what}.  
            Please behave like a helpful family member who gently initiates a conversation with me and help me recall something because I am currently confused based on what I am seeing. 
            Use my previous information if needed: {memory_block}
            """
    
    return system_prompt
