import re


def string_to_morse(str_text):
    morse_dict = {
                'a': '▄▄▄ ▄   ',
                'b': '▄▄▄ ▄ ▄ ▄   ',
                'c': '▄▄▄ ▄ ▄▄▄   ',
                'd': '▄▄▄ ▄ ▄   ',
                'e': '▄   ',
                'f': '▄ ▄ ▄▄▄ ▄   ',
                'g': '▄▄▄ ▄▄▄ ▄   ',
                'h': '▄ ▄ ▄ ▄   ',
                'i': '▄ ▄   ',
                'j': '▄ ▄▄▄ ▄▄▄ ▄▄▄   ',
                'k': '▄▄▄ ▄ ▄▄▄   ',
                'l': '▄ ▄▄▄ ▄ ▄   ',
                'm': '▄▄▄ ▄▄▄   ',
                'n': '▄▄▄ ▄   ',
                'o': '▄▄▄ ▄▄▄ ▄▄▄   ',
                'p': '▄ ▄▄▄ ▄▄▄ ▄   ',
                'q': '▄▄▄ ▄▄▄ ▄ ▄▄▄   ',
                'r': '▄ ▄▄▄ ▄   ',
                's': '▄ ▄ ▄   ',
                't': '▄▄▄   ',
                'u': '▄ ▄ ▄▄▄   ',
                'v': '▄ ▄ ▄ ▄▄▄   ',
                'w': '▄ ▄▄▄ ▄▄▄   ',
                'x': '▄▄▄ ▄ ▄ ▄▄▄   ',
                'y': '▄▄▄ ▄ ▄▄▄ ▄▄▄   ',
                'z': '▄▄▄ ▄▄▄ ▄ ▄   ',
                '1': '▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄   ',
                '2': '▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄   ',
                '3': '▄ ▄ ▄ ▄▄▄ ▄▄▄   ',
                '4': '▄ ▄ ▄ ▄ ▄▄▄   ',
                '5': '▄ ▄ ▄ ▄ ▄   ',
                '6': '▄▄▄ ▄ ▄ ▄ ▄   ',
                '7': '▄▄▄ ▄▄▄ ▄ ▄ ▄   ',
                '8': '▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄   ',
                '9': '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄   ',
                '0': '▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄   ',
                ' ': '    ',
                '.': '    ',
                '?': '    ',
                '!': '    '
                }

    morse_text = ''
    for c in str_text:
        morse_text += morse_dict.get(c, '')

    return morse_text


def main():
    str_text = input("\n🔤 Enter a word to convert to morse: \n").lower()
    morse_text = string_to_morse(str_text)
    if re.match(r'^[a-zA-Z0-9\s.?!]*$', str_text):
        print("\n✅ Your text in morse is: \n", morse_text, "\n")
    else:
        print("\n❌ Your text is invalid! \n Use letters, numbers, spaces or .?! punctuation.\n")


if __name__ == '__main__':
    main()
