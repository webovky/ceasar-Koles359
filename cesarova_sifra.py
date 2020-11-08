# -*- coding: utf-8 -*-


import modul_k_cesarove_sifre

start = input("Chcete spustit program? y/n : ")

while start == "y":
    print("\n")
    vstup = int(input("Zadej 1 pokud chceš šifrovat nebo 2 pokud chceš dešifrovat: "))
    print("\n")

    if vstup < 1 or vstup > 2:
        print("\n")
        print("Musíš zadat 1 pokud chceš šifrovat nebo 2 pokud chceš dešifrovat!")
        print("\n")
        start = input("Chcete v programu pokračovat? y/n : ")
    else:
        if vstup == 1:
            zadani = input("Zadej zprávu k šifrování (bez interpunkce, diakritiky a mezer!!!): ").lower()
            posun = int(input("Zadej posun: "))
            print("\n")
            print(modul_k_cesarove_sifre.sifrovani(zadani, posun))
            print("\n")
            start = input("Chcete v programu pokračovat? y/n : ")
        else:
            zprava = input("Zadej zprávu k dešifrování (bez interpunkce, diakritiky a mezer!!!): ").lower()
            posun = int(input("zadej posun: "))
            print("\n")
            print(modul_k_cesarove_sifre.desifrovani(zprava, posun))
            print("\n")
            start = input("Chcete v programu pokračovat? y/n : ")
    