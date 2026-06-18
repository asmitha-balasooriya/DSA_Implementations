n=20 #size of array as specified in the assignment 
dataArray=[None]*n
for i in range(0,n):
    dataArray[i]=int(input(f"Enter element {i+1}: "))#reading in 20 user input values

print("Array to be sorted :",dataArray)
print("")
print("Sorting process showing output of each scan")
print("")


for i in range (n):#for n number of times, the outer loop itereates
    for j in range (n-1,0,-1):#inner loop iterates from the last element in the array to the first one 
        if dataArray[j] < dataArray[j-1]:#checking if the right element is less than the left element
            #swapping if condition met
            temp = dataArray[j]
            dataArray[j]=dataArray[j-1]
            dataArray[j-1] = temp
    print(dataArray)
print("")
print("Sorted Array :",dataArray)
