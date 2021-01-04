from functools import wraps

def capitalize(func):
    @wraps(func)
    def make_upper():
        return func().upper()
    
    return make_upper

@capitalize
def say_hi():
    return 'Hi there'

print(say_hi.__name__)