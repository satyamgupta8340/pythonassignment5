
# Ques 3. Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints:Use init method to construct some parameters

class IOstring():
    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())

str1 = IOstring()
str1.get_string()
str1.print_string()