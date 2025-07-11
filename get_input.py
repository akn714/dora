from prompt_toolkit import prompt

def get_input(start_str):
    return prompt(start_str, multiline=True)