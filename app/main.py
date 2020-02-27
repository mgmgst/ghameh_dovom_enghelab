import config
def check(username,password):
    res = False
    if username == config.usernamein and password == config.passwordin:
        res = True
    return res