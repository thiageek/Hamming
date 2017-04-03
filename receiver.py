from hamming import Hamming

data = raw_input('Type the message received: ')
h = Hamming()
result = h.decode(data)
msg = 'Result: ' + result + '\n'
if(int(result, 2) != 0):
	msg += 'There\'s an error on position ' + str(int(result, 2)) + '.\n'
	correct = h.correct(data, int(result, 2))
	msg += 'The correct data should be ' + correct + '.'
else:
	msg += 'The data received is correct.'
print msg
