# Python3 program to find maximum
# in arr[] of size n 
arr = [10, 8, 45]
n = 3

def largest(arr,n):
  
    # Initialize maximum element
    max = arr[0]
  
    # Traverse array elements from second
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

print ("Largest in given array is",largest(arr,n))