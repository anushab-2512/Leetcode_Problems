class BubbleSort:
    def sort(self,arr):
        n=len(arr)
        for i in range(n-1):
            for j in range(n-1-i):
                if arr[j]>arr[j+1]:
                    arr[j],arr[j+1]=arr[j+1],arr[j]
        return arr
        
# Array length
n=int(input("Enter an Array size: "))
print("Enter an Array elements")
# creating an array and taking array elements
arr=list(map(int,input().split()))
print("Array before sorting",arr)

# object creation
obj=BubbleSort()
# calling method by using object reference 
result=obj.sort(arr)
print("Array after sorting",result)



# Bubble Sort compares adjacent elements and swaps them if they are in the wrong order.
# Time complexity : O(n²)
# Space complexity: O(1)
