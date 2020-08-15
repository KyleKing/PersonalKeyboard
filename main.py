"""Call with `poetry run python main.py."""

from personal_keyboard import pk

if __name__ == '__main__':
    # Launch the watcher for keyboard events
    pk.watch()
