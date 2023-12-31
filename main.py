letter_to_number = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

number_to_letter = {
    1: 'a',
    2: 'b',
    3: 'c',
    4: 'd',
    5: 'e',
    6: 'f',
    7: 'g',
    8: 'h',
    9: 'i',
    10: 'j',
    11: 'k',
    12: 'l',
    13: 'm',
    14: 'n',
    15: 'o',
    16: 'p',
    17: 'q',
    18: 'r',
    19: 's',
    20: 't',
    21: 'u',
    22: 'v',
    23: 'w',
    24: 'x',
    25: 'y',
    26: 'z'
}


def encrypt():
    input_string = input('input string to encrypt\n').lower()
    encrypted = input_string[0]
    for idx, i in enumerate(input_string):
        if idx == 0:
            continue
        try:
            current = input_string[idx]
            previous_val = encrypted[idx - 1]
            summed = letter_to_number[current] + letter_to_number[previous_val]
            if summed > 26:
                summed -= 26
            encrypted += number_to_letter[summed]
        except KeyError:
            encrypted += i
    print(encrypted)


def decrypt():
    input_string = input('input string to decrypt\n').lower()
    input_string = input_string[::-1]
    decrypted = ''
    for idx, i in enumerate(input_string):
        if idx == len(input_string) - 1:
            break
        try:
            current = input_string[idx]
            next_val = input_string[idx + 1]
            subtracted = letter_to_number[current] - letter_to_number[next_val]
            if subtracted <= 0:
                subtracted += 26
            decrypted += number_to_letter[subtracted]
        except KeyError:
            decrypted += i
    decrypted += input_string[-1]
    decrypted = decrypted[::-1]
    print(decrypted)


encrypt()
decrypt()
