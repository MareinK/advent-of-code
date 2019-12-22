zero = lambda *args, **kwargs: 0
identity = lambda x: x


def search(f, g, s):
    while f:
        n = f.get()
        if g(n):
            return n
        for m in s(n):
            f.put(m)
