# Первое задание

# == Предложенный метод ==

# def isEven(value):
#     return value % 2 == 0

# Преимущества:
# 1. Интуитивно понятен
# 2. Корректно обрабатывает вещественные числа
#
# Недостатки:
# 1. Медленнее


# == Мой метод ==
def isEven(num: int) -> bool:
    return num & 1 == 0

# Преимущества:
# 1. Быстрее
#
# Недостатки:
# 1. Менее читабельный
# 2. Непредвиденное поведение для вещественных чисел

def isEven_test():
    assert isEven(0) == True
    assert isEven(2) == True
    assert isEven(10) == True
    assert isEven(100) == True
    assert isEven(1000) == True

    assert isEven(1) == False
    assert isEven(3) == False
    assert isEven(11) == False
    assert isEven(101) == False
    assert isEven(1001) == False

    assert isEven(-2) == True
    assert isEven(-10) == True
    assert isEven(-100) == True

    assert isEven(-1) == False
    assert isEven(-3) == False
    assert isEven(-11) == False

    return True

if __name__ == '__main__':
    print(isEven_test())