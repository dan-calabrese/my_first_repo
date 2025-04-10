name = input("Please enter your name: ")
print("Hello,", name)

i = True
while i is True:
    try:
        num = int(input("Enter a number: "))
        print(num)
        double = num * 2
        print(double)
        i = False
    except:
        print("You didn't enter a number. Try again")

with open("movies.txt") as file:
    for line in file:
        line = line.strip()
        print(line)

with open("heights.txt") as file:
    for line in file:
        info = line.strip().split()
        #would print info: ['Thomas', 'Jones', '70']
        print(info)
        info[2] = int(info[2])
        #would print info: ['Thomas', 'Jones', 70]
        print(info)
    
file_name = input("Please enter file name: ")
with open(file_name) as file:
    count = 1 # could also use enumerate instead of a counter
    for line in file:
        line = line.strip()
        print(str(count) + ".", line)
        count += 1

