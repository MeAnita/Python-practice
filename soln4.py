def is_divisible(number, divisor):
    if (number % divisor) == 0:
        return(True)
    else:
        return(False)

print(is_divisible (10,2))
print(is_divisible(10,3))
