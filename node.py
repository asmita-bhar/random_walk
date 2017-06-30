import networkx as nx 

class Node :

	#constructor
	def __init__(self,dim):
		self.status = [[],[]]
		self.width = dim[1]
		self.height = dim[2]
		self.node_hist = [[] for i in range(dim[0]*dim[1]*dim[2])]

	#create graph
	def Node_list(self,dim):
		self.G = nx.grid_graph(dim)
		return self.G

	#initialise status for all nodes to be not visited(=0) 
	def init_node_status(self):
		self.status[0] = nx.nodes(self.G)
		for i in self.status[0]: 	
			self.status[1].append(0)

	#change the status of a node from not visited(=0) to visited(=1)
	def change_status(self,vertex):
		index = self.status[0].index(vertex)
		if(self.status[1][index]==0):
			self.status[1][index]=1

	#return the current visit status of a given node
	def current_visit_status(self,vertex):
		index = self.status[0].index(vertex)
		return self.status[1][index]

	#count the total number of nodes covered
	def count_nodes_covered(self):
		return self.status[1].count(1)

	#update the node history for the given node
	def update_node_hist(self,v,k):
		self.index = v[2]+v[1]*self.height+v[0]*self.width*self.height
		if(k not in self.node_hist[self.index]):
			self.node_hist[self.index].append(k)
		return

	#return node history for the given node
	def get_node_hist(self,v):
		#print(self.ind)
		self.index = v[2]+v[1]*self.height+v[0]*self.width*self.height
		l = self.node_hist[self.index]
		return l