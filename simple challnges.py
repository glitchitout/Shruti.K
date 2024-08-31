# 1. Hello World
# Print "Hello World" without using the string literals
print(chr(72)+chr(101)+chr(108)+chr(108)+chr(111)+chr(32)+chr(87)+chr(111)+chr(114)+chr(108)+chr(100))

# 2. Multiplication
# Multiple two numbers without using the mutiplication operator(*)
def multiply(x,y):
    if y == 0:
        return 0
    elif y > 0:
        return x + multiply(x,y-1)
    else:
        return -multiply(x,-y)
result = multiply(69,96)
print(result)

# 3. Maximum 
# Find the maximum of two numbers without using comparison operators
def maximum(a,b):
    return( a + b + abs(a-b))//2
a=7
b=11
result=maximum(a,b)
print(result)

# 4. Length
# Calculate the length of a string without using buit-in length function like len()
def length(s):
    count = 0
    for char in s:
        count += 1
    return count
str="Penny justin"
str_len= length(str)
print(str_len)

# 5. String to Int
# Convert a string to an integer without using buit-in function like int()
def str_to_int(s):
    result=0
    for char in s:
        result = result*10+(ord(char)-ord('0'))
    return result
print(str_to_int("11"))

# What is the output of the following code?
a,b="pq"
b,c="rs"
print(a,b,c)