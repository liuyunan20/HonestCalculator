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
        else:
            bad_input = False
