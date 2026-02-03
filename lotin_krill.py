data_alphabet = {
    "a": "а",
    "b": "б",
    "d": "д",
    "e": "е",
    "f": "ф",
    "g": "г",
    "h": "ҳ",
    "i": "и",
    "j": "ж",
    "k": "к",
    "l": "л",
    "m": "м",
    "n": "н",
    "o": "о",
    "p": "п",
    "q": "қ",
    "r": "р",
    "s": "с",
    "t": "т",
    "u": "у",
    "v": "в",
    "x": "х",
    "y": "й",
    "z": "з",
    "o'": "ў",
    "g'": "ғ",
    "sh": "ш",
    "ch": "ч",
    "ng": "нг",
    "’": "ъ"
}



def lotin_to_krill(text):
    new_text = ''
    i = 0

    while i < len(text):
        # 2 harfli kombinatsiya
        if i + 1 < len(text) and text[i:i+2].casefold() in data_alphabet:
            juft_harf = data_alphabet[text[i:i+2].casefold()]

            if text[i:i+2].isupper():
                new_text += juft_harf.upper()
            elif text[i].isupper():
                new_text += juft_harf.capitalize()
            else:
                new_text += juft_harf

            i += 2
        else:
            # 1 harfli
            harf = text[i]
            letter = data_alphabet.get(harf.casefold(), harf)

            if harf.isupper():
                new_text += letter.upper()
            else:
                new_text += letter

            i += 1

    return new_text

def receive_data():
    while True:
        ask=input("Matnni kiriting(chiqish-'exit'):")
        if ask.casefold() == 'exit':
            break
        print(lotin_to_krill(ask))


receive_data()




