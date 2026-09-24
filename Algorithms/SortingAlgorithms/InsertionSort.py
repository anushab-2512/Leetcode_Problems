class InsertionSort():
    def sort(self,arr):
        n=len(arr)
        for i in range(1,n):
            item=arr[i]
            j=i-1
            while j>=0 and arr[j]>item:
                arr[j+1]=arr[j]
                j-=1
            arr[j+1]=item
        
        return arr
        
# Array length from user
n=int(input("Enter an array length"))
print("Enter an array elements")
# creating an array by taking input from user in one line 
arr=list(map(int,input().split()))
print("Array before sorting",arr)

# objection creation for the class
obj=InsertionSort()
# calling method by using that object refernce
result=obj.sort(arr)
print("Array after sorting",result)

# Insertion Sort takes one element at a time and inserts it into its correct position in the already-sorted portion.
# Time complexity: O(n²) worst case
# Best case: O(n)
# Space complexity: O(1)
