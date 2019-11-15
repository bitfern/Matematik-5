def factorial(number):
    if number == 0:
        return 1
    elif number < 0:
        print ("ERROR negative number entered")
        return
    else:
        product = 1
        for i in range(0, number):
            product = product * (number - i)
    return product

print(factorial(5))
