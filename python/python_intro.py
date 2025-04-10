import time

print("Hello World!")

# this is a comment
'''
Run, by selecting the code and pressing the play button or by pressing Shift + Enter.
Time to run the code!
'''

x=100
x="hello"
x=[1,2,3]
print(x)

x = 100
y = 10
result = x//y
print(result)
print(int(x/y))

min_value = min(1,2,3)
print(min_value)
raised = pow(2,3)
print(raised)
raised = 2**3
print(raised)

# when creating variables, use all lowercase letters and separate words with underscores

x = -1
y = 0
if x < 0:
    print("x is negative")
    y += 1
elif x > 0:
    print("x is positive")
else:
    print("x is zero")

start = 10
end = 100

if x > start and x < end:
    print("x is within range")

if x < start or x > end:
    print("x is not in range")

count = 0
while count < 5: 
    print(count)
    count += 1

for i in range(5):
    print(i, end=" ")
print()

for i in range(1,5):
    print(i, end=" ")
print()

for i in range(1,15,2):
    print(i, end=" ")
print()

lst=[2,4,6,8]
for i in range(len(lst)):
    print(i,lst[i])

for val in lst:
    print(val, end=" ")
print()

# unrelated to the above code, but here is a way to print the index and value of a list

for i,val in enumerate(lst):
    print(i,val)

for i in range(0,20,3):
    print(i, end=" ")
print()

for i in range(20):
    if i % 3 == 0:
        print(i, end=" ")
print()

counter = 1
sum = 0
while counter <= 50:
    if counter % 2 == 0:
        sum += counter
    counter+=1
print(sum)

counter = 0
sum = 0
while counter <= 50:
    sum += counter
    counter += 2
print(sum)

lst = [5,8,2,15,10,3,7]
for val in lst:
    if val > 5:
        print(val, end=" ")
print()

lst = [1,2,3,4,5]
lst2 = []
lst2.append(lst[0])
for i in range(1,len(lst)):
    lst2.append(lst[i]+lst2[i-1])
print(lst2)

def hello_world():
    print("Hello World!")
hello_world()

def hello(name):
    print("Hello " + name)
hello("Bob")

def hello2(name = "Bob"):
    print("Hello " + name)
hello2()
hello2("Jane")

def happy_new_year():
    counter = 5
    while counter > 0:
        print(counter)
        counter -= 1
        time.sleep(1)
    print("Happy New Year!")

def swap(lst):
    tmp = lst[0]
    lst[0] = lst[-1]
    lst[-1] = tmp
    print(lst)

swap([1,2,3,4,5])

hello = "hello"
for c in hello:
    print(c)

course = "Platform Computing"
plat = course[0:8]
print(plat)

course = "Platform Computing"
plat = course[:8]
computing = course[9:]
print(plat)
print(computing)

happy_new_year()