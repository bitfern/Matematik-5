from factorial import factorial

def combinations(n, k):
    C = (factorial(n) / (factorial(k) * factorial(n - k)))
    return C


high_number = -1
low_number = -1

print("C(n,k) = n! / (k! * (n - k)!)\n" + "n has to be greater than or equal to k")

while high_number < 1 or high_number < 0:
    high_number = int(input("n= "))
    if high_number < 1:
        print("n must be greater than or equal to 1")

while low_number > high_number or low_number < 0:
    low_number = int(input("k= "))
    if low_number > high_number:
        print("k must be smaller than or equal to n")

print("C(" + str(high_number) + "," + str(low_number) + ") = " + str(combinations(high_number, low_number)))
