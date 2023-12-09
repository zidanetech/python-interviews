"""
    Challange One
    12/23
    M.Z
"""

def app(a, b):
    return {
        "sum": sum([a, b]),
        "diff": (a - b),
        "prod": (a*b)
    }

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    if ((a >= 1 and a <= 10**10) and (b >= 1 and b <= 10**10)):
        dict_res = app(a, b)
        print(dict_res)
        print(dict_res["sum"])
        print(dict_res["diff"])
        print(dict_res["prod"])
    else:
        print("Value not in set")
