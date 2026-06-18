n=20 #size of array as specified in the assignment 
dataArray=[None]*n
for i in range(0,n):
    dataArray[i]=int(input(f"Enter element {i+1}: "))#reading in 20 user input values

print("Array to be sorted :",dataArray)
print("")
print("Sorting process showing output of each scan")
print("")

NoMoreSwaps=False #initially, a flag is set to false to monitor the swapping later in the program

maxIndex=n-1
while NoMoreSwaps==False: #Loop continues until no swapping takes place
    NoMoreSwaps=True #set to true here but boolean changes if a swap is taken place below
    for i in range(maxIndex):
        if dataArray[i] > dataArray[i+1]:
            #swapping
            temp = dataArray[i]
            dataArray[i]=dataArray[i+1]
            dataArray[i+1] = temp
            NoMoreSwaps=False # There was a swap, therefore boolean changes
        
    maxIndex=maxIndex-1 #During one pass, the largest value in the list is pushed to the end of the list.
                        #ThereFore, no need to carry out the sorting until the last element.
                        #observation 1 is included in here
    print(dataArray)

print("")
print("Sorted Array :",dataArray)

