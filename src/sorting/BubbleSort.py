n=20 #size of array as specified in the assignment 
dataArray=[None]*n
for i in range(0,n):
    dataArray[i]=int(input(f"Enter element {i+1}: "))#reading in 20 user input values
    
print("Array to be sorted :",dataArray)
print("")
print("Sorting process showing output of each scan")
print("")
for i in range (n):#outer loop, iterating for n times
    for j in range (n-1):#inner loop, iterating for n-1 times
        if dataArray[j] > dataArray[j+1]:#comparing the current array element with the next element 
            #swapping if the left element is greater than right element
            temp = dataArray[j]
            dataArray[j]=dataArray[j+1]
            dataArray[j+1] = temp
    print(dataArray)
print("")
print("Sorted Array :",dataArray)

    
