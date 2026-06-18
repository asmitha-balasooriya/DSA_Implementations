import time
import random
import sys

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

    return comparisons,timeTaken,dataArray

        


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
    
    return comparisons,timeTaken,dataArray

        


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
    
    return comparisons,timeTaken,dataArray


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
    
    return comparisons,timeTaken,dataArray
        

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
    
    return comparisons,timeTaken,dataArray

            
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
    
    return comparisons,timeTaken,dataArray

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
    
    return comparisons,timeTaken,dataArray

def insertionSort(dataArray,n):
    comparisons=0
    startTime=time.time()
    for Pointer in range(n):
        ItemToBeInserted=dataArray[Pointer] #item that is currently being inserted into the sorted sub array
        CurrentItem=Pointer-1
        while (dataArray[CurrentItem]>ItemToBeInserted) and (CurrentItem>-1):
            comparisons=comparisons+1
            dataArray[CurrentItem+1]=dataArray[CurrentItem]
            CurrentItem=CurrentItem-1
        comparisons=comparisons+1 #if while was false, the comparsion still has to be counted because a comparison occured       
        dataArray[CurrentItem+1]=ItemToBeInserted #placing the item to its proper position

    endTime = time.time()
    timeTaken=(endTime-startTime)*1000
    
    return comparisons,timeTaken,dataArray

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
    
    return comparisons,timeTaken,dataArray
    
def mergeSort(dataArray,n):
    comparisons=0 #counter to count the comparisons
    startTime=time.time()
    def mergeSortRecursive(dataArray,buffer,minIndex,maxIndex):
        nonlocal comparisons #comparisons should be able to be amened inside the program
        if minIndex<maxIndex: #checking if the array has more than 1 element 
            middleIndex = (minIndex+maxIndex)//2 #finding the middle point 
            mergeSortRecursive(dataArray,buffer,minIndex,middleIndex)
            mergeSortRecursive(dataArray,buffer,middleIndex+1,maxIndex)
            index1=minIndex #start index for left half 
            index2=middleIndex+1 #strat index for right half 
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


    buffer = [None]*(n)#creating a buffer of similar size to the array to be sorted 
    mergeSortRecursive(dataArray, buffer, 0, n-1)
    endTime = time.time()
    timeTaken=(endTime-startTime)*1000
    
    return comparisons,timeTaken,dataArray

def quickSort(dataArray, n):
    comparisons=0
    startTime=time.time()
    def quickSortRecursive(dataArray, leftIndex, rightIndex):
        nonlocal comparisons
        if leftIndex < rightIndex:
            pivot = dataArray[rightIndex]  # Correct: Choose the pivot as the rightmost element
            p = leftIndex - 1  # Initialize p to track the smaller element's index

            # Loop through the array to partition elements
            for i in range(leftIndex, rightIndex):
                comparisons=comparisons+1
                if dataArray[i] <= pivot:
                    p += 1
                    # Swap dataArray[p] with dataArray[i]
                    dataArray[p], dataArray[i] = dataArray[i], dataArray[p]

            # Swap the pivot element to its correct sorted position
            dataArray[p + 1], dataArray[rightIndex] = dataArray[rightIndex], dataArray[p + 1]

            # Recursively sort the left and right subarrays
            quickSortRecursive(dataArray, leftIndex, p)  # Left side of the pivot
            quickSortRecursive(dataArray, p + 2, rightIndex)  # Right side of the pivot

    # Start the quicksort process
    quickSortRecursive(dataArray, 0, n - 1)
    endTime = time.time()
    timeTaken=(endTime-startTime)*1000
    
    return comparisons,timeTaken,dataArray

