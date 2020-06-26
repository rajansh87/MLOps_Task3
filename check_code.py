programfile = open('/root/task3/program.py','r')	#connecting to the code file
code = programfile.read()				#reading the code file

if 'keras' or 'tensorflow' in code:			#because keras or tensorflow keyword is a must for a deep learning program
	if 'Conv2D' in code:				#beacuse if a code is of CNN conv2D layer is a must
		print('Present')
	else:
		print('Not a CNN')
else:
	print('NOT A NEURAL NETWORK')
