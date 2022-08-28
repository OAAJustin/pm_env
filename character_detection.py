import chardet

def character_detect(detect):
    with open(detect, 'rb') as file:
        print(chardet.detect(file.read()))

