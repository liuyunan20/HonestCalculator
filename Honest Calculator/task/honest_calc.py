# write your code here
print("Enter an equation")
calc = input().split()
bad_input = True
while bad_input:
    try:
        x = float(calc[0])
        y = float(calc[2])
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
