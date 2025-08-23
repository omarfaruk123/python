# There is no need to use semeicolon for ending any statement like other language

# get user input
age = int(input("Enter your age : "))

while(int(age) < 10) :
    print("Your age is ", age)
    age = age + 1  # So Python officially doesn’t support ++ or --

# string literal
s = 'This is a string'
print(s)
s = "Another string using double quotes"
print(s)
s = ''' string can span
        multiple line '''
print(s)
s = """ Sting can span triple double code
        multiple line  """

print(s)

summary = ''' A Python statement ends with a newline character.
              Python uses spaces and indentation to organize its code structure.
              Identifiers are names that identify variables, functions, modules, classes, etc..
              Comments describe why the code works. They are ignored by the Python interpreter.
              Use the single quote, double-quotes, triple-quotes, or triple double-quotes to denote a string literal. '''

print(summary)

