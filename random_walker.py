import random

class Random_walker() :

	#assign id and status(dead=0) to each random walker
	def assign_id(self,a):
		self.id = a
		self.status = 0

	#return the current position of the random walker
	def current_position(self):
		return self.position

	#return the current status(dead or alive) of the random walker
	def current_status(self):
		return self.status

	#change status of the random walker
	def change_status(self):
		if(self.status==0):
			self.status = 1
		else:
			self.status = 0

class Random_walker_history(Random_walker):

	#initialize 
	def initialize(self,size):
		self.hist_size = size
		self.hist_status = []
		self.visit_status = []

	#assign history status i.e. add the node visited to the random walker history
	def assign_hist_status(self,v):
		if v in self.hist_status:
			self.visit_status.append(1)
		else:
			self.visit_status.append(0)
		self.hist_status.append(v)

		if(len(self.hist_status)>self.hist_size):
			self.hist_status.pop(0)
			self.visit_status.pop(0)

	#check whether a node is present in history or not
	def current_hist_status(self,v):
		if v in self.hist_status:
			return 1
		else:
			return 0

	#return visit status for the given node
	def current_visit_status(self,v):
		index = self.hist_status.index(v)
		return self.visit_status[index]

	#find the next position of the random walker
	def next_position(self,G,v):
		#find the neighbours of the current node
		self.neighbors = G.neighbors(v)
		#select a random node from the neighbours
		self.next_v = random.choice(self.neighbors)

		#loop while we get an unvisited node(out of last 20 visits) or just one node remains
		while(self.current_hist_status(self.next_v)==1):

			if(len(self.neighbors)>1):
				self.neighbors.remove(self.next_v)
				self.next_v = random.choice(self.neighbors)
			else:
				self.next_v = self.neighbors[0]
				break

		#set current position of random walker to this new node
		Random_walker.position = self.next_v

	#get the node at the ith position of history
	def get_hist(self,i):
		if len(self.hist_status)>i:
			return self.hist_status[i]
		else:
	 		return [-1,-1,-1]

	#get visit status of the random walker
	def get_visit(self):
		return self.visit_status

	
