import keyboard

print('1')
keyboard.press_and_release('shift+s, space')

print('2')
keyboard.write('The quick brown fox jumps over the lazy dog.')

print('3')
keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

print('Press PAGE UP then PAGE DOWN to type "foobar".')
keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

print('Blocks until you press esc.')
keyboard.wait('esc')

print('Record events until "esc is pressed.')
recorded = keyboard.record(until='esc')
print('Then replay back at three times the speed.')
keyboard.play(recorded, speed_factor=3)

print('Type @@ then press space to replace with abbreviation')
# for thing, other in json.loads("user_snippets.json")
keyboard.add_abbreviation('@@', 'my.long.email@example.com')

print('Block forever, like `while True`.')
keyboard.wait()
