class Hamming:

	def encode(self, data):
		r_size = self.calculateR(data)
		for i in range (0, r_size):
			offset = pow(2,i)
			data = data[:len(data)-offset+1] + '0' + data[len(data)-offset+1:]
		for i in range (0, r_size):
			offset = pow(2,i)
			jump = False
			sum = 0
			first = True
			for j in range(len(data)-offset, -1, -1):
				if not jump and not first:
					sum += int(data[j])
				if(j%offset==0):
					jump = not jump
				if first:
					first = False
			if(sum%2==1):
				data = data[:len(data)-offset] + '1' + data[len(data)-offset+1:]
		return data

	def decode(self, data):
		r = []
		for i in range(0, self.calculateR(data)):
			offset = pow(2,i)
			jump = False
			sum = 0
			for j in range(len(data)-offset,-1,-1):
				if not jump:
					sum += int(data[j])
				if (j%offset==0):
					jump = not jump
			r.append(sum%2)
		return (''.join(str(e) for e in [x for x in r[::-1]]))

	def calculateR(self, data):
		r = 0
		while (pow(2,r) < len(data)+r+1):
			r += 1
		return r

	def correct(self, data, pos):
		bit = abs(int(data[len(data)-pos]) -1)
		return data[:len(data)-pos] + str(bit) + data[len(data)-pos+1:]
