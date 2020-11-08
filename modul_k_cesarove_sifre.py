# -*- coding: utf-8 -*-


def sifrovani(zadani, posun):
    zprava = ""
    for i in zadani:
        if ord(i) > ord("z") or ord(i) < ord("a"):
            zprava += i
        else:
            znak = ord(i)
            znak += posun
            if znak > ord("z"):
                znak -= 26
            i = chr(znak)
            zprava += i
    return zprava


def desifrovani(zprava, posun):
    text = ""
    for i in zprava:
        if ord(i) > ord("z") or ord(i) < ord("a"):
            text += i
        else:
            znak = ord(i)
            znak -= posun
            if znak < ord("a"):
                znak += 26
            i = chr(znak)
            text += i
    return text
    
    