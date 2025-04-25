# Google question
# Given an array = [2,5,1,2,3,5,1,2,4]:
#It should return 2

#Given an array = [2,1,1,2,3,5,1,2,4]:
#It should return 1

#Given an array = [2,3,4,5]:
#It should return undefined


def first_recurring_character(arr):
    #make a note of each value in input array. Compare new value with each previous value
    # if new value and previous value are equal, return new value
    previously_seen = []
    for i in arr:
        if i in previously_seen:
            return i
        previously_seen.append(i)
    return None

print(first_recurring_character([2,5,1,2,3,5,1,2,4]))
print(first_recurring_character([2,1,1,2,3,5,1,2,4]))
print(first_recurring_character([2,3,4,5]))


def first_recurring_character2(arr):
    previously_seen = dict()
    for i in arr:
        if i in previously_seen:
            return i
        else:
            previously_seen[i] = True
    return None


print(first_recurring_character2([2,5,1,2,3,5,1,2,4]))
print(first_recurring_character2([2,1,1,2,3,5,1,2,4]))
print(first_recurring_character2([2,3,4,5]))