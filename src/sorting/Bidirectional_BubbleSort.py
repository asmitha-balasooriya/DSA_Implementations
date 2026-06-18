n=20 #size of array as specified in the assignment 
dataArray=[None]*n
for i in range(0,n):
    dataArray[i]=int(input(f"Enter element {i+1}: "))#reading in 20 user input values

print("Array to be sorted :",dataArray)
print("")
print("Sorting process showing output of each scan")
print("")

#scannning happens in both direction as in bubbling and sinking.
#combines both algorithms from bubblsort and sink sort
    
NoMoreSwaps=False
maxIndex=n-1
minIndex=0

while NoMoreSwaps==False: #Loop continues until no swapping takes place 
    NoMoreSwaps=True
    #left to right scan
    for i in range(maxIndex):
        if dataArray[i] > dataArray[i+1]:
            temp = dataArray[i]
            dataArray[i]=dataArray[i+1]
            dataArray[i+1] = temp
            NoMoreSwaps=False # There was a swap, therefore boolean changes
    #right to left scan 
    for i in range(n-1,minIndex,-1):
        if dataArray[i] < dataArray[i-1]:
            temp = dataArray[i]
            dataArray[i]=dataArray[i-1]
            dataArray[i-1] = temp
            NoMoreSwaps=False # There was a swap, therefore boolean changes
    minIndex=minIndex+1 #During one pass, the smallest value in the list is pushed to the start of the list.
    maxIndex=maxIndex-1 #During one pass, the largest value in the list is pushed to the end of the list.
    
    print(dataArray)

print("")
print("Sorted Array :",dataArray)


