n=20 #size of array as specified in the assignment 
dataArray=[None]*n
for i in range(0,n):
    dataArray[i]=int(input(f"Enter element {i+1}: "))#reading in 20 user input values

print("Array to be sorted :",dataArray)
print("")
print("Sorting process showing output of each scan")
print("")

#adjusting the sink down sort algorithm like the observation 3 of bubble

NoMoreSwaps=False #initially, a flag is set to false to monitor the swapping later in the program
minIndex=0 #minimum index is set. This will be incremented later because in every scan, the smallest will at the start of array
while NoMoreSwaps==False: #Loop continues until no swapping takes place 
    NoMoreSwaps=True
    for i in range(n-1,minIndex,-1):#inner loop iterating from last to specified minIndex element in array
        if dataArray[i] < dataArray[i-1]:#checking if the right element is less than the left element
            #swapping if condition met
            temp = dataArray[i]
            dataArray[i]=dataArray[i-1]
            dataArray[i-1] = temp
            NoMoreSwaps=False # There was a swap, therefore boolean changes     
    minIndex=minIndex+1 #During one pass, the largest value in the list is pushed to the end of the list.
                        #ThereFore, no need to carry out the sorting until the last element.

    print(dataArray)
print("")
print("Sorted Array :",dataArray)

