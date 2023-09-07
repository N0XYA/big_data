morze =  {'a': '.-', 'b': '-…', 'c': '-.-.', 'd': '-..',
 'e': '.', 'f': '..-.', 'g': '--.', 'h': '….',
 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
 'q': '--.-', 'r': '.-.', 's': '…', 't': '-',
 'u': '..-', 'v': '…-', 'w': '.--', 'x': '-..-',
 'y': '-.--', 'z': '--..'}


def find_morze(morze):
    print("Please input text: ")
    text = input()
    text = text.lower()
    morze_text = ""
    for letter in text:
        if letter != " ":
            morze_text += morze[letter.lower()]
        else:
            morze_text += '\n'
    print(morze_text)
    return


def main():
    find_morze(morze)
    return 0


if __name__ == "__main__":
    main()