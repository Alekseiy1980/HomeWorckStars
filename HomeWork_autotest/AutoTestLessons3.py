# from random import randint
#
#
# '''
# задача 1
# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
#
# Найдите количество и выведите его.
# list_1 = [1, 2, 3, 4, 5]
# k = 3
# -> 1
# '''
# # list_1 = ([i+randint(1,10) for i in range(10)])
# # print(list_1)
# # k = int(input("Введите какое значение найти "))
# # print(list_1.count(k))

'''
задача 2
Требуется найти в массиве list_1 самый близкий по величине элемент к
заданному числу k и вывести его.

list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
'''
list_1 = [1, 5, 10, 15, 20]
k = 3

closest = None
for elem in list_1:
    if closest is None or abs(elem - k) < abs(closest - k):
        closest = elem

print(closest)


# '''
# задача3
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
#
#
# А русские буквы оцениваются так:
#
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова k
#  и выводит его. Будем считать, что на вход подается только одно слово, которое
#  содержит либо только английские, либо только русские буквы.
#
#  В случае с английским алфавитом очки распределяются так:
#
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
#
#  k = 'ноутбук'
# # 12
# '''
#
# # from lingua import Language, LanguageDetectorBuilder
# #
# # languages = [Language.ENGLISH, Language.RUSSIAN]
# # detector = LanguageDetectorBuilder.from_languages(*languages)\
# # .with_minimum_relative_distance(0.9)\
# # .build()
# #
# # # print(detector.detect_language_of("languages are awesome"))
# # #
# # # lang = detector.detect_language_of('Привет')
# # # print(lang)
#
# dictionary = {
#     'А': 1, 'В': 1,'Е': 1,'И': 1,'Н': 1,'О': 1,'Р': 1,'С': 1,'Т': 1,
#     'Д': 2,'К': 2,'Л': 2,'М': 2,'П': 2,'У': 2,
#     'Б': 3,'Г': 3,'Ё': 3,'Ь': 3,'Я': 3,
#     'Й': 4,'Ы': 4,
#     'Ж': 5,'З': 5,'Х': 5,'Ц': 5,'Ч': 5,
#     'ш': 8,'Э': 8,'Ю': 8,
#     'Ф': 10,'Щ': 10,'Ъ': 10,
#     'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#     'D': 2, 'G': 2,
#     'B': 3, 'C': 3, 'M': 3, 'P': 3,
#     'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#     'K': 5,
#     'J': 8, 'X': 8,
#     'Q': 10, 'Z': 10
# }
#
#
# say = input("Ваше слово - ")
# count = 0
# # переводим str в верхний регистр
#say = str.upper((say))
#
# list_1 = []
#
# # переводим str in list
# for i in say:
#     list_1.append(i)
#
# # подсчет  баллов в слове
# for i in list_1:       # берем литеру
#     for item in dictionary:   #проходимся по словарю
#         if i == item:         #проверяем литеру с ключом словаря
#             # print(dictionary[item])
#             count += dictionary[item]
#
# print(count)