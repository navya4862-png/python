# 1. Add an Element to a List
# Problem: Write a function to add an element to a list. Explanation: Use append() to add the element to the end. Input: [1, 2, 3], add 4 Output: [1, 2, 3, 4]
def add_element(lst, element):
    lst.append(element)
    return lst

print(add_element([1, 2, 3], 4))

# 2. Remove an Element from a List
# Problem: Write a function to remove a specific element from a list. Explanation: Use remove() or pop() if index is known. Input: [1, 2, 3, 4], remove 3 Output: [1, 2, 4]
def remove_element(lst, element):
    lst.remove(element)
    return lst

print(remove_element([1, 2, 3, 4], 3))

# 3. Find Maximum in List
# Problem: Find the maximum value in a list. Explanation: Use max() or iterate manually. Input: [4, 7, 1, 9] Output: 9
def find_max(lst):
    return max(lst)

print(find_max([4, 7, 1, 9]))

# 4. Find Minimum in List
# Problem: Find the minimum value in a list. Explanation: Use min() or iterate manually. Input: [4, 7, 1, 9] Output: 1
def find_min(lst):
    return min(lst)

print(find_min([4, 7, 1, 9]))

# 5. Sum of All Elements in List
# Problem: Write a function to find the sum of all list elements. Explanation: Use sum() or loop to add all items. Input: [1, 2, 3] Output: 6
def list_sum(lst):
    return sum(lst)

print(list_sum([1, 2, 3]))

# 6. Count Occurrence of an Element
# Problem: Count how many times a value appears in a list. Explanation: Use count() method. Input: [1, 2, 2, 3, 2], value 2 Output: 3
def count_element(lst, element):
    return lst.count(element)

print(count_element([1, 2, 2, 3, 2], 2))

# 7. Reverse a List
# Problem: Write a function to reverse the order of list elements. Explanation: Use slicing or reverse() method. Input: [1, 2, 3] Output: [3, 2, 1]
def reverse_list(lst):
    return lst[::-1]

print(reverse_list([1, 2, 3]))

# 8. Sort a List
# Problem: Write a function to sort a list in ascending order. Explanation: Use sort() or sorted(). Input: [4, 1, 3, 2] Output: [1, 2, 3, 4]
def sort_list(lst):
    return sorted(lst)

print(sort_list([4, 1, 3, 2]))

# 9. Remove Duplicates from a List
# Problem: Eliminate duplicate values. Explanation: Use set() or manual loop. Input: [1, 2, 2, 3] Output: [1, 2, 3]
def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3]))

# 10. Merge Two Lists
# Problem: Merge two lists into one. Explanation: Use + operator or extend(). Input: [1, 2], [3, 4] Output: [1, 2, 3, 4]
def merge_lists(lst1, lst2):
    return lst1 + lst2

print(merge_lists([1, 2], [3, 4]))

# 11. Find Common Elements in Two Lists
# Problem: Return common elements between two lists. Explanation: Use set() and & or loops. Input: [1, 2, 3], [2, 3, 4] Output: [2, 3]
def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(common_elements([1, 2, 3], [2, 3, 4]))

# 12. Print Even Numbers in a List
# Problem: Print only even numbers from a list. Explanation: Use modulo condition in a loop. Input: [1, 2, 3, 4] Output: [2, 4]
def even_numbers(lst):
    result = []

    for x in lst:
        if x % 2 == 0:
            result.append(x)

    return result

print(even_numbers([1, 2, 3, 4]))

# 13. Print Odd Numbers in a List
# Problem: Print only odd numbers from a list. Input: [1, 2, 3, 4] Output: [1, 3]
def odd_numbers(lst):
    result = []

    for x in lst:
        if x % 2 != 0:
            result.append(x)

    return result

print(odd_numbers([1, 2, 3, 4]))

# 14. Check if List is Palindrome
# Problem: Check if the list reads the same forwards and backwards. Input: [1, 2, 1] Output: True
def pal(list):
    return list==list[::-1]
print(pal([1,2,1]))

# 15. Count Positive, Negative, Zero
# Problem: Count the number of positive, negative and zero values in a list. Input: [0, -1, 2, -3, 4] Output: Positive: 2, Negative: 2, Zero: 1
def count(arr):
    positive=0
    negative=0
    zero=0
    for num in arr:
        if num>0:
            positive+=1
        elif num<0:
            negative+=1
        else:
            zero+=1
    return positive,negative,zero

