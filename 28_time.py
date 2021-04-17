import termcolor2

print(termcolor2.colored("Time Sum", color="green"))


def sum():
    h1 = int(input("Enter Hour1: "))
    m1 = int(input("Enter Minutes1: "))
    if 0 > m1 or m1 > 60:
        print(termcolor2.colored("TryAgain", color="red"))
        exit()
    s1 = int(input("Enter Seconds1: "))
    if 0 > s1 or s1 > 60:
        print(termcolor2.colored("TryAgain", color="red"))
        exit()
    h2 = int(input("Enter Hour2: "))
    m2 = int(input("Enter Minutes2: "))
    if 0 > m2 or m2 > 60:
        print(termcolor2.colored("TryAgain", color="red"))
        exit()
    s2 = int(input("Enter Seconds2: "))
    if 0 > s2 or s2 > 60:
        print(termcolor2.colored("TryAgain", color="red"))
        exit()
    result1 = {"h": h1, "m": m1, "s": s1}
    print(result1["h"], ":", result1["m"], ":", result1["s"], end="\t")
    result2 = {"h": h2, "m": m2, "s": s2}
    print(result2["h"], ":", result2["m"], ":", result2["s"])
    result3 = {"h": h1 + h2, "m": m1 + m2, "s": s1 + s2}
    return result3


res = sum()
print(res["h"], ":", res["m"], ":", res["s"])

print(termcolor2.colored("Time Minus", color="green"))


def minus():
    h1 = int(input("Enter Hour1: "))
    m1 = int(input("Enter Minutes1: "))
    if 0 > m1 or m1 > 60:
        print(termcolor2.colored("TryAgain", color="red"))
        exit()
    s1 = int(input("Enter Seconds1: "))
    if 0 > s1 or s1 > 60:
        print(termcolor2.colored("TryAgain", color="red"))
        exit()
    h2 = int(input("Enter Hour2: "))
    m2 = int(input("Enter Minutes2: "))
    if 0 > m2 or m2 > 60:
        print(termcolor2.colored("TryAgain", color="red"))
        exit()
    s2 = int(input("Enter Seconds2: "))
    if 0 > s2 or s2 > 60:
        print(termcolor2.colored("TryAgain", color="red"))
        exit()
    result1 = {"h": h1, "m": m1, "s": s1}
    print(result1["h"], ":", result1["m"], ":", result1["s"], end="\t")
    result2 = {"h": h2, "m": m2, "s": s2}
    print(result2["h"], ":", result2["m"], ":", result2["s"])
    result3 = {"h": h1 - h2, "m": m1 - m2, "s": s1 - s2}
    return result3


res = minus()
print(res["h"], ":", res["m"], ":", res["s"])

print(termcolor2.colored("Convert Time To Seconds", color="green"))


def time():
    h = int(input("Enter Hour: "))
    m = int(input("Enter Minutes: "))
    s = int(input("Enter Seconds: "))
    print(f"{h} : {m} : {s}")
    hour = h * 3600
    minute = m * 60
    result = hour + minute + s
    return result


res = time()
print(f"Seconds: {res}")
