#made by easin

import string
import random

p = string.ascii_letters
y = string.digits
t = string.punctuation
h = string.ascii_uppercase
on = string.ascii_lowercase

e = []
e.extend(list(p))
e.extend(list(y))
e.extend(list(t))
e.extend(list(h))
e.extend(list(on))
random.shuffle(e)
easin = int(input("Enter the length of password: "))

password = "".join(e[0:easin])
print("Your password is:", password)
