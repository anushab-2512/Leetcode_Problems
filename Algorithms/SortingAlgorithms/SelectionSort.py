class SelectionSort:
    def sort(self,arr):
        n=len(arr)
        for i in range(n-1):
            minindex=arr[i]
            pos=i
            for j in range(i+1,n):
                if arr[j]<minindex:
                    minindex=arr[j]
                    pos=j 
            arr[i],arr[pos]=arr[pos],arr[i]
        return arr

# array length
n=int(input("Eneter an array size"))
print("Enter arrray elements")
# creating array 
arr=list(map(int,input().split()))
print("Array before sorting: ",arr)

# object creation
obj=SelectionSort()
# calling method using object refernce
result=obj.sort(arr)
print("Array after sorting: ",result)


# Selection Sort finds the smallest element from the unsorted part and puts it at the correct position.
# Time complexity : O(n2)
# Space complexity: O(1)
