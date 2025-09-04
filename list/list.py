# use for list

numbers = [1,2,3,4,5]
print(numbers)
# get single value from lit
# print(numbers[3])

print("after append of list")
numbers.append(10)
print(numbers)
print("after insert of list")

numbers.insert(1,15)
print(numbers)

print("add multiple item of list use extend")
numbers.extend([50,40,60])
print(numbers)

print("for remove we will use del by index")
del numbers[0]
print(numbers)
print("for remove we remove method by value")
numbers.remove(60)
print(numbers)
print("for remove we will use pop ")
numbers.pop()
print(numbers)
print("now we will use position 1 by pop")
numbers.pop(1)
print(numbers)
print("slice of list")
print(numbers[1:4])
print(numbers[:3])
print(numbers[::4])
print(numbers[::-1])
print("after loop")
for value in numbers :
    print(value)
print("after sort")
numbers.sort()
print(numbers);
print("Finally we will use clear for remove all item from list")
# numbers.clear()
print(numbers)