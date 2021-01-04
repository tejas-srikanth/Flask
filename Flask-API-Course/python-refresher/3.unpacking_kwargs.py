def print_nicely(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key}: {value}')

d = {'a': 1, 'c': 4, 'bob': 'not'}

print_nicely('excelsion', 4, **d)