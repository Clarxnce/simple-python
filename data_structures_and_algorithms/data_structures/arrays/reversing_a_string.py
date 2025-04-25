#Create a function that reverses a string
#"Hi My name is Clarence" becomes "ecneralC si eman yM iH"

def reverse_string(str):
    return str[::-1]

print(reverse_string('Hi my name is Clarence'))

def reverse_string2(input):
    if not input or len(input) < 2 or type(input) != str:
        return 'something went wrong. fix it'
    reverse = []
    for i in range(len(input)-1,-1,-1):
        reverse.append(input[i])
    return ''.join(reverse)

print(reverse_string2('racecar'))

def reverse_string3(string):
    result = str(string)
    result.split().reverse()
    return ''.join(result)


print(reverse_string3('racecar'))

