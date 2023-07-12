class Node:
	def __init__(self):
		self.value = None
		self.next = None



class LinkedList:

	def __init__(self):
		self.head = Node()
	

	def add(self, value):
		if self.head.value is None:
			self.head.value = value
			
			return
		#print(self.head.value)


		temp = Node()
		temp.value = value

		#1var
		#current_node = self.head
		#while current_node.next is not None:
		#	current_node = current_node.next
		#current_node.next = temp
		
		#2var
		temp.next = self.head
		self.head = temp

		##3 var
		#temp.next = temp

		#print(temp)

	def leng(self):
		c_node = self.head
		cnt = 0
		while c_node.next:
			
			c_node = c_node.next
			cnt += 1
		else:			
			print("Длина - ", cnt)
		#return cnt


	# Удаляем первый элеммент
	def delete(self):
	
		self.head = self.head.next


	# Получаем значения ячеек
	def get_info(self):
		c_node = self.head
		while c_node.next:
			print(c_node.value, end = " ")
			c_node = c_node.next
		else:
			print(c_node.value)
			print("Over")



pp = LinkedList()
pp.add(907)
#pp.leng()
pp.add(8)
#pp.leng()
#pp.add(7)
##pp.leng()
#pp.add(68)
##pp.leng()
#pp.add(5)
##pp.leng()
#pp.add(444)
pp.add(34)
#pp.add(2)
#pp.add(4599)
##______________________________________________________


pp.get_info()
pp.leng()

pp.delete()

pp.get_info()
pp.leng()