"""Personal Keyboard Main Script File."""

import json
from pathlib import Path

import keyboard

def watch():
    """Main function that registers all of the keyboard shortcuts from the user."""
    pk_dir = Path(__file__).parent
    for config_file in pk_dir.glob('*.json'):
        snippet_dict = json.loads(config_file.read_text())
        snippets = snippet_dict.get('snippets', [])
        for abbreviation, completion in snippets:
            print(f'Registering: {abbreviation}: {completion}')
            keyboard.add_abbreviation(abbreviation, completion)

    print('\n')
    keyboard.wait()
