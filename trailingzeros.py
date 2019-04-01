def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

def count_trailing(num):
    if num < 5:
        return 0
    else:
        return 1

for i in range(5, 21):
    print(factorial(i))
