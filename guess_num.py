import random

ran_upper = input('Please enter the upper limit of random random number: ')
ran_lower = input('Please enter the lower limit of random random number: ')
ran_lower = int(ran_lower)
ran_upper = int(ran_upper)
correct_anws = random.randint(ran_lower+1, ran_upper-1)
print(correct_anws)
times = 0

while times < 1000 :
	anws = input('Please guess a number: ')
	anws = int(anws)
	if anws > correct_anws and anws < ran_upper :
		print('Higher than anwser')
	elif anws < correct_anws and anws > ran_lower :
		print('lower than anwser')
	elif anws == correct_anws:
		print('correct!')
		print('You guess',times+1,'times.')
		break
	else:
		print('The number is over limit. ')
	times = times +1
