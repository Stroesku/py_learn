def code(text, key=1):
    ans = ' '
    for letter in text:
        if letter != ' ':
            ans += " ".join(chr(ord(letter) + key))
        else:
            if (key == 3):
                ans += " ".join('#')
            else:
                ans += " ".join('!')

    ans = ans.strip()
    return ans