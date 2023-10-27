def factorial(num):
    result = num
    if num == 0:
        result = 1
    for i in range(num , 1, -1):
        result *= i-1

    return result

print(factorial(1))
print(factorial(5))
print(factorial(7))
print(factorial(13))
