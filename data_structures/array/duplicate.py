# You will find a duplicate in an array of integers given that the integers are in random order and 
# not necessarily each integer i is 0 <= i <= N where N = length of array

# Solution - use tortoise and hare algorithm. The tortoise pointer moves slower while the hare pointer
# moves faster

# Note: this array will always contain a duplicate number due to the pigeonhole principle. You are trying to fit
# N different numbers in an array of size N - 1 so one number will be repeated

def duplicate(arr):
    tortoise = arr[0]
    hare = arr[0]

    while True:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
        if tortoise == hare:
            break

    tortoise = arr[0]

    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]

    return hare


arr = [3,5,1,2,4,5]
print(duplicate(arr))
