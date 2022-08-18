def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(500, 8, 9))

# greater than or equal sign >=
# is equal or not sign ==
# not equal sign !=
# less than or equal to sign <=
