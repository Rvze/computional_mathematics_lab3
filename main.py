def error_late(k):
    error_late = {}
    error_late["h"] = answer["answer"]
    if k == 4:
        error_late["h/2"] = simpson_method_half(data["a"], data["b"], data["error"], data["function"])
    else:
        error_late["h/2"] = trapezoid_method_half(data["a"], data["b"], data["error"], data["function"])
    return (abs(error_late["h/2"] - error_late["h"])) / (2 ** k - 1)


def simpson_method_half(a, b, error, function, start_n=4):
    try:
        n = start_n
        summa = float("inf")
        while True:
            h = (b - a) / n
            last_sum = summa
            summa = function(a) + function(b)
            x = a + h
            for k in range(1, n + 1):
                if k % 2 == 0:
                    summa += 4 * function(x)
                else:
                    summa += 2 * function(x)
                x += h
            summa *= h / 6

            if abs(summa - last_sum) <= error:
                break
            else:
                n *= 2

        return summa

    except ZeroDivisionError:
        print("Деление на ноль!")


def simpson_method(a, b, error, function, start_n=4):
    try:
        n = start_n
        summa = float("inf")
        while True:
            h = (b - a) / n
            last_sum = summa
            summa = function(a) + function(b)
            x = a + h
            for k in range(1, n + 1):
                if k % 2 == 0:
                    summa += 4 * function(x)
                else:
                    summa += 2 * function(x)
                x += h
            summa *= h / 3

            if abs(summa - last_sum) <= error:
                break
            else:
                n *= 2

        return summa, n

    except ZeroDivisionError:
        print("Деление на ноль!")


def trapezoid_method_half(a, b, error, function, start_n=5):
    n = start_n
    sum = float("inf")

    while True:
        last_sum = sum
        sum = (function(a) + function(b)) / 2

        h = (b - a) / n
        x = a + h
        for k in range(1, n):
            sum += function(x)
            x += h
        sum *= h / 2
        if abs(sum - last_sum) <= error:
            break
        else:
            n *= 2
    return sum


def trapezoid_method(a, b, error, function, start_n=5):
    n = start_n
    sum = float("inf")

    while True:
        last_sum = sum
        sum = (function(a) + function(b)) / 2

        h = (b - a) / n
        x = a + h
        for k in range(1, n):
            sum += function(x)
            x += h
        sum *= h
        if abs(sum - last_sum) <= error:
            break
        else:
            n *= 2
    return sum, n


def get_error():
    print("Введите погрешность вычисления: ")
    while True:
        try:
            error = float(input(">>>"))
            if error <= 0:
                raise ArithmeticError
            return error
        except ArithmeticError:
            print("Погрешность вычислений должен быть больше или равен нуля!")


def get_integration_limit():
    limit = {}
    while True:
        try:
            a = float(input("Введите нижний предел: "))
            b = float(input("Введите верхний предел: "))
            if a > b:
                a, b = b, a
            break
        except ValueError:
            print("Введите пределы")
    limit["a"] = a
    limit["b"] = b
    return limit["a"], limit["b"]


def method_handler(method_type):
    if method_type == "1":
        return "simpson_method"
    elif method_type == "2":
        return "trapezoid_method"
    else:
        return None


def get_method():
    while True:
        try:
            method_type = input()
            method = method_handler(method_type)
            if method is None:
                raise AttributeError
            return method
        except AttributeError:
            print("Данного метода нет в списке, попробуйте снова: ")


def func_handler(func_id):
    if func_id == "1":
        return lambda x: x / (x ** 4 + 4)
    elif func_id == "2":
        return lambda x: (1 - x) / x ** 2
    elif func_id == "3":
        return lambda x: 1 - x ** 2
    elif func_id == "4":
        return lambda x: 3 * x ** 3 + 5 * x ** 2 + 3 * x - 6
    else:
        return None


def get_func():
    print("\tВыберите функцию:")
    print("1 - x/(x^4+4)")
    print("2 - (1-x^2)/x")
    print("3 - 1-x^2")
    print("4 - 3x^3 + 5x^2 + 3x - 6")
    while True:
        try:
            func_id = input()
            func = func_handler(func_id)
            if func is None:
                raise AttributeError
            return func
        except AttributeError:
            print("Данной функции нет в списке, попробуйте снова")


# Получить данные с клавиатуры
def data_input():
    data = {}

    print("\tВыберите метод интегрирования:")
    print("1 - метод Симпсона")
    print("2 - метод трапеций")
    data["method"] = get_method()
    data["function"] = get_func()
    data["a"], data["b"] = get_integration_limit()
    data["error"] = get_error()
    return data


if __name__ == '__main__':
    answer = {}
    print("\tЛабораторная работа №3")
    print("\tЧисленное интегрирование")
    data = data_input()
    if data["method"] == "simpson_method":
        answer["answer"], answer["partitions"] = simpson_method(data["a"], data["b"], data["error"], data["function"])
        answer["error_late"] = error_late(4)
    elif data["method"] == "trapezoid_method":
        answer["answer"], answer["partitions"] = trapezoid_method(data["a"], data["b"], data["error"], data["function"])
        answer["error_late"] = error_late(2)
    print("Ответ: ", answer["answer"])
    print("Количество разбиений: ", answer["partitions"])
    print("Оценка погрешности: ", answer["error_late"])
