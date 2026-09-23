class LinearSearch:
    def search(self,arr,key):
        for i in range(len(arr)):
            if arr[i]==key:
                return i
        return -1

# Taking input from user
n=int(input("enter array size:"))
print("Enter array elements:")

# list of elements e.g: [1,2,3,4,5]
arr=list(map(int,input().split()))
print("Array:",arr)

# taking input from the user to search an particular element
key=int(input("Enter an element to search:"))

# Creating object
obj=LinearSearch()

res=obj.search(arr,key)
if res != -1:
    print("Element found at the index:",res)
else:
    print("Element not found")

# Theory about LinearSearch
# idea: Check each element one by one from left to right.
# Time Complexity: O(n)
# "The space complexity of linear search is O(1) because we only use a constant amount of extra space for variables like the index and key. 
# The input array itself is not considered extra space."
# Important: Linear search does not require a sorted array but works on both sorted and unsorted arrays.
