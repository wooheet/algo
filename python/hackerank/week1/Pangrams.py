def pangrams(s):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    s = sorted(set(s.replace(" ", "").upper()))

    if len(s) == len(alphabet):
        return "pangram"
    else:
        return "not pangram"


s = 'We promptly judged antique ivory buckles for the next prize'
# s = 'We promptly judged antique ivory buckles for the prize'
pangrams(s)
