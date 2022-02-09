'''
task 1
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль
'''
'''
Имя функции: divide_param_by_param (divide parameter by parameter)
Назначение функции: деление одного параметра на другой
Типы данных параметров: float
Типы данных результата: float
Имена параметров функции:
делимое dividend;
делитель divider;
частное от деления quotient of division – quot_of_divis
'''


def divide_param_by_param(dividend, divider):
    # Делимое dividend; делитель divider; частное от деления quotient of division – quot_of_divis
    if divider == 0:
        print("Нельзя делить на ноль")
    else:
        quot_of_divis = dividend / divider
        print(quot_of_divis)


dividend = float(input("Введите число которое требуется разделить (делимое): "))
divider = float(input("Введите число на которое требуется разделить (делитель): "))
divide_param_by_param(dividend, divider)
'''
task 2
Выполнить функцию, которая принимает несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
 город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы.
 Осуществить вывод данных о пользователе одной строкой.
'''
'''
Имя функции: принять и вывести данные пользователя (accept_and_display_user_data)
Назначение функции: принять и вывести данные пользователя
Имена и типы данных параметров:
имя – str – user_name;
фамилия – str – user_surname;
год рождения – int – user_year_bith;
город проживания – str – user_city;
email – str – user_email;
телефон – str – user_phone.
Имена и типы данных результата:  аналогичны именам и типам данных параметров

'''


def accept_and_display_user_data(user_name, user_surname, user_year_bith, user_city, user_email, user_phone):
    return print(
        f"имя пользователя: {user_name}; фамилия пользователя: {user_surname};"
        f"год рождения пользователя: {user_year_bith}; город проживания пользователя: {user_city};"
        f"email пользователя: {user_email}; телефон пользователя: {user_phone}")


user_name = str(input("Введите имя пользователя: "))
user_surname = str(input("Введите фамилию пользователя: "))
user_year_bith = int(input("Введите год рождения пользователя: "))
user_city = str(input("Введите город проживания пользователя: "))
user_email = str(input("Введите email пользователя: "))
user_phone = str(input("Введите телефон пользователя: "))

accept_and_display_user_data(user_year_bith=user_year_bith, user_city=user_city, user_phone=user_phone,
                             user_name=user_name, user_email=user_email, user_surname=user_surname)
'''
task 3
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента
 и возвращает сумму наибольших двух аргументов.
'''
'''
Имя функции: сравнить три значения (my_func)
Назначение функции: сравнить три значения
Имена и типы данных параметров:
первый – int – first_arg;
второй – int – second_arg;
третий – int – third_arg;
Имена и типы данных результата:  аналогичны именам и типам данных параметров
Тело функции: ...

'''
def my_func(first_arg, second_arg, third_arg):
    print(f'Сумма двух наибольших аргументов равна: '
          f'{first_arg + second_arg + third_arg - min([first_arg, second_arg, third_arg])}')


first_arg = int(input("Введите первый аргумент (число):"))
second_arg = int(input("Введите второй аргумент (число):"))
third_arg = int(input("Введите первый аргумент (число):"))

my_func(first_arg, second_arg, third_arg)
'''
task 4
4. Программа принимает действительное положительное
 число x и целое отрицательное число y.
  Выполните возведение числа x в степень y.
   Задание реализуйте в виде функции my_func(x, y).
    При решении задания нужно обойтись
     без встроенной функции возведения числа в степень.

Подсказка: попробуйте решить задачу двумя способами.
 Первый — возведение в степень с помощью оператора **.
  Второй — более сложная реализация без оператора **,
   предусматривающая использование цикла.
'''
'''

'''

def my_func(x, y):
    return 1 / x ** abs(y)


xx = int(input("Введите действительное положительное число: "))
yy = int(input("Введите целое отрицательное число: "))
print(my_func(xx, yy))

'''
task 5
5. Программа запрашивает у пользователя строку чисел,
 разделённых пробелом. При нажатии Enter должна выводиться сумма чисел.
  Пользователь может продолжить ввод чисел,
   разделённых пробелом и снова нажать Enter.
    Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ,
 выполнение программы завершается.
  Если специальный символ введён после нескольких чисел,
   то вначале нужно добавить сумму этих чисел к полученной
    ранее сумме и после этого завершить программу.
'''
def my_sum():
    total_result = 0
    ex = False
    while ex == False:
        value = input('Введите число (или несколько чисел через пробел)'
                      ' или G (или g) для выхода из программы - ').split()

        result = 0
        for el in range(len(value)):
            if value[el] == 'g' or value[el] == 'G':
                ex = True
                break
            else:
                result = result + int(value[el])
        total_result = total_result + result
        print(f'Текущая сумма {total_result}')
    print(f'Финальная сумма {total_result}')


my_sum()
'''
task 6 и 7
6. Реализовать функцию int_func(),
принимающую слова из маленьких латинских букв и возвращающую их же,
 но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
'''


def int_func(a):
    return a.title()


a = input("Введите слова, через пробел, из маленьких латинских букв: ")
print(int_func(a))
'''
7. Продолжить работу над заданием. В программу должна попадать строка из слов,
 разделённых пробелом. Каждое слово состоит из латинских букв в нижнем регистре.
  Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
   Используйте написанную ранее функцию int_func().
'''


def int_func(a):
    return a.title()


output = []
for word in input('Введите строку из слов разделенных пробелами '
                  'и состоящих из маленьких латинских букв: ').split(' '):
    output.append(int_func(word))

print(f'Результат: {" ".join(output)}')
