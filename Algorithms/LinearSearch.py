class LinearSearch:

    def search(self, arr, key):
        for i in range(len(arr)):
            if arr[i] == key:
                return i
        return -1


n = int(input("Enter array size: "))

print("Enter array elements:")
arr = list(map(int, input().split()))

print("Array:", arr)

key = int(input("Enter an element to search: "))

obj = LinearSearch()

res = obj.search(arr, key)

if res != -1:
    print("Element found at the index:", res)
else:
    print("Element not found")

# Idea: Check each element one by one from left to right.
# Linear search checks elements sequentially and works on both sorted and unsorted arrays.
# space complexity is O(1)
# Time complexity is O(n)
