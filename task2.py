#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Ввод двух строк с клавиатуры
    string1 = input("Введите первую строку: ")
    string2 = input("Введите вторую строку: ")

    # Преобразование строк в множества уникальных символов
    set1 = set(string1)
    set2 = set(string2)

    # Определение общих символов
    common_characters = set1.intersection(set2)

    print(f"Общие символы в двух введенных строках: {common_characters}")

