# Daniel Calabrese

def repeat_start(s):
    """
    Given a string, return a new string where the first two characters 
    are repeated 
    three times. If the string is shorter than two characters, 
    return the string repeated three times.
    repeat_start("hello") returns "hehehe"
    repeat_start("a") returns "aaa"
    """
    if len(s) >= 2:
        return s[:2] * 3 # returns the first two characters of a string three times.
    else:
        return s[:] * 3 # returns the string three times.


def shift_left(lst):
    """
    Given a list, rotate its elements to the left by one position. 
    The first element should become the last.
    shift_left([1, 2, 3, 4]) returns [2, 3, 4, 1]
    shift_left([5]) returns [5]
    """
    temp = lst[0]
    for i in range(1,len(lst)): # runs through the list except for the first index
        lst[i-1] = lst[i] # shifts the values to the previous index
    lst[len(lst)-1] = temp
    return lst
    

def count_digits(s):
    """
    Use a comprehension to count the number of digits in a string.
    *** Important: your code must use comprehensions and should not be more than
    two lines of code including the return statement ***
    count_digits("The year is 2025!") returns 4
    The string function isdigit() returns True if the string is a digit.
    Eg. c='1' c.isdigit() returns True
    """

    return len([s[i] for i in range(len(s)-1) if s[i].isdigit() == True]) # returns the length of a list made up of only the digits in the string

def swap(lst):
    """
    Given a list, find the minimum element in the list and swap it with the first
    element in the list. Return the list.
    swap([5,4,3,2,1]) returns [1, 4, 3, 2, 5]
    """
    stor = 0
    min = lst[0]
    for i in range(0,len(lst)): # searches the list
        if lst[i] < min:
            min = lst[i]
            stor = i # stores the location of the minimum
    temp = lst[0] # stores the first value
    lst[0] = min # overrides first value
    lst[stor] = temp #sets the first value at the former location of the minimum
    return lst

def build_grades_dict():
    '''
    Create a dictionary where the key is a student's name and the value is
    their grade stored as an integer. 
    Read in the file, grades.txt, store the student's first and last name as 
    the key (first and last name should have a space between them) 
    and their grade as the integer value.
    Your output should read:
     {'Alice Brown': 90, 'Bob Smith': 85, 'Charlie Johnson': 78, 
     'Daisy Lee': 92, 'Evelyn Taylor': 88}
    '''
    dict = {}
    with open("grades.txt") as file:
        for line in file:
            info = line.strip().split()
            info[0] = info[0] + " " + info[1] # sets up the names to be 'First Last'
            del info[1] # deletes the place where the last name used to be
            dict[info[0]] = int(info[1]) #builds the dictionary
    return dict
    

# Test Cases
print('repeat_start("hello") expected: hehehe')
print('repeat_start("hello") actual:', repeat_start("hello"))

print('repeat_start("a") expected: aaa')
print('repeat_start("a") actual:', repeat_start("a"))

print('repeat_start("fido") expected: fififi')
print('repeat_start("fido") actual:', repeat_start("fido"))

print('repeat_start("g1") expected: g1g1g1')
print('repeat_start("g1") actual:', repeat_start("g1"))

print('shift_left([1, 2, 3, 4]) expected: [2, 3, 4, 1]')
print('shift_left([1, 2, 3, 4]) actual:', shift_left([1, 2, 3, 4]))

print('shift_left([5]) expected: [5]')
print('shift_left([5]) actual:', shift_left([5]))

print('shift_left([5, 8, 9, 12]) expected: [8, 9, 12, 5]')
print('shift_left([5, 8, 9, 12]) actual:', shift_left([5, 8, 9, 12]))

print('count_digits("The year is 2025!") expected: 4')
print('count_digits("The year is 2025!") actual:', count_digits("The year is 2025!"))

print('count_digits("3 men walked into 2 stores") expected: 2')
print('count_digits("3 men walked into 2 stores") actual:', count_digits("3 men walked into 2 stores"))

print('count_digits("Why have 30 when you can have 100!") expected: 5')
print('count_digits("Why have 30 when you can have 100!") actual:', count_digits("Why have 30 when you can have 100!"))

print('swap([5,4,3,2,1]) expected: [1, 4, 3, 2, 5]')
print('swap([5,4,3,2,1]) actual:',swap([5,4,3,2,1]))

print('swap([6,7,5,4,2]) expected: [2, 7, 5, 4, 6]')
print('swap([6,7,5,4,2]) actual:',swap([6,7,5,4,2]))

print('swap([2,3]) expected: [2, 3]')
print('swap([2,3]) actual:',swap([2,3]))

print(build_grades_dict())
