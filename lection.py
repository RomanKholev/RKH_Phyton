data [1, 2, 3, 4, 5]

def select(f, col):
    return [f(x) for x in col]
