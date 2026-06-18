import time
import random

def Obs1_BubbleSort(dataArray,n):
    comparisons=0 
    maxIndex=n-1 #initializing the maximum index each scan will go through

    startTime=time.time() #record current time
    for i in range (n-1): #outer loop, iterating for n-1 times
        for j in range (maxIndex):#inner loop iterating until the maxIndex 
            comparisons=comparisons+1 #incrementing everytime a comparison is about to happen
            if dataArray[j] > dataArray[j+1]:#comparing the current array element with the next element 
                #swapping if the left element is greater than right element
                temp = dataArray[j]
                dataArray[j]=dataArray[j+1]
                dataArray[j+1] = temp
    
        maxIndex=maxIndex-1 #decremented after each scan as the highest element will be already sorted
    endTime = time.time() #record end time
    timeTaken=(endTime-startTime)*1000 #calculate time gap and convert to miliseconds

    return comparisons,timeTaken

        


def bubbleSort(dataArray,n):
    comparisons=0
    startTime=time.time()#record current time(start time)
    for i in range (n):#outer loop, iterating for n times
        for j in range (n-1):#inner loop, iterating for n-1 times
            comparisons=comparisons+1#incrementing everytime a comparison is about to happen
            if dataArray[j] > dataArray[j+1]:#comparing the current array element with the next element 
                #swapping if the left element is greater than right element
                temp = dataArray[j]
                dataArray[j]=dataArray[j+1]
                dataArray[j+1] = temp
    endTime = time.time()#record end time
    timeTaken=(endTime-startTime)*1000 #calculate time gap in miliseconds 
    return comparisons,timeTaken

        


def Obs2_BubbleSort(dataArray,n):
    NoMoreSwaps=False #initially, a flag is set to false to monitor the swapping later in the program
    comparisons=0
    startTime=time.time()
    while NoMoreSwaps==False: #Loop continues until no swapping takes place
        NoMoreSwaps=True #set to true here but boolean changes if a swap is taken place below
        for i in range(n-1):
            comparisons=comparisons+1#incrementing whenever a comparison is about to occur
            if dataArray[i] > dataArray[i+1]:#comparing adjacent elements
                #swapping if current element is larger than the next element
                temp = dataArray[i]
                dataArray[i]=dataArray[i+1]
                dataArray[i+1] = temp
                NoMoreSwaps=False # There was a swap, therefore boolean changes
    endTime = time.time()#record end time 
    timeTaken=(endTime-startTime)*1000 #calculate time in ms
    
    return comparisons,timeTaken


def Obs3_BubbleSort(dataArray,n):
    comparisons=0
    NoMoreSwaps=False #initially, a flag is set to false to monitor the swapping later in the program
    
    maxIndex=n-1
    startTime=time.time()
    while NoMoreSwaps==False: #Loop continues until no swapping takes place
        NoMoreSwaps=True #set to true here but boolean changes if a swap is taken place below
        for i in range(maxIndex):
            comparisons=comparisons+1#incrementing whenever a comparison is about to occur
            if dataArray[i] > dataArray[i+1]:
                #swapping
                temp = dataArray[i]
                dataArray[i]=dataArray[i+1]
                dataArray[i+1] = temp
                NoMoreSwaps=False # There was a swap, therefore boolean changes
            
        maxIndex=maxIndex-1 #During one pass, the largest value in the list is pushed to the end of the list.
                            #ThereFore, no need to carry out the sorting until the last element.
                            #observation 1 is included in here
    endTime = time.time()#record end time 
    timeTaken=(endTime-startTime)*1000#calculate total time in ms 
    
    return comparisons,timeTaken
        

def sinkDownSort(dataArray,n):
    comparisons=0 #initializing comparisons variable to zero at start
    startTime=time.time()#record start time
    for i in range (n):#for n number of times, the outer loop itereates
        for j in range (n-1,0,-1):#inner loop iterates from the last element in the array to the first one 
            comparisons=comparisons+1#if a comparison is about to occur, increment the variable
            if dataArray[j] < dataArray[j-1]:#checking if the right element is less than the left element
                #swapping if condition met
                temp = dataArray[j]
                dataArray[j]=dataArray[j-1]
                dataArray[j-1] = temp

    endTime = time.time()#record end time
    timeTaken=(endTime-startTime)*1000 #calculate total time in ms
    
    return comparisons,timeTaken

            
