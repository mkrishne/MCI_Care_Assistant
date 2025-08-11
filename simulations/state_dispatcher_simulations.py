# state_dispatcher.py

brain_state = "learning"
def state_dispatcher():
    if brain_state == "rest":
        return

    elif brain_state == "learning":
        return "learning"

    elif brain_state == "memory":
        return "memory"

    else:
        raise ValueError(f"Unknown brain_state: {brain_state}")
