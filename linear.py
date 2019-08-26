class Array:
			
	def __init__(self):
		self.arr = [1,2,3,4,5,6,7,8,9,10]
	

	def insert_value(self,K,item):	
		self.arr.append(None)
		
		j = len(self.arr)-1	
		print("old array :",self.arr[:j])
		while j >= K:
			self.arr[j] = self.arr[j-1]
			j-=1
		self.arr[K] = item
		print("New array: ",self.arr)


	def delete(self,pos):
		lent = len(self.arr)-1
		print("old array :",self.arr[:])
		if pos > lent:
			print("index out of range max index is {}".format(lent))
		else:
		# print(lent)
			for i in range(pos,len(self.arr)-1):
				if i < len(self.arr):
					self.arr[i] = self.arr[i+1]
				else:
					print("end")
			print("new array :",self.arr[0:len(self.arr)-1])


	



