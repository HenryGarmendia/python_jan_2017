#ASSIGNMENT: ODD / EVEN

'''
Create a function that counts from 1 to 2000. As it loops through each number, 
have your program generate the number and specify whether it's an odd or even number.
'''

#Your program output should look like below:
'''
Number is 1.  This is an odd number.
Number is 2.  This is an even number.
Number is 3.  This is an odd number.
...
Number is 2000.  This is an even number.
'''

def oddEven():
	for eoNum in range(1, 2001):
		if eoNum %2 == 0:
			print 'Number is {}. This is an even Number'.format(eoNum)
		else:
			print 'Number is {}. This is an odd Number'.format(eoNum)

oddEven()
