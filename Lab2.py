"""Реализуйте рекурсивную функцию нарезания прямоугольника с заданными пользователем
сторонами a и b на квадраты с наибольшей возможной на каждом этапе стороной.
Выведите длины ребер получаемых квадратов и кол-во полученных квадратов."""


def square_cut(wight_1, height_1, num=0):
    while wight_1 - height_1 >= height_1:
        return print(height_1)
    if wight_1 - height_1 < height_1:
        if height_1 != 0:
            return
    print("Длина ребра квадрата: " + str(height_1))
    num += 1
    return print("Количество квадратов: " + str(num))


wight_1 = int(input("Введите ширину прямоугольника:\n"))
height_1 = int(input("Введите высоту прямоугольника:\n"))