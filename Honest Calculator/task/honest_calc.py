# write your code here
def check_cal(calc):
    global memory
    global result
    bad_input = True
    while bad_input:
        x = calc[0]
        y = calc[2]
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        try:
            x = float(x)
            y = float(y)
        except:
            print("Do you even know what numbers are? Stay focused!")
            print("Enter an equation")
            calc = input().split()
            bad_input = True
        else:
            if calc[1] not in ["+", "-", "*", "/"]:
                print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
                print("Enter an equation")
                calc = input().split()
                bad_input = True
            elif calc[1] == "+":
                result = x + y
                bad_input = False
            elif calc[1] == "-":
                result = x - y
                bad_input = False
            elif calc[1] == "*":
                result = x * y
                bad_input = False
            elif calc[1] == "/" and y != 0:
                result = x / y
                bad_input = False
            else:
                print("Yeah... division by zero. Smart move...")
                print("Enter an equation")
                calc = input().split()
                bad_input = True
    print(result)


memory = 0
result = 0
print("Enter an equation")
_calc = input().split()
check_cal(_calc)


def store_result():
    print("Do you want to store the result? (y / n):")
    s_answer = input()
    while s_answer not in ["y", "n"]:
        print("Do you want to store the result? (y / n):")
        s_answer = input()
    if s_answer == "y":
        global memory
        memory = result


store_result()
print("Do you want to continue calculations? (y / n):")
ctn_answer = input()
while ctn_answer != "n":
    if ctn_answer == "y":
        print("Enter an equation")
        _calc = input().split()
        check_cal(_calc)
        store_result()
    print("Do you want to continue calculations? (y / n):")
    ctn_answer = input()
