# Ques 2. With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 12¶
#  Hint by using dictionary comprehension
# then the output should be {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}


n = int(input("Enter the value of n: "))
sqr = {i : i*i for i in range(1, n+1)}
print(sqr)