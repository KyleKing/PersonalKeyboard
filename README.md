# PersonalKeyboard

Personal keyboard configuration for both Mac and Windows. Written in Python

## Status

Currently there are a couple of issues:

- Doesn't recognize the keyboard abbreviation @@ because it doesn't pick up the Shift key: https://github.com/boppreh/keyboard/issues/230#issuecomment-457241316
- `keyboard.add-abbreviation` isn't working at all on Mac
- Need to figure out a way to launch with sudo automatically from Mac, which is not ideal
- If I want to use @clipboard/@cursor like Dash snippets, i would need to have some sort of UI for editing before pasting

For now this project is shelved, but I plan to look into alternative options for syncing keyboard shortcuts between Mac and Windows