result=count([0, -1, 2, -3, 4])
print("Positive :",result[0])
print("Negative :",result[1])
print("Zero :",result[2])

# 16. Find Second Largest Number in List
# Problem: Find the second highest value. Input: [1, 3, 4, 5, 0] Output: 4
def second_highest(arr):
    max_num=float("-inf")
    second_max_num=float("-inf")
    for num in arr:
        if num > max_num:
            second_max_num=max_num
            max_num=num
        elif num > second_max_num and num!=max_num:
            second_max_num=num
    return  second_max_num
print(second_highest([1, 3, 4, 5, 0] ))


# 17. Find Second Smallest Number in List
# Problem: Find the second lowest value. Input: [5, 1, 4, 2, 3] Output: 2
def second_smallest(arr):
    min_num=float("inf")
    second_min_num=float("inf")
    for num in arr:
        if num < min_num:
            second_min_num=min_num
            min_num=num
        elif num < second_min_num and num!=min_num:
            second_min_num=num
    return  second_min_num
print(second_smallest([5, 1, 4, 2, 3]))

#or
def large(l):
    unique=list(set(l))
    unique.sort()
    return unique[-2]
print(large([1,2,2,3,3,3,6,6,6,7,]))

# 18. Copy List to Another List
# Problem: Copy the contents of one list to another. Explanation: Use slicing or copy(). Input: [1, 2, 3] Output: [1, 2, 3]
def copy(arr):
    result=arr.copy()
    return result
print(copy([1,2,3]))

# 19. Print All Prime Numbers in List
# Problem: Print all prime numbers from a list. Input: [1, 2, 3, 4, 5] Output: [2, 3, 5]
def prime(arr):
    result=[]
    
    for i in range(0,len(arr)):
        num=arr[i]
        count=0
        for j in range(1,num+1):
          if num%j==0:
            count+=1
        if count==2:
            result.append(num)
    return result

print(prime([1,2,3,4,5]))

# 20. Replace All Zeroes with a Given Number
# Problem: Replace every zero with a specific value (e.g., -1). Input: [0, 2, 0, 4], replace with -1 Output: [-1, 2, -1, 4]
def replace(arr):
    result = []
    for num in arr:
        if num == 0:
            result.append(-1)
        else:
            result.append(num)
    return result
print(replace([0,2,0,4]))

# 21. Check if All Elements Are Same
# Problem: Check whether all elements in the list are identical. Input: [5, 5, 5, 5] Output: True
def same(arr):
    n=len(arr)
    left=0
    right=n-1
    while left<right:
        if arr[left]!=arr[right]:
            return False
        left+=1
        right-=1
    return True
print(same([5,5,5,5]))

# 22. Find Frequency of All Elements
# Problem: Return a dictionary with the frequency of each element. Input: [1, 2, 2, 3, 1] Output: {1: 2, 2: 2, 3: 1}
def frequency(arr):
    result = {}
    for num in arr:
        if num in result:
            result[num] += 1
        else:
            result[num] = 1
    return result
print(frequency([1, 2, 2, 3, 1]))


# 23. Flatten a Nested List
# Problem: Convert a nested list into a single list. Input: [[1, 2], [3, 4]] Output: [1, 2, 3, 4]
def flat_list(arr):
    result=[]
    for i in range(0,len(arr)):
       inner_list=arr[i]
       for num in inner_list:
          result.append(num)
    return result
print(flat_list([[1, 2], [3, 4]] ))

# 24. Split a List into Even and Odd Lists
# Problem: Separate even and odd numbers into different lists. Input: [1, 2, 3, 4, 5] Output: Even: [2, 4], Odd: [1, 3, 5]
def spilt_list(arr):
    even=[]
    odd=[]
    for num in arr:
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
    return even,odd
result=spilt_list([1,2,3,4,5])
print("Even :",result[0])
print("Odd :",result[1])

# 25. Find Pair of Elements with Given Sum
# Problem: Find all pairs in the list whose sum equals a given value. Input: [1, 2, 3, 4], sum = 5 Output: [(1, 4), (2, 3)]

def pair_sum(arr, target):
    result = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                result.append((arr[i], arr[j]))
    return result
print(pair_sum([1, 2, 3, 4], 5))

# 26. Remove All Odd Numbers
# Problem: Remove all odd numbers from the list. Input: [1, 2, 3, 4, 5] Output: [2, 4]
def remove_odd(arr):
    result=[]
    for num in arr:
        if num%2==0:
            result.append(num)
    return result
