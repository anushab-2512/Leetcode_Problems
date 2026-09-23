class BinarySearch:
    def search(self,arr,key):
        low=0
        high=len(arr)-1
        while low<= high:
            mid=(low+high)//2
            if arr[mid]==key:
                return mid
            elif key>arr[mid]:
                low=mid+1
            else:
                high=mid-1
        return -1

# length of an array from user input
n=int(input("Enter Array size: "))

# array elements 
print("Eneter an array elements ")
arr=list(map(int,input().split()))
print("Array: ",arr)

# element to search from user input
key=int(input("Enter an element to search"))

# creating object for the class binarysearch
obj=BinarySearch()
# calling an menthod 
result=obj.search(arr,key)

if result != -1:
    print("Element is found at the index:", result)
else:
    print("Element not found")

# Binary search only works for sorted list (ascending order)
# we call it has binary search because we always divide the list into two halfs to search an element 
# Time Complexity: O(log n) bcz " Every iteration removes half of the search space."
# Space Complexity: O(1) bcz "it uses only a constant number of variables."
