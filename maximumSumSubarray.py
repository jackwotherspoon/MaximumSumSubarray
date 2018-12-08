#Divide and Conquer Algorithm for maximum sum subarray problem
#Author: Jack Wotherspoon
#Created: October 20th, 2018
def max_subarray(arr, start, end):
    # base case if there is 1 element in subarray
    if start == end - 1:
        return start, end, arr[start]
    else:
        mid = (start + end) // 2
        left_start, left_end, left_max =max_subarray(arr, start, mid)
        right_start, right_end, right_max =max_subarray(arr, mid, end)
        cross_start, cross_end, cross_max =max_crossing_subarray(arr, start, mid, end)
        if (left_max > right_max and left_max > cross_max):
            return left_start, left_end, left_max
        elif (right_max > left_max and right_max > cross_max):
            return right_start, right_end, right_max
        else:
            return cross_start, cross_end, cross_max


def max_crossing_subarray(arr, start, mid, end):
    # Include elements on left of mid.
    sum_left = -10000
    sum = 0
    cross_start = mid
    for i in range(mid - 1, start - 1, -1):
        sum = sum + arr[i]
        if sum > sum_left:
            sum_left = sum
            cross_start = i
    # Include elements on right of mid
    sum_right = -10000
    sum = 0
    cross_end = mid + 1
    for i in range(mid, end):
        sum = sum + arr[i]
        if sum > sum_right:
            sum_right = sum
            cross_end = i + 1
    return cross_start, cross_end, sum_left + sum_right

arr = [3,4,6,-5,-8,4,4]
n=len(arr)
left=0  #choosing leftbound index
right=n #choosing rightbound index
#make if statement so rightbound can not exceed array size
if(right>n):
    right=n
# if statement so leftbound can not have lower index than possible
if(left<0):
    left=0
start, end, maximum =max_subarray(arr, left, right)
print(arr)
print('The start of the max subarray starts at index', start,'and ends at index', end-1,'with max sum of', maximum,'.')
#for loop to implement part 2 which is getting a second mss that does not overlap with the first
for x in range(start,end):
    arr[x] = -999
print(arr)
start, end, maximum =max_subarray(arr, left, right)
print('The start of the max subarray starts at index', start,'and ends at index', end-1,'with max sum of', maximum,'.')

