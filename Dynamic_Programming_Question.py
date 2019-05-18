"""
find subsets interview question

"""

# recursion tree

def count_sets(arr,total):  # the count sets will return the total number of subsets that will equal to the total
    return rec(arr,total,arr.length -1 )


def rec(arr,total,i): # recursive function , calling itself recursively , it will return subsets that = total but only that are equal to i (index)
    if total == 0 :
        return 1
    elif total < 0 :
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        return rec(arr,total , i-1)
    else :
        return rec(arr,total - arr[i], i-1) + rec(arr, total, i-1)

print(rec([2,4,6,10],16,3))

"""
Dynamic Programming solution using memoized 
"""

def dp(arr,total,i,mem): # values will be stored in mem as key-value pairs
    key = str (total) + ":" + str(i)   # convert total and i (integers) to strings .then concatenate(link) them with a : between them
    if key in mem: # if key alredy in mem, thats = its alredy calculated, so we return the stored value
        return mem[key]
    if total == 0 :
        return 1
    elif total < 0 :
        return 0
    elif i < 0 :
        return 0
    elif total < arr[i]:
        to_return = dp(arr,total,i-1,mem)               # we store them in (to_return)
    else:
        to_return = (dp(arr,total-arr[i],i-1,mem)+ dp(arr,total,i-1,mem))       # we stored them in to_return
    mem[key]= to_return  # stored them at our dict , key calculated above
    return to_return


def count_sets_dp(arr,total):
    mem = {} # empty dict
    return dp(arr,total,arr.length-1,mem)
print("------------------------------")

"""
time complexity : 
"""