def sinkDownSort_Improved(dataArray,n):
    #adjusting the sink down sort algorithm like the observation 3 of bubble
    
    comparisons=0#initializing comparisons variable to zero at start
    NoMoreSwaps=False #initially, a flag is set to false to monitor the swapping later in the program
    minIndex=0 #minimum index is set. This will be incremented later because in every scan, the smallest will at the start of array
    startTime=time.time()#record start time
    while NoMoreSwaps==False: #Loop continues until no swapping takes place 
        NoMoreSwaps=True
        for i in range(n-1,minIndex,-1):#inner loop iterating from last to specified minIndex element in array
            comparisons=comparisons+1
            if dataArray[i] < dataArray[i-1]:#checking if the right element is less than the left element
                #swapping if condition met
                temp = dataArray[i]
                dataArray[i]=dataArray[i-1]
                dataArray[i-1] = temp
                NoMoreSwaps=False # There was a swap, therefore boolean changes     
        minIndex=minIndex+1 #During one pass, the largest value in the list is pushed to the end of the list.
                            #ThereFore, no need to carry out the sorting until the last element.
    endTime = time.time()#record end time
    timeTaken=(endTime-startTime)*1000 #calculate total time in ms
    
    return comparisons,timeTaken

def biDirectionalBubbleSort(dataArray,n):
    #scannning happens in both direction as in bubbling and sinking.
    #combines both algorithms from bubblsort and sink sort
    
    comparisons=0
    NoMoreSwaps=False
    maxIndex=n-1
    minIndex=0
    startTime=time.time()
    while NoMoreSwaps==False: #Loop continues until no swapping takes place 
        NoMoreSwaps=True
        #left to right scan
        for i in range(maxIndex):
            comparisons=comparisons+1
            if dataArray[i] > dataArray[i+1]:
                temp = dataArray[i]
                dataArray[i]=dataArray[i+1]
                dataArray[i+1] = temp
                NoMoreSwaps=False # There was a swap, therefore boolean changes
        #right to left scan 
        for i in range(n-1,minIndex,-1):
            comparisons=comparisons+1
            if dataArray[i] < dataArray[i-1]:
                temp = dataArray[i]
                dataArray[i]=dataArray[i-1]
                dataArray[i-1] = temp
                NoMoreSwaps=False # There was a swap, therefore boolean changes
        minIndex=minIndex+1 #During one pass, the smallest value in the list is pushed to the start of the list.
        maxIndex=maxIndex-1 #During one pass, the largest value in the list is pushed to the end of the list.
               
    endTime = time.time()
    timeTaken=(endTime-startTime)*1000
    
    return comparisons,timeTaken

def insertionSort(dataArray,n):
    comparisons=0
    startTime=time.time()
    for Pointer in range(n):
        ItemToBeInserted=dataArray[Pointer]
        CurrentItem=Pointer-1
        while (dataArray[CurrentItem]>ItemToBeInserted) and (CurrentItem>-1):
            comparisons=comparisons+1
            dataArray[CurrentItem+1]=dataArray[CurrentItem]
            CurrentItem=CurrentItem-1
        comparisons=comparisons+1 #if while was false, the comparsion still has to be counted because a comparison occured       
        dataArray[CurrentItem+1]=ItemToBeInserted

    endTime = time.time()
    timeTaken=(endTime-startTime)*1000

    return comparisons,timeTaken

def selectionSort(dataArray,n):
    comparisons=0
    startTime=time.time()
    for i in range(n):
        minIndex=i
        for j in range(i+1,n):
            comparisons=comparisons+1
            if dataArray[j]<dataArray[minIndex]:
                minIndex=j
        if minIndex != i:
            temp = dataArray[i]
            dataArray[i] = dataArray[minIndex]
            dataArray[minIndex] = temp
    endTime = time.time()
    timeTaken=(endTime-startTime)*1000
    
    return comparisons,timeTaken
    
