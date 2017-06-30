from node import Node 
from random_walker import Random_walker
from random_walker import Random_walker_history
import random
import matplotlib.pyplot as plt

#function to calculate the rate of proliferation
def rate(t):
	#find proliferation rate
	r = (1+1.0/(t+155-1))**(10*0.5)-1
	#generate a random number between 0 and 1
	ran = random.uniform(0,1)
	#proliferate if generated random number is less than the proliferation rate
	if(ran<r):
		return 1
	else:
		return 0

#function to decide whether a particular random walker should be proliferated or not
def decision_to_proliferate(h,n):
	#set decision to false by default
	decision = False
	#find the number of nodes with visit status = 0
	c = 20 - h.get_visit().count(1)
	#considering threshold to be 0.5
	if(c>=0.5*20):
		#for the entire history of random walker 
		for i in range(20):
			#node at last ith visit 
			v = h.get_hist(i)
			#if the node has been traversed already by a random walker then set decision to false 
			if(len(n.get_node_hist(v))>1):
				decision = False
				break
			else:
				decision = True	
	#print decision
	return decision


def main():

	print("Enter dimensions : ")
	dim = []
	dim.append(input())
	dim.append(input())
	dim.append(input())
	'''print('Enter the no. of walkers : ')
	k = input()'''
	threshold = 0.5
	k = 1000
	n = float(dim[0]*dim[1]*dim[2])

	node = Node(dim)
	G = node.Node_list(dim)
	node.init_node_status()
	#node.init_node_hist(dim)

	#list of random walker objects
	rw = []
	for i in range(k):
		rw.append(Random_walker())

	#list of random walker history objects
	h = []
	for i in range(k):
		h.append(Random_walker_history())

	#initialise 
	for i in range(k):
		h[i].initialize(20)
		rw[i].assign_id(i)

	#setting up the first random walker object
	rw[0].change_status()
	start = random.choice(G.nodes())
	node.change_status(start)
	node.update_node_hist(start,0)	
	h[0].assign_hist_status(start)
	covered = []
	#covered.append(0)
	count = 1  #maintains a count of the number of active random walkers

	#loop for 1000 time steps
	time=2
	for time in range(1001):
		c=0
		#check which of the active random walker objects can be proliferated
		for i in range(count):
			#print rw[i].current_status()
			if(rw[i].current_status()==1 and decision_to_proliferate(h[i],node)==True):
				if(rate(time)==1):
					c=c+1
					
		#finding the number of new random walker objects
		new = c 
		#finding the total number of random walker objects
		count = int(count+new)
		if(count>k):
			count = k
		print count 

		#change the status of the newly proliferated random walkers(from dead to alive)
		for i in range(count):
			if(rw[i].current_status()==0): 
				rw[i].change_status()

		#a list to store which nodes have been visited by which random walker 
		visited = [[],[]] 

		#loop for all active random walker objects
		for j in range(count):
			#finding the next position for each active random walker
			h[j].next_position(G,start)
			next_v = rw[j].current_position()
			#assign history status for the node visited next
			h[j].assign_hist_status(next_v)
			#assign the node to visited[] 
			visited[0].append(next_v)
			visited[1].append(j)
			#set start node to the node visited
			start = next_v

		#change node status and node history for each visited node
		while(len(visited[0])>0):
			v = visited[0].pop(0)
			node.change_status(v)
			node.update_node_hist(v,visited[1].pop(0))

		#add fraction of nodes covered every 100 time steps 
		if(time%100==0):
			covg = node.count_nodes_covered()/n
			covered.append(covg)

	print(covered)

	#plotting coverage vs time 
	x = []
	i=0
	while(i<=1000):
		x.append(i)
		i=i+100

	plt.xlabel('time steps')
	plt.ylabel('fraction of nodes covered')
	plt.plot(x,covered)
	plt.show()

if __name__ == "__main__":
	main()