class BigNum:
    def __init__(self, M, N):
        self.M = M
        self.N = N

    def to_base_m(self, num):
        """Преобразует целое число сначала в младшие разряды"""
        if num == 0:
            return [0], False
        is_negative = num < 0
        num = abs(num)
        # Расчет необходимого размера
        digit_count = 0
        temp = num
        while temp > 0:
            digit_count += 1
            if digit_count > self.N:
                raise OverflowError(f"The number exceeds the limit of {self.N} digits")
            temp //= self.M

        # Распределение и преобразование
        digits = [0] * digit_count
        temp = num
        for i in range(digit_count):
            digits[i] = temp % self.M
            temp //= self.M

        return digits, is_negative

    def from_base_m(self, digits, is_negative=False):
        """Преобразует в целые числа"""
        if not digits or digits == [0]:
            return 0

        for d in digits:
            if d < 0 or d >= self.M:
                raise ValueError(f"Digit {d} invalid for base {self.M}")

        # Reconstruction
        num = 0
        for i in range(len(digits) - 1, -1, -1):
            num = num * self.M + digits[i]

        return -num if is_negative else num

    def input_number(self, prompt):
        nombre_str = input(prompt)
        try:
            nombre_int = int(nombre_str)
            digits, is_negative = self.to_base_m(nombre_int)
            return digits, is_negative
        except ValueError:
            print("Invalid entry, please enter an integer.")
            return self.input_number(prompt)

    def display_number(self, digits, is_negative=False):
        """Отображает число в удобочитаемом виде"""
        sign = "-" if is_negative else ""
        digits_str = ' '.join(f"[{d}]" for d in digits)
        return f"{sign}{digits_str}"

    def compare(self, a_digits, a_negative, b_digits, b_negative):
        """Сравнивает два числа, возвращает -1, если a < b, 0, если a == b, 1, если a > b"""
        if a_negative and not b_negative:
            return -1
        elif not a_negative and b_negative:
            return 1

        # Одинаковый знак, сравнение абсолютных значений
        if len(a_digits) != len(b_digits):
            if not a_negative:  # Both positive
                return 1 if len(a_digits) > len(b_digits) else -1
            else:  # Both negative
                return -1 if len(a_digits) > len(b_digits) else 1

        # Одинаковая длина, сравнение по цифрам (наибольший вес в конце)
        for i in range(len(a_digits) - 1, -1, -1):
            if a_digits[i] != b_digits[i]:
                if not a_negative:  # Both positive
                    return 1 if a_digits[i] > b_digits[i] else -1
                else:  # Both negative
                    return -1 if a_digits[i] > b_digits[i] else 1

        return 0

    def add(self, a_digits, a_negative, b_digits, b_negative):
        """Сложение двух чисел с обработкой знаков"""
        #Case 1: a positive, b negative → a - |b|
        if not a_negative and b_negative:
            return self.subtract(a_digits, False, b_digits, False)

        # Case 2: a négative, b positive → b - |a|
        if a_negative and not b_negative:
            return self.subtract(b_digits, False, a_digits, False)

        # Cas 3: тот же знак
        result = []
        carry = 0
        max_len = max(len(a_digits), len(b_digits))

        for i in range(max_len):
            a_val = a_digits[i] if i < len(a_digits) else 0
            b_val = b_digits[i] if i < len(b_digits) else 0
            total = a_val + b_val + carry
            carry = total // self.M
            digit = total % self.M
            result.append(digit)

        if carry > 0:
            if len(result) >= self.N:
                raise OverflowError("Result exceeds limit N")
            result.append(carry)

        return result, a_negative

    def subtract(self, a_digits, a_negative, b_digits, b_negative):
        """Вычитает два числа с учётом знака"""
        # Case 1: a positive, b négative → a + |b|
        if not a_negative and b_negative:
            return self.add(a_digits, False, b_digits, False)

        # Case 2: a négative, b positive → -(|a| + b)
        if a_negative and not b_negative:
            result_digits, _ = self.add(a_digits, False, b_digits, False)
            return result_digits, True

        # Cas 3: тот же знак
        comparison = self.compare(a_digits, False, b_digits, False)

        if comparison == 0:  # a == b
            return [0], False

        if comparison < 0:  # |a| < |b|
            #  a - b = -(b - a)
            if not a_negative:
                result_digits = self._subtract_absolute(b_digits, a_digits)
                return result_digits, True
            else:  #  (-a) - (-b) = b - a
                result_digits = self._subtract_absolute(b_digits, a_digits)
                return result_digits, False
        else:  # |a| > |b|
            #  a - b
            if not a_negative:
                result_digits = self._subtract_absolute(a_digits, b_digits)
                return result_digits, False
            else:  #  (-a) - (-b) = -(a - b)
                result_digits = self._subtract_absolute(a_digits, b_digits)
                return result_digits, True

    def _subtract_absolute(self, larger_digits, smaller_digits):
        """Вычитает два положительных числа (больше >= меньше)"""
        result = []
        borrow = 0

        for i in range(len(larger_digits)):
            a_val = larger_digits[i]
            b_val = smaller_digits[i] if i < len(smaller_digits) else 0

            diff = a_val - b_val - borrow
            if diff < 0:
                diff += self.M
                borrow = 1
            else:
                borrow = 0

            result.append(diff)

        # Очистка начальных нулей
        while len(result) > 1 and result[-1] == 0:
            result.pop()

        return result


# main:
base = 100
N = 10
long_arith = BigNum(base, N)

print(" Введите первое число :")
a_digits, a_negative = long_arith.input_number("Number 1 : ")

print("Введите первое число :")
b_digits, b_negative = long_arith.input_number("Number 2 : ")

print("Number 1:", long_arith.display_number(a_digits, a_negative))
print("Number 2:", long_arith.display_number(b_digits, b_negative))

result_add, result_neg_add = long_arith.add(a_digits, a_negative, b_digits, b_negative)
result_sub, result_neg_sub = long_arith.subtract(a_digits, a_negative, b_digits, b_negative)
print("Addition:", long_arith.from_base_m(result_add, result_neg_add))
print("Subtraction:", long_arith.from_base_m(result_sub, result_neg_sub))

