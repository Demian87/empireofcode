def morse_time(time_string):
    numerals = [(n[:1], n[1:]) for n in time_string.split(":")]
    binary = []
    for i, (a, b) in enumerate(numerals):
        if not b:
            a, b = '0', a
        if i == 0:
            a_bin = format(int(a), '02b')
        else:
            a_bin = format(int(a), '03b')
        b_bin = format(int(b), '04b')
        binary.append(' '.join((a_bin, b_bin)))
    return ' : '.join(binary).replace('0', '.').replace('1', '-')



if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert morse_time("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert morse_time("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert morse_time("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert morse_time("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
