def Caesar_Cipher(s, k):
    result = ""
    k = k % 26 
    for char in s:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            new_pos = (ord(char) - ord(base) + k) % 26
            result += chr(ord(base) + new_pos)
        else:
            result += char
    return result