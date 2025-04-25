#Given 2 sorted arrays, return one larger, sorted array that combines the two input arrays

def merge_sorted_arrays(arr1,arr2):
    arr1.extend(arr2)
    arr1.sort()
    return arr1

print(merge_sorted_arrays([0,3,4,31], [4,6,30]))


def merge_sorted_arrays2(a,b):
  if len(a)==0 or len(b)==0:
    return a+b
  mylist=[]
  i=0
  j=0
  while i<len(a) and j<len(b):
    print(f'{a[i]}, {b[j]}')
    if a[i]<=b[j]:
      mylist.append(a[i])
      i+=1

    elif b[j]<a[i]:
      mylist.append(b[j])
      j+=1

  return mylist+a[i:]+b[j:]

print(merge_sorted_arrays2([0,3,4,20,21], [1,2,3,4,5]))
