# 01234567 89abcdef ghijklmn opqrstuv wxyzABCD EFGHIJKL MNOPQRST UVWXYZ<>
def in_hex(val):
    if val <= 9:
        return str(val)
    elif val == 10:
        return 'a'
    elif val == 11:
        return 'b'
    elif val == 12:
        return 'c'
    elif val == 13:
        return 'd'
    elif val == 14:
        return 'e'
    elif val == 15:
        return 'f'
def in_b64(val):
    if val <= 9:
        return str(val)
    elif val == 10:
        return 'a'
    elif val == 11:
        return 'b'
    elif val == 12:
        return 'c'
    elif val == 13:
        return 'd'
    elif val == 14:
        return 'e'
    elif val == 15:
        return 'f'
    elif val == 16:
        return 'g'
    elif val == 17:
        return 'h'
    elif val == 18:
        return 'i'
    elif val == 19:
        return 'j'
    elif val == 20:
        return 'k'
    elif val == 21:
        return 'l'
    elif val == 22:
        return 'm'
    elif val == 23:
        return 'n'
    elif val == 24:
        return 'o'
    elif val == 25:
        return 'p'
    elif val == 26:
        return 'q'
    elif val == 27:
        return 'r'
    elif val == 28:
        return 's'
    elif val == 29:
        return 't'
    elif val == 30:
        return 'u'
    elif val == 31:
        return 'v'
    elif val == 32:
        return 'w'
    elif val == 33:
        return 'x'
    elif val == 34:
        return 'y'
    elif val == 35:
        return 'z'
    elif val == 36:
        return 'A'
    elif val == 37:
        return 'B'
    elif val == 38:
        return 'C'
    elif val == 39:
        return 'D'
    elif val == 40:
        return 'E'
    elif val == 41:
        return 'F'
    elif val == 42:
        return 'G'
    elif val == 43:
        return 'H'
    elif val == 44:
        return 'I'
    elif val == 45:
        return 'J'
    elif val == 46:
        return 'K'
    elif val == 47:
        return 'L'
    elif val == 48:
        return 'M'
    elif val == 49:
        return 'N'
    elif val == 50:
        return 'O'
    elif val == 51:
        return 'P'
    elif val == 52:
        return 'Q'
    elif val == 53:
        return 'R'
    elif val == 54:
        return 'S'
    elif val == 55:
        return 'T'
    elif val == 56:
        return 'U'
    elif val == 57:
        return 'V'
    elif val == 58:
        return 'W'
    elif val == 59:
        return 'X'
    elif val == 60:
        return 'Y'
    elif val == 61:
        return 'Z'
    elif val == 62:
        return '<'
    elif val == 63:
        return '>'
def int2hex(val):
    string = ''
    places = []
    while val >= 1:
        leftover = val - (val // 16 * 16)
        val //= 16
        string = in_hex(leftover) + string
    return string
def int2b64(val):
    string = ''
    places = []
    while val >= 1:
        leftover = val - (val // 64 * 64)
        val //= 64
        string = in_b64(leftover) + string
    return string