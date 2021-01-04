import functools
me = {"name": "Tejas", "level": "admin"}

def secure_get_password(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if me["level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No password for you, {me['name']}"
    return secure_function

@secure_get_password
def get_admin_password(panel):
    if panel == "admin":
        return 1234
    elif panel == "billing":
        return "super_secret_password"

get_admin_password = secure_get_password(get_admin_password)
print(get_admin_password("admin"))