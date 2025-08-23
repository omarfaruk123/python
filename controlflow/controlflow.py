# get user input

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

# if ... else
# if num1 > num2 :
#     print("Number is grater than mnumber two")
# else :
#     print("Number one is less then number number two ")


# ternary operator
# resutl = "okk" if num1 > num2 else "fale"
# print(resutl)

# for index in range(num1) :
#     print("Number is = ", index)
#

# while loop
# while num1 > num2 :
#     print("Number is = ", num1)
#     num2 += 1

# break

# for index in range(num1) :
#     if index == 7 :
#         break
#     print("Number is ", index)

# Continue
for index in range(num1) :
    if index % 2 :
        continue
    print("Number is ", index)