def mergeSort(dataArray,n):
    comparisons=0
    startTime=time.time()
    def mergeSortRecursive(dataArray,buffer,minIndex,maxIndex):
        nonlocal comparisons
        if minIndex<maxIndex:
            middleIndex = (minIndex+maxIndex)//2
            mergeSortRecursive(dataArray,buffer,minIndex,middleIndex)
            mergeSortRecursive(dataArray,buffer,middleIndex+1,maxIndex)
            index1=minIndex
            index2=middleIndex+1
            for i in range(minIndex, maxIndex+1):
                
                if index1>middleIndex:
                    buffer[i]=dataArray[index2]
                    index2=index2+1
                elif index2>maxIndex:
                    buffer[i]=dataArray[index1]
                    index1=index1+1
                elif dataArray[index1]<dataArray[index2]:
                    buffer[i]=dataArray[index1]
                    index1=index1+1
                    comparisons=comparisons+1
                else:
                    buffer[i]=dataArray[index2]
                    index2=index2+1
                    comparisons=comparisons+1

            for i in range(minIndex,maxIndex+1):
                dataArray[i]=buffer[i]


    buffer = [None]*(n)
    mergeSortRecursive(dataArray, buffer, 0, n-1)
    endTime = time.time()
    timeTaken=(endTime-startTime)*1000
    
    return comparisons,timeTaken

def quickSort(dataArray, n):
    comparisons=0
    startTime=time.time()
    def quickSortRecursive(dataArray, leftIndex, rightIndex):
        nonlocal comparisons
        if leftIndex < rightIndex:
            pivot = dataArray[rightIndex]
            p = leftIndex - 1  # Initialize p to track the smaller element's index

            # Partition
            for i in range(leftIndex, rightIndex):
                comparisons=comparisons+1
                if dataArray[i] <= pivot:
                    p += 1
                    # Swapping
                    dataArray[p], dataArray[i] = dataArray[i], dataArray[p]

            # Swap the pivot element to its correct sorted position
            dataArray[p + 1], dataArray[rightIndex] = dataArray[rightIndex], dataArray[p + 1]

            # Recursively sort the left and right subarrays
            quickSortRecursive(dataArray, leftIndex, p)  # Left side of the pivot
            quickSortRecursive(dataArray, p + 2, rightIndex)  # Right side of the pivot


    quickSortRecursive(dataArray, 0, n - 1)
    endTime = time.time()
    timeTaken=(endTime-startTime)*1000
    
    return comparisons,timeTaken

