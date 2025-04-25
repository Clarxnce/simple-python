import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla']
large = ['nemo' for i in range(100000)]
def find_nemo(array):
    t0 = time.time()
    for i in range(0,len(array)):
        if array[i] == 'nemo':
            print("Found Nemo!!")
    t1 = time.time()
    print(f'The search took {t1-t0} seconds.')
find_nemo(nemo)
find_nemo(everyone)
find_nemo(large)

def random_function():
    pass


def funchallenge(input):
    temp = 10 #O(1)
    temp = temp +50 #O(1)
    for i in range(len(input)): #O(n)
        random_function() #O(n)
        var = True #O(n)
        temp += 1 #O(n)
    return temp #O(1)

funchallenge(nemo)
funchallenge(everyone)
funchallenge(large)

#Total running time of the funchallenge function =
#BIG O - 1 + 1 + 1 + n + n + n + n = (3 + 4n)
#Any constant in the Big-O representation can be replaced by 1, as it doesn't really matter what constant it is.
#Therefore, O(3n + 4) becomes O(n+4)
#Similarly, any constant number added or subtracted to n or multiplied or divided by n can also be safely written as just n
#This is because the constant that operates upon n, doesn't depend on n, i.e., the input size
#Therefore, the funchallenge function can be said to be of O(n) or Linear Time Complexity.