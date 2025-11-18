import random
chars = "abcdefghijklmnopqrstuvwxyz0123456789"
password = "".join(random.choice(chars) for _ in range(8))
print(password)
