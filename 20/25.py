import itertools

SUBJECT_NUMBER = 7
MODULUS = 20201227


def modular_exponential_inverse(b, c, m):
    a = 1
    for i in itertools.count():
        if a == c:
            return i
        a = a * b % m


def loop_size(public_key):
    return modular_exponential_inverse(SUBJECT_NUMBER, public_key, MODULUS)


public_keys = tuple(map(int, open("25.txt")))
print(pow(public_keys[0], loop_size(public_keys[1]), MODULUS))