def heapSort(dataArray,n):
    comparisons=0
    startTime=time.time()
    def heapRecursive(dataArray,n,i):
        nonlocal comparisons
        root=i
        leftIndex=2*i+1
        rightIndex=2*i+2

        if leftIndex<n:
            comparisons+=1
            if dataArray[root]<dataArray[leftIndex]:
                root=leftIndex
            
        if rightIndex<n:
            comparisons+=1
            if dataArray[root]<dataArray[rightIndex]:
                root=rightIndex
            
        if root!=i:
            temp=dataArray[i]
            dataArray[i]=dataArray[root]
            dataArray[root]=temp
            heapRecursive(dataArray,n,root)
        
    for i in range(n//2-1,-1,-1):
        heapRecursive(dataArray,n,i)

    for i in range(n-1,0,-1):
        temp=dataArray[i]
        dataArray[i]=dataArray[0]
        dataArray[0]=temp
        heapRecursive(dataArray,i,0)

    endTime = time.time()
    timeTaken=(endTime-startTime)*1000
    
    return comparisons,timeTaken
        
        
def experimental_study():
    ##-----DESCRIPTION----
    ##
    ##In this experimental study, I have chosen 12 runs for each 'n' value and each sorting algorithm
    ##In the process of these 12 runs, I am consecutively adding the # of comparisons and run times for the respective spaces in the array
    ##
    ##Example: For n=100, the selection sort will be run 12 times with different randomly generated numbers in an array
    ##         During these 12 runs, the number of comparisons and run times for each run will be be added to the value
    ##         stored in the respective allocated space in the 2D array.
    ##         At the end of the 12 runs, it will have the total of the 12 runs' number of comparisons and run times.
    ##         Then it will be divied by 12 and stored back to obtain the average.



    #2d array to store the comparisons data for each 'n' value 
    comparisons_data=[["Sorting Algorithm","n=100","n=200","n=400","n=800","1000","n=2000"],
            ["Selection",None,None,None,None,None,None],
            ["Insertion",None,None,None,None,None,None],
            ["Merge",None,None,None,None,None,None],
            ["Quick",None,None,None,None,None,None],
            ["Heap",None,None,None,None,None,None],
            ["Bubble Sort",None,None,None,None,None,None],
            ["Obs1-Bubble Sort",None,None,None,None,None,None],
            ["Obs2-Bubble Sort",None,None,None,None,None,None],
            ["Obs3-Bubble Sort",None,None,None,None,None,None],
            ["Sink Down",None,None,None,None,None,None],
            ["Bidirectional",None,None,None,None,None,None]]
    
    #2d array to store the runtime  data for each 'n' value 
    runtime_data=[["Sorting Algorithm","n=100","n=200","n=400","n=800","1000","n=2000"],
            ["Selection",None,None,None,None,None,None],
            ["Insertion",None,None,None,None,None,None],
            ["Merge",None,None,None,None,None,None],
            ["Quick",None,None,None,None,None,None],
            ["Heap",None,None,None,None,None,None],
            ["Bubble Sort",None,None,None,None,None,None],
            ["Obs1-Bubble Sort",None,None,None,None,None,None],
            ["Obs2-Bubble Sort",None,None,None,None,None,None],
            ["Obs3-Bubble Sort",None,None,None,None,None,None],
            ["Sink Down",None,None,None,None,None,None],
            ["Bidirectional",None,None,None,None,None,None]]

    comparisons_data = [[0 if v is None else v for v in row] for row in comparisons_data]#initialzing 0 for none elemensts (comparisons will be integer)
    runtime_data = [[0.0 if v is None else v for v in row] for row in runtime_data]#initialzing 0.0 for none elemensts (run times will be float)

    #storing the n values in an array as well to easy retrieval later 
    n_values=[100,200,400,800,1000,2000]

    #storing the functions in an array so that it will be easy to call it according to index values
    functions = [selectionSort, insertionSort,mergeSort,quickSort,heapSort,bubbleSort,Obs1_BubbleSort,Obs2_BubbleSort,Obs3_BubbleSort,sinkDownSort,biDirectionalBubbleSort]
    
    print("Experimental Study in progress")

    #iterating for 12 runs 
    for k in range(0,12):
        #iterating for the 6 'n' values 
        for i in range(0,6):
            
            numbers_array=[None]*n_values[i] #initialize array
            
            for j in range(0,n_values[i]):
                
                numbers_array[j]=random.randint(-1000,1000) #generate and store random integers

            x=1
            for func in functions:
                temp_comparisons,temp_time=func(numbers_array.copy(),n_values[i]) #calling each function with array
                #adding to the respective elements
                comparisons_data[x][i+1]=comparisons_data[x][i+1]+temp_comparisons 
                runtime_data[x][i+1]=runtime_data[x][i+1]+temp_time
                x+=1

        print("Run ",k+1," over")
                    
            

    #after the 12 runs are over, each element in the array are divided 12 to obtain average 
    for count in range(1,12):
        for count2 in range(1,7):
            comparisons_data[count][count2]=comparisons_data[count][count2]//12
            runtime_data[count][count2]=runtime_data[count][count2]/12

    
    #printing the two arrays at the end in the form of tables
    column_widths = [20, 10, 10, 10,10,10,10]
    row_widths = "| {:<20} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} | {:^10} |"

    #printing the comparisons table 
    def border():
        total_width = sum(column_widths) + len(column_widths) * 3 + 1
        print("+" + "-" * (total_width - 2) + "+")

    print("")
    print("Average Comparisons for n values for 12 runs ")
    print("")
        
    border()
    print(row_widths.format("Sorting Algorithm", "n=100", "n=200", "n=400","n=800","n=1000","n=2000"))
    border()


    for row in comparisons_data[1:]:  
        
        display_row = [
            row[0],  
            row[1], 
            row[2], 
            row[3], 
            row[4], 
            row[5], 
            row[6], 
        ]
        print(row_widths.format(*display_row))
        border()

    #printing the run time table 
    print("")
    print("Average Run Time for n values for 12 runs ")
    print("")
    
    border()
    print(row_widths.format("Sorting Algorithm", "n=100", "n=200", "n=400","n=800","n=1000","n=2000"))
    border()


    for row in runtime_data[1:]:  
        
        display_row = [
            row[0],  
            f"{float(row[1]):.3g}", 
            f"{float(row[2]):.3g}",
            f"{float(row[3]):.3g}",
            f"{float(row[4]):.3g}",
            f"{float(row[5]):.3g}",
            f"{float(row[6]):.3g}",
        ]
        print(row_widths.format(*display_row))
        border()

    print("")


experimental_study()

