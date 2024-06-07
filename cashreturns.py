def isFloat(num):
    try:
        float(num)
        return float(num)
    except ValueError:
        return False

cash = isFloat(input("Change owed: "))

while cash < 0 or cash == False:
    cash = isFloat(input("Try again, change owed: "))

change_return = 0

while cash != 0:
    cash = float("%.2f" % cash)
    if cash >= 0.25:
        cash = cash - 0.25
        change_return += 1
                    
    elif cash >= 0.10:
        cash = cash - 0.10
        change_return += 1
                
    elif cash >= 0.05:
        cash = cash - 0.05
        change_return += 1

    elif cash >= 0.01:
        cash = cash - 0.01
        change_return += 1

    else:
        cash = cash - 0.01
        change_return += 1
        break

print(change_return)

