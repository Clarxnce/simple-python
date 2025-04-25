
def reverse_string(str):
    reverse = []
    for i in range(len(str)-1,-1,-1):
        reverse.append(str[i])
    return ''.join(reverse)

print(reverse_string('hello'))

def reverse_string_recursive(str):
    if str == "":
        return ""
    else:
        return reverse_string_recursive(str[1:]) + str[0]

