def toLowerCase(s: str) -> str:
    new_string = ''
    for c in s:
        if(ord(c)>= ord("A") and ord(c)<=ord("Z")):
            new_string += chr(ord(c)+32)
            continue
        new_string += c
    return new_string