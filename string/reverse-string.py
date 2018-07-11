"""
Reverse an array without affecting special characters
Given a string, that contains special character together with alphabets (a to z and A to Z), reverse the string in a way that special characters are not affected.

Ex:
Input:   str = "a,b$c"
Output:  str = "c,b$a"
Note that $ and , are not moved anywhere.
Only subsequence "abc" is reversed

Input:   str = "Ab,c,de!$"
Output:  str = "ed,c,bA!$"

"""
str_inp = "a,b$c"

letters_li = []
main_list = []

for mi in str_inp:
    main_list.append(mi)

b = [0 if t.isalpha() else t for t in main_list]
for count, element in enumerate(main_list):
    if str(element).isalpha():
        letters_li.append(str(element))

letters_li = letters_li[::-1]

cnt = 0
for i in range(len(b)):
    if b[i] == 0:
        b[i] = letters_li[cnt]
        cnt += 1
print b

"""
###### Web Solution for the problem ######
# Python program to reverse a
# string with special characters

# Returns true if x is an aplhabatic
# character, false otherwise
def isAlphabet(x):
    return x.isalpha()

def reverse(string):
    LIST = toList(string)

    # Initialize left and right pointers
    r = len(LIST) - 1
    l = 0

    # Traverse LIST from both ends until
    # 'l' and 'r'
    while l < r:

        # Ignore special characters
        if not isAlphabet(LIST[l]):
            l += 1
        elif not isAlphabet(LIST[r]):
            r -= 1

        # Both LIST[l] and LIST[r] are not special
        else:
            LIST[l], LIST[r] = swap(LIST[l],
                                    LIST[r])
            l += 1
            r -= 1

    return toString(LIST)

# Utility functions
def toList(string):
    List = []
    for i in string:
        List.append(i)
    return List

def toString(List):
    return ''.join(List)

def swap(a, b):
    return b, a

# Driver code
string = "a!!!b.c.d,e'f,ghi"
print "Input string: " + string
string = reverse(string)
print "Output string: " + string

# This code is contributed by Bhavya Jain
"""