import random


lower_case = 'qwertyuioplkjhgfdsazxcvbnm'
upper_case = 'QWERTYUIOPLKJHGFDSAZXCVBNM'
number = '0987654321'
symbols = '!@#$%^&*()_-=+}{[]|;:<>,.?/`~'
Use_for = "{0}{1}{2}{3}".format(lower_case, upper_case, number, symbols)
length = 8
password = "".join(random.sample(Use_for, length))
print("your secure password is:", password)
