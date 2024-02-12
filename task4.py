#!/usr/bin/env python
# coding: utf-8

# # Классы
# ## Домашнее задание

# ### Вопросы по лекциям
# 
# #### 1.
# 
# Напишите название функции, которая является конструктором класса.

# **Ответ:**
def __init__():
    pass


# #### 2.
# 
# На что указывает переменная `self`?

# **Ответ:**
# Переменная `self` ссылается текущий на экземпляр объекта

# #### 3.
# С помощью какой функции можно проверить, что некая строка является именем одного из атрибутов объекта?

# **Ответ:**
hasattr(object, name)


# #### 4.
# Когда вызывается метод `__del__`? (относительно события удаления объекта)

# **Ответ:**
# В момент завершения работы экземпляра класса

# #### 5.
# Верно ли, что атрибут класса перекрывает атрибут объекта?

# **Ответ:**
# Да

# #### 6.
# Можно ли атрибуты базового класса вызывать в дочернем классе? Если да, то напишите, нет ли исключений?

# **Ответ:**
# Можно, исключения составляет ф-я super()

# #### 7.
# Объясните своими словами для чего нужен метод `super`.

# **Ответ:**
# Для того чтоб переназначить родительские методы
# ### Практика
# 
# 1. Напишите класс `Fraction` для работы с дробями.
# Пусть дробь в нашем классе предстает в виде `числитель/знаменатель`.
# Дробное число должно создаваться по запросу `Fraction(a, b)`, где `a` – это числитель, а `b` – знаменатель дроби.
# 2. Добавьте возможность сложения (сложения через оператор сложения) для дроби.
# Предполагается, что операция сложения может проводиться как только между дробями,
# так и между дробью и целым числом. Результат операции должен быть представлен в виде дроби.
# 3. Добавьте возможность взятия разности (вычитания через оператор вычитания) для дробей.
# Предполагается, что операция вычитания может проводиться как только для двух дробей,
# так и для дроби и целого числа. Результат операции должен быть представлен в виде дроби.
# 4. Добавьте возможность умножения (умножения через оператор умножения) для дробей.
# Предполагается, что операция умножения может проводиться как только для двух дробей,
# так и для дроби и целого числа. Результат операции должен быть представлен в виде дроби.
# 5. Добавьте возможность приведения дроби к целому числу через стандартную функцию `int()`.
# 6. Добавьте возможность приведения дроби к числу с плавающей точкой через стандартную функцию `float()`.
# 7. Создайте дочерний класс `OperationsOnFraction`
# и добавьте туда собственные методы `getint` и `getfloat`,
# которые будут возвращать целую часть дроби и представление дроби в виде числа с плавающей точкой соответственно.

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __int__(self):
        return self.numerator // self.denominator

    def __float__(self):
        return self.numerator / self.denominator


class OperationsOnFraction(Fraction):
    def getint(self):
        return int(self)

    def getfloat(self):
        return float(self)


# Пример использования:
fraction1 = Fraction(3, 4)
fraction2 = Fraction(1, 2)
result_sum = fraction1 + fraction2
result_difference = fraction1 - fraction2
result_product = fraction1 * fraction2
print("Сумма:", result_sum.numerator, "/", result_sum.denominator)
print("Разность:", result_difference.numerator, "/", result_difference.denominator)
print("Произведение:", result_product.numerator, "/", result_product.denominator)

# Примеры приведения к целому числу и числу с плавающей точкой
fraction3 = Fraction(5, 2)
print("Приведение к целому числу:", int(fraction3))
print("Приведение к числу с плавающей точкой:", float(fraction3))

# Примеры использования дочернего класса
fraction4 = OperationsOnFraction(7, 3)
print("Целая часть:", fraction4.getint())
print("Число с плавающей точкой:", fraction4.getfloat())
