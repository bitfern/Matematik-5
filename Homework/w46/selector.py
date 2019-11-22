import Homework.w46.factorial as factorial
import Homework.w46.permutations as perm
import Homework.w46.combinations as comb

i = "0"

while i == "0":
    i = str(input("Enter F for factorial, RF for reverse factorial, P for permutation, C for combination"
                  "or X to cancel:   "))
    if i[0] == "F" or "f":
        n = str(input("n! enter n = "))
        print(str(n) + "! = " + str(factorial.factorial(n)))
        i = "0"
    elif i[:2] == "RF" or "rf":
        product = int(input(" n! = "))
        print(str(product) + " = " + str(factorial.factorial_backwards(product)) + "!")
        i = "0"
    elif i[0] == "P" or "p":
        perm.perm_initiate()
        i = "0"
    elif i[0] == "C" or "c":
        comb.comb_initiate()
        i = "0"
    elif i[0] == "X" or "x":
        break
