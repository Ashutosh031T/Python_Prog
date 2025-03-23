'''

Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd letter is lowercase. Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.

'''

def myfunc(input_string):
    result = ""
    for index, letter in enumerate(input_string):
        if index % 2 == 0:
            result += letter.upper()
        else:
            result += letter.lower()
    return result

print(myfunc("Hello Ashutosh"))