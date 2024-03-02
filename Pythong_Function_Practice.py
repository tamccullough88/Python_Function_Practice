# Write a Python function called max_num()to find the maximum of three numbers
def max_num(a,b,c):
    return max([a,b,c])
print(max_num(5,7,27))

# Write a Python function called mult_list() to multiply all the numbers in a list
def multi_list(nums):
    if len(nums) == 0:
        return 0
    multi = nums[0]
   
    if len(nums) > 1:
        for i in nums[1:]:
            multi = multi * i
    return multi

print (multi_list([4,5,2]))
   
# Write a Python function called rev_string() to reverse a string
def rev_string(a):
   return a[::-1]
   
print(rev_string("world hello"))

# Write a Python function called num_within() to check whether a number falls in a given range
def num_within(i, a, b) :
    return i in range(a, b+1)


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
def pascal(row):
    for i in range(row):
        print(" "*(row-i), end=' ')
        print(" ".join(str(11**i)))






# print (num_within(3, 2, 4))
# print (num_within(3,1,1))
# print (num_within(10,2,5))
print(pascal(6))