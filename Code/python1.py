
	
def one(input1, input2):
	length1=len(input1)
	length2=len(input2)
	if length1>length2:
		return input1
	if length1<length2:
		return input2
	else:
		return input1+ ' '+input2




def two(input):
	sentence=input.split()
	b='bert'
	if b in sentence:
		sentence=sentence.remove('bert')
		print(sentence)

	print(sentence)

	return ""




def three(arg1):
	if arg1%3==0 and arg1%5==0:
		return 'fizzbuzz'
	elif arg1%3==0:
		return 'fizz'
	elif arg1%5==0:
		return 'buzz'
	else:
		return "null"

def four(arg1):
	numbers=arg1.split()
	map_numbers=map(int, numbers)
	integers=list(map_numbers)
	summ=0
	sum_list=[]
	for i in integers:
		summ[i]=summ+integers[i]%10
		integers[i]=integers[i]//10
		sum_list.append(summ[i])
	return max(sum_list)
	
	
def five(input):
	sentence=(input.split())
	print (sentence)
	return []

	

def six(input):
	if 'cie' in input:
		return False
	elif 'cei' in input:
		return True
	elif 'ei' in input:
		return False
	elif 'ie' in input:
		return True
	else:
		return True



def seven(input):
	counter=0
	vowels=['a', 'e', 'i', 'o', 'u']
	for i in input.lower():
		if i in vowels:
			counter+=1
		else:
			pass
	return counter

def eight(input):
	previous_numbers=list(range(1, input+1))
	prod=1
	for i in previous_numbers:
		prod=prod*i
	return prod
	print (previous_numbers)
		

def nine(inputString, char):
	return -1

	
 
def ten(string, int, char):
	return False
