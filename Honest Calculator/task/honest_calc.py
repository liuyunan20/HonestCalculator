# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
msg_ = [msg_0, msg_1, msg_2, msg_3, msg_4, msg_5, msg_6, msg_7, msg_8, msg_9, msg_10, msg_11, msg_12]

def check_cal(calc):
    global memory
    global result
    bad_input = True
    while bad_input:
        x = calc[0]
        oper = calc[1]
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
            if oper not in ["+", "-", "*", "/"]:
                print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
                print("Enter an equation")
                calc = input().split()
                bad_input = True
            else:
                check(x, y, oper)
                if oper == "+":
                    result = x + y
                    bad_input = False
                elif oper == "-":
                    result = x - y
                    bad_input = False
                elif oper == "*":
                    result = x * y
                    bad_input = False
                elif oper == "/" and y != 0:
                    result = x / y
                    bad_input = False
                else:
                    print("Yeah... division by zero. Smart move...")
                    print("Enter an equation")
                    calc = input().split()
                    bad_input = True
    print(result)


def is_one_digit(v):
    if int(v) == float(v) and 10 > v > -10:
        output = True
    else:
        output = False
    return output


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 in ["*", "+", "-"]):
        msg += msg_8
    if msg != "":
        msg = msg_9 + msg
        print(msg)


def store_result():
    global memory
    print("Do you want to store the result? (y / n):")
    s_answer = input()
    while s_answer not in ["y", "n"]:
        print("Do you want to store the result? (y / n):")
        s_answer = input()
    if s_answer == "y":
        if is_one_digit(result):
            msg_index = 10
            while msg_index < 13 and s_answer in ["y", "n"]:
                print(msg_[msg_index])
                s_answer = input()
                if s_answer == "y":
                    msg_index += 1
                elif s_answer == "n":
                    break
            if s_answer == "y":
                memory = result
        else:
            memory = result


memory = 0
result = 0
print("Enter an equation")
_calc = input().split()
check_cal(_calc)
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
