import re
from random import randint
from faker import Faker


# 1. Написать функцию, которая принимает на вход список целых чисел и возвращает новый список, содержащий только уникальные элементы из исходного списка.
def unique_elems(items_list: list):
    return list(frozenset(items_list))


# 2. Написать функцию, которая принимает на вход два целых числа (минимум и максимум) и возвращает список всех простых чисел в заданном диапазоне.
def range_(min_value=0, max_value=0):
    return list(range(min_value, max_value + 1))


# 3. Создать класс Point, который представляет собой точку в двумерном пространстве. Класс должен иметь методы для инициализации координат точки,
# вычисления расстояния до другой точки, а также для получения и изменения координат.
class Point:
    def __init__(self, pos_x=0, pos_y=0):
        self.__x = pos_x
        self.__y = pos_y

    @property
    def coordinates(self) -> tuple:
        return self.__x, self.__y,

    @coordinates.setter
    def coordinates(self, x=None, y=None):
        if x is not None:
            self.__x = x
        if y is not None:
            self.__y = y

    def get_distance(self, point: "Point") -> tuple:
        self._is_valid(point)
        return tuple(map(lambda cords: cords[0] - cords[1], zip(self.coordinates, point.coordinates)))

    def __sub__(self, point):
        self._is_valid(point)
        return self.get_distance(point)

    def _is_valid(self, other_point: "Point"):
        if type(other_point) is not self.__class__:
            raise TypeError


# 4. Написать программу, которая сортирует список строк по длине, сначала по возрастанию, а затем по убыванию.
def merge_sort(input_: list[str], decr=False):  # O(n * log(n))
    """ Рекурсивная реализация """
    def merge(left, right):
        result = []
        l_ = r = 0
        while l_ < len(left) and r < len(right):
            if len(left[l_]) < len(right[r]):
                if not decr:
                    result.append(left[l_])
                    l_ += 1
                else:
                    result.append(right[r])
                    r += 1
            else:
                if not decr:
                    result.append(right[r])
                    r += 1
                else:
                    result.append(left[l_])
                    l_ += 1
        if not decr:
            if l_ < len(left):
                result.extend(left[l_:])
            if r < len(right):
                result.extend(right[r:])
        else:
            if r < len(right):
                result.extend(right[r:])
            if l_ < len(left):
                result.extend(left[l_:])
        return result

    def recursive_divide(elems):
        if len(elems) == 1:
            return elems
        left = recursive_divide(elems[:len(elems) // 2])
        right = recursive_divide(elems[elems.__len__() // 2:])
        return merge(left, right)
    return recursive_divide(input_)


if __name__ == "__main__":
    print(f"1) {[1, 2, 3, 3, 3, 3]} -> {unique_elems([1, 2, 3, 3])}")
    print(f"2) {range_(randint(0, 200), randint(200, 300))}")
    print(f"3) {Point(10, 10).get_distance(Point(5, 5))}")
    print(f"3) {Point(10, 10) - Point(5, 5)}")
    text = Faker().text()
    r = re.compile(r"\b\w|[а-яА-я]+\b", flags=re.S)
    print(f"4) {merge_sort(re.split(r, text))}")
    print(f"4) {list(map(lambda x: len(x), merge_sort(re.split(r, text))))}")
    print("Обратно, - убывание")
    print(f"4) {merge_sort(re.split(r, text), decr=True)}")
    print(f"4) {list(map(lambda x: len(x), merge_sort(re.split(r, text), decr=True)))}")
