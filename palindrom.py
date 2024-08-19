def check_palindrom(some_str):
    if some_str == some_str[::-1]:
        print("PALINDROM")
    else:
        print("NO")

    # for i in some_str:
check_palindrom("abba")