def plus_one(digits: list[int]) -> list[int]:
    for i in range(len(digits)-1, -1, -1):
        if(digits[i]<9):
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits

a = [9,9,9]
b = plus_one(a)
print(b)
