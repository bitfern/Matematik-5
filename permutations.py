from factorial import factorial

def permutation(n,k):
    P = (factorial(n)) / factorial(n - k)
    return P


high_number = 0
low_number = 0

print("P(n,k) = n! / (n - k)!\n" + "n has to be greater than or equal to k")

while high_number < 1 or high_number <= 0:
    high_number = int(input("n= "))
    if high_number < 1:
        print("n must be greater than or equal to 1")

while low_number > high_number or low_number <= 0:
    low_number = int(input("k= "))
    if low_number < high_number:
        print("k must be smaller than or equal to n")

print("P(" + str(high_number) + "," + str(low_number) + ") = " + str(permutation(high_number, low_number)))