def heapSort(dataArray,n):
    comparisons=0
    startTime=time.time()
    def heapRecursive(dataArray,n,i):
        nonlocal comparisons
        root=i #the current root node is taken as i 
        leftIndex=2*i+1
        rightIndex=2*i+2

        #checking if the left child is greater than the root
        if leftIndex<n:
            comparisons+=1
            if dataArray[root]<dataArray[leftIndex]:
                root=leftIndex
                
        #checking if the right child is greater than the root
        if rightIndex<n:
            comparisons+=1
            if dataArray[root]<dataArray[rightIndex]:
                root=rightIndex
            
        if root!=i:
            #if the root is changed, a swap will happen 
            temp=dataArray[i]
            dataArray[i]=dataArray[root]
            dataArray[root]=temp
            heapRecursive(dataArray,n,root)

    #building the max heap 
    for i in range(n//2-1,-1,-1):
        heapRecursive(dataArray,n,i)

    
    #extracting elements from the heap one by one at a time 
    for i in range(n-1,0,-1):
        temp=dataArray[i]
        dataArray[i]=dataArray[0]
        dataArray[0]=temp
        heapRecursive(dataArray,i,0)

    endTime = time.time()
    timeTaken=(endTime-startTime)*1000
    
    return comparisons,timeTaken,dataArray

def main():
    #printing the main menu
    print("")
    print("  Menu")
    print("--------------------")
    print("1. Test an individual sorting algorithm")
    print("2. Test multiple sorting algorithms")
    print("3. Exit")
    print("")
    choice=int(input("Enter choice : "))#prompting user
    print("")

    #execution if user input choice was 1
    if(choice==1):
        #print sub menu
        print("1. Test selection sort algorithm")
        print("2. Test insertion sort algorithm")
        print("3. Test merge sort algorithm")
        print("4. Test quick sort algorithm")
        print("5. Test heap sort algorithm")
        print("6. Test bubble sort algorithm")
        print("7. Test Obs1-bubble sort algorithm")
        print("8. Test Obs2-bubble sort algorithm")
        print("9. Test Obs3-bubble sort algorithm")
        print("10. Test Sink-down sort algorithm")
        print("11. Test Bidirectional Bubble sort algorithm")
        print("")
        choice=int(input("Enter choice : "))
        print("")

        #prompting the user to choose and enter the size of the array
        n= int(input("Enter number of elements in the array : "))
        #validation handling. If user entered any negative number or zero
        while n<1:
           print("Integers below 1 is not allowed. Please enter a positive integer")
           n= int(input("Enter number of elements in the array : "))

        #initializing the array   
        dataArray=[None]*n
        for i in range(0,n):#iterating through the whole array in the loop
            num=random.randint(-1000,1000)#creating random numbers and storing them in the array
            dataArray[i]=num
        print("")
        print("Unsorted Array with random generated values : ",dataArray)#printing the randomly generated array for user reference

        #calling the necessary sorting algorithm function according to what user selected
        if(choice==1):
            numOfComparisons,time,sortedArray=selectionSort(dataArray.copy(),n)#sending a copy so that the original array would not be amended
        elif(choice==2):
            numOfComparisons,time,sortedArray=insertionSort(dataArray.copy(),n)
        elif(choice==3):
            numOfComparisons,time,sortedArray=mergeSort(dataArray.copy(),n)
        elif(choice==4):
            numOfComparisons,time,sortedArray=quickSort(dataArray.copy(),n)
        elif(choice==5):
            numOfComparisons,time,sortedArray=heapSort(dataArray.copy(),n)
        elif(choice==6):
            numOfComparisons,time,sortedArray=bubbleSort(dataArray.copy(),n)
        elif(choice==7):
            numOfComparisons,time,sortedArray=Obs1_BubbleSort(dataArray.copy(),n)
        elif(choice==8):
            numOfComparisons,time,sortedArray=Obs2_BubbleSort(dataArray.copy(),n)
        elif(choice==9):
            numOfComparisons,time,sortedArray=Obs3_BubbleSort(dataArray.copy(),n)
        elif(choice==10):
            numOfComparisons,time,sortedArray=sinkDownSort_Improved(dataArray.copy(),n)
        elif(choice==11):
            numOfComparisons,time,sortedArray=biDirectionalBubbleSort(dataArray.copy(),n)
        print("")
        print("Sorted Array : ",sortedArray)
        print("")
        #printing the number of comparisons and time taken
        print("The sorting algorithm you selected had {} comparisons which took {:.3g} miliseconds".format(numOfComparisons, time))
        print("")
        main()


    #execution if user input choice was 2
    elif(choice==2):
        #prompting the user to choose and enter the size of the array
        n= int(input("Enter number of elements in the array : "))
        #validation handling. If user entered any negative number or zero
        while n<1:
           print("Integers below 1 is not allowed. Please enter a positive integer")
           n= int(input("Enter number of elements in the array : "))
           
        dataArray=[None]*n
        for i in range(0,n):
            num=random.randint(-1000,1000)#random number generation
            dataArray[i]=num #storing in the array

        #initializing a 2D array to store the data and later print it as a table 

        table = [["Sorting Algorithm Name","Array Size","Num of Comparisons","Run time/ms"],
                 ["Selection Sort     ", n,None,None],
                 ["Insertion Sort     ", n,None,None],
                 ["Merge Sort         ", n,None,None],
                 ["Quick Sort         ", n,None,None],
                 ["Heap Sort          ", n,None,None],
                 ["Bubble Sort        ", n,None,None],
                 ["Obs1-Bubble Sort   ", n,None,None],
                 ["Obs2-Bubble Sort   ", n,None,None],
                 ["Obs3-Bubble Sort   ", n,None,None],
                 ["Sink Down Sort     ", n,None,None],
                 ["Bidirectional Sort ", n,None,None]]

        table[7][2],table[7][3],sortedArray=Obs1_BubbleSort(dataArray.copy(),n)#sending a copy so that the original array would not be amended

        table[6][2],table[6][3],sortedArray=bubbleSort(dataArray.copy(),n)

        table[9][2],table[9][3],sortedArray=Obs3_BubbleSort(dataArray.copy(),n)

        table[8][2],table[8][3],sortedArray=Obs2_BubbleSort(dataArray.copy(),n)

        table[10][2],table[10][3],sortedArray=sinkDownSort(dataArray.copy(),n)

        table[5][2],table[5][3],sortedArray=heapSort(dataArray.copy(),n)

        table[11][2],table[11][3],sortedArray=biDirectionalBubbleSort(dataArray.copy(),n)

        table[2][2],table[2][3],sortedArray=insertionSort(dataArray.copy(),n)

        table[1][2],table[1][3],sortedArray=selectionSort(dataArray.copy(),n)

        table[3][2],table[3][3],sortedArray=mergeSort(dataArray.copy(),n)

        table[4][2],table[4][3],sortedArray=quickSort(dataArray.copy(),n)

        
        #printing the data in the table format as specified in the assignment 
        column_widths = [25, 10, 20, 11] #coloum widths are set
        row_widths = "| {:<25} | {:^10} | {:^20} | {:^11} |"  #row widths are set with format to print a border

        #to print the border around the tbale 
        def border():
            total_width = sum(column_widths) + len(column_widths) * 3 + 1
            print("+" + "-" * (total_width - 2) + "+")
            
        border()
        print(row_widths.format("Sorting Algorithm Name", "Array Size", "Num of Comparisons", "Run time/ms"))
        border()

    
        for row in table[1:]:  #the header row is skipped as it is printed before
            #formatting every row
            display_row = [
                row[0],  
                row[1],  
                row[2],
                f"{float(row[3]):.3g}" #floating point numbers printed correct to 5 sf
            ]
            print(row_widths.format(*display_row))#printing each row
            border()
                 
        main()#calling the main function inside the main again to keep iterating until user choose to end the program
         
    else:
        print("Program Terminated")
        sys.exit()#if user chooses to end the program, program is exited/terminated 
        

main()