print(remove_odd([1,2,3,4,5]))

# 27. Remove All Even Numbers
# Problem: Remove all even numbers from the list. Input: [1, 2, 3, 4, 5] Output: [1, 3, 5]

def remove_even(arr):
    result=[]
    for num in arr:
        if num%2!=0:
            result.append(num)
    return result
print(remove_even([1,2,3,4,5]))

# 28. Multiply All Elements by a Number
# Problem: Multiply every element in the list by a fixed number. Input: [1, 2, 3], multiply by 2 Output: [2, 4, 6]

def mul_two(arr):
    result=[]
    for num in arr:
            result.append(num*2)
    return result
print(mul_two([1,2,3]))

# 29. Find Difference Between Max and Min
# Problem: Return the difference between the largest and smallest element. Input: [4, 2, 7, 1] Output: 6

def diff(arr):
    a=max(arr)-min(arr)
    return a
print(diff([4,2,7,1]))

# 30. Check if a List is Empty
# Problem: Write a function that returns True if the list is empty, else False. Input: [] Output: True

def empty_list(arr):
    if arr==[]:
        return True
    return False
print(empty_list([]))

# 31. Insert Element at Specific Index
# Problem: Insert a value at a specific position. Input: [1, 2, 4], insert 3 at index 2 Output: [1, 2, 3, 4]
def add_element(arr, index, num):
    arr.insert(index, num)
    return arr

print(add_element([1, 2, 4], 2, 3))

#32. Remove All Instances of a Value
# Problem: Remove all occurrences of a specific value. Input: [1, 2, 2, 3], remove 2 Output: [1, 3]
def remove(arr,nums):
    result=[]
    for num in arr:
        if num!=nums:
            result.append(num)
    return result
print(remove([1,2,2,3],2))

# 33. Get Index of an Element
# Problem: Return the index of a given value. Input: [10, 20, 30], find index of 20 Output: 1
def ind(arr,value):
    for i in range(0,len(arr)):
        if arr[i]==value:
            return i
print(ind([10,20,30],20))

# 34. Square All Elements in a List
# Problem: Return a list with each element squared. Input: [1, 2, 3] Output: [1, 4, 9]

def square(arr):
    result=[]
    for num in arr:
        result.append(num*2)
    return result
print(square([1,2,3]))

# 35. Filter Out Negative Numbers
# Problem: Remove all negative values from the list. Input: [-1, 2, -3, 4] Output: [2, 4]

def positive(arr):
    result=[]
    for num in arr:
        if num>0:
          result.append(num)
    return result
print(positive([-1, 2, -3, 4]))

# 36. Get Elements Greater Than a Value
# Problem: Return elements greater than a specified number. Input: [1, 5, 8, 3], greater than 4 Output: [5, 8]
def greater(arr,value):
    result=[]
    for num in arr:
        if num>value:
          result.append(num)
    return result
print(greater([1, 5, 8, 3],4))

# 37. Find Duplicates in List
# Problem: Return a list of duplicated values. Input: [1, 2, 2, 3, 3, 4] Output: [2, 3]
def dup(arr):
    unique=[]
    result=[]
    for num in arr:
        if num not in unique:
          unique.append(num)
        else:
            result.append(num)
    return result
print(dup([1, 2,2,3,3,4]))

#38. Rotate List Elements Right
#Problem: Rotate list by k positions to the right. Input: [1, 2, 3, 4], k = 2 Output: [3, 4, 1, 2]
def rotation(arr,k):
    n=len(arr)
    k=k%n
    index=n-k
    r=arr[index:]
    l=arr[:index]
    arr[:]=r+l
    return arr
print(rotation([1,2,3,4],5))

# 39. Check If List Contains a Value
# Problem: Return True if list contains a specific value. Input: [1, 2, 3], check 2 Output: True
def contain(arr,value):
    for num in arr:
        if num==value:
            return True
print(contain([1, 2,3],2))

# 40. Chunk List into Smaller Lists
# Problem: Break a list into chunks of given size. Input: [1, 2, 3, 4, 5, 6], chunk size 2 Output: [[1, 2], [3, 4], [5, 6]]
def chunk_list(arr,size):
    result=[]
    for i in range(0,len(arr),size):
        result.append(arr[i:i+size])
    return result
print(chunk_list([1,2,3,4,5,6],2))




































