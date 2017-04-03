from hamming import Hamming

data = raw_input('Type the message you to send: ')
h = Hamming()
print 'The message to be sent with '+ str(h.calculateR(data)) + ' redudancy bits is: ' + h.encode(data)
