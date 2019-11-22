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


def factorial_backwards(product):
    tmp_product = 1
    i = 0
    while tmp_product<product:
        i = i + 1
        tmp_product = i * tmp_product

    return i

