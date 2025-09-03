# use function

# def addtwonumber() :
#     print("Summation two numbers ", 10 + 20)
#
# addtwonumber()

# default function

# def sum(num1, num2=5) :
#     return f" Sum two numbers {num1 + num2}"
#
# resutl1 = sum(4,4)
# resutl2 = sum(10)
# print(resutl1,resutl2)

# # parameterize function
# def name(name) :
#     return f" hello how are you { name }"
#
# result = name("omar faruk")
# print(result)

# keywords argument function

# def get_net_price (price, tax=3, discount=0.5) :
#     discount_price = price * (1 - discount)
#     net_price = discount_price * (1 + tax)
#     return net_price


# result_price = get_net_price(5)
# print(result_price)

# result_price2 = get_net_price(price = 5,discount=4)
# print(result_price2)

# recursive function

# def count_down(start) :
#     print(start)
#     next = start - 1
#     if next > 0 :
#         count_down(start - 1)

# count_down(5)

# # use for
# def sum_hundred(n) :
#     total = 0
#     for index in range(n+1) :
#         total += index
    
#     print(total)

# sum_hundred(100)

# # recursive
# def sum_recursive(n) :
    
#     if n > 0 :
#       return  n + sum_recursive(n-1)
#     return 0

# result =sum_recursive(100)

# print(result)

# # use ternary operator call recursive
# def ternary_recursive_sum(n) :
#     return n + ternary_recursive_sum(n-1) if n > 0 else 0
        

# res = ternary_recursive_sum(100)
# print(res)

# lambda function

add = lambda a, b : a+b
print(add(10,5))