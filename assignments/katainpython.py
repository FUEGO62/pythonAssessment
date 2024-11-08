def getLargest(array):
	
	largest = array[0] 

	for  count  in   range(len(array)):

		if array[count]>largest:

			largest=array[count] 		 
		
		return largest 

	 

def reverseIntArray(array) :

	reversedArray = [0]* len(array)

	for  count  in   range(len(array))  :

			reversedArray[( len(array)-1)-count]=array[count] 

		 
		
	return reversedArray 

	 

def  displayArray(array) :
	
	for  count  in   range(len(array))  :

		print (array[count]+" ") 

		 
		
	 

def checkArray(array,   number) :

	counter = 0 
	
	for  count  in   range(len(array))  :

		if array[count] == number:

			counter+=1 

		 


	if(counter>0):
		return True
	else :
		return False
	 


def   displayEvenArray(array) :
	
	for  count  in   range(len(array))  :

		if((count+1)%2==0):
			print (array[count]+" ")
	
def   displayOddArray(    array) :
	
	for  count  in   range(len(array))  :

		if((count+1)%2!=0):

			print (array[count]+" ")

def   sumArray(array) :

	total = 0 
	
	for  count  in   range(len(array))  :

		total += array[count] 

		 
 
	return total 
	 

def isStringPalindrome( word) :

	counter = 0 

	wordArray = [0]*len(word) 
	
	for count in len(word):

		wordArray[count] =word[count] 

		 
	for count in len(word) :

		if wordArray[len(word)-1-count] == wordArray[count]:
			counter+=1 

		 

	if counter == len(word):
		 return True
	else:
		 return False
		

	 
def reverseCharArray(array) :
	
	reversedArray =[0]* len(array) 

	for  count  in   range(len(array))  :

		reversedArray[( len(array)-1)-count]=array[count] 

		 
		
	return reversedArray 

	 
def fuseArrays( array1,    array2) :

	sum = "" 
	concatenatedList = [0]*(len(array1)+len(array2)) 
	
	for count in range(len(array1)) :

		sum += array1[count] 
		 

	for count in range(len(array2)) :

		sum += array2[count] 
		 

	for count in range(len(concatenatedList)) :

		concatenatedList[count] = sum[count] 
		 


	return concatenatedList 
 
def  fuseAlternateArrays( array1,   array2) :

	sum1 = "" 
	sum2 = "" 
	counter = 0 
	concatenatedList = [0] *(len(array1)+len(array2))
	
	for count in range(len(array1)) :

		sum1 += array1[count] 
		 

	for count in range(len(array2)) :

		sum2 += array2[count] 
		 

	for count in range(len(sum1)) :

		concatenatedList[counter] = sum1[count] 

		counter+=2 

		 
	counter = 1 

	for count in range(len(sum2)) :

		
		concatenatedList[counter] = sum2[count] 

		counter +=2 

	return concatenatedList 

def putInList(number) :

	name =  String.valueOf(number) 
	list = [len(name)] 
	for count in range(len(list)) :
		
		list[count] = name[count] 

	return list 

array1 = ["1","2","3"]

array2 = ["a","b","c"]

print(fuseArrays( array1, array2))
	 
