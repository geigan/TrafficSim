import random

class Lane(object):
	def __init__(self,lanesize):
		#print("Lane created.") #diagnostic line when object is created
		self.carqueue=[]
		self.lanesize=lanesize
		self.spawnP = 100

		self.lanesum = 0 #aggregate total of all lengths for all time stamps
		self.lanemax = 0 #maximum number of cars in a lane
		self.number_of_cars = 0 #total number of cars spawned
		self.total_wait_time = 0 #total time waited by all cars
	'''def MoveCar(self,LightStatus):
	#cars follow one set of rules with a green light
	#starting at the head of the queue and moving towards the tail, for each
            
                for x,item in reversed(list(enumerate(self.carqueue))):  #iterate through the queue in descending order,
                    if self.carqueue[x][1] > 20:
                            self.carqueue[x][1]+=1
                            self.carqueue[x][0]+=1
                            if self.carqueue[x]==[25,26]:
                                    self.carqueue.pop(0) #once a car's head and tail is clear of the intersection, pop it
                    elif ( self.PositionIsClear((self.carqueue[x][1]) ) ) and (self.carqueue[x][1] < 20):
                            self.carqueue[x][1]+=1
                            self.carqueue[x][0]+=1
                    elif self.PositionIsClear((self.carqueue[x][1]) ) and LightStatus=="green":
                            self.carqueue[x][1]+=1
                            self.carqueue[x][0]+=1
                    else:
                            pass
		self.spawn()#at the end of the movement turn, roll the dice and see if a car spawns'''
        #def spawn(self):
		#if self.PositionIsClear(2) and self.PositionIsClear(1):
			#self.carqueue.append([1,2])
			#print("PositionIsClear returned True for both squares")
            #protip: to shift left all lines by one tab, highlight those lines and hit Shift+TabError






	#def __init__(self):
		#print("Lane created.")
		#self.carqueue=[]

	'''randomly generate a car based on a given probability
	IF AND ONLY IF the first two spaces are clear'''
	def spawn(self):
		if self.PositionIsClear(2) and self.PositionIsClear(1):
			if random.randint(1,100) < self.spawnP:
				self.carqueue.append([1,2]) #each time we spawn,
				self.number_of_cars += 1 #add one to the total number of cars

	def PositionIsClear(self,location):
		for x in self.carqueue:
			for y in x:
				if y==location:
					#print("Position is not clear.")
					return False
		#print("All clear!")
		return True

	def MoveCar(self,LightStatus):
		#cars follow one set of rules with a green light
		#starting at the head of the queue and moving towards the tail, for each
		for x,item in list(enumerate(self.carqueue)):  #iterate through the queue in descending order
			if self.carqueue[x][1] > self.lanesize: #once we're past the intersection line, we can keep going
				self.carqueue[x][1]+=1 #...no matter what.  The light will be yellow anyway.
				self.carqueue[x][0]+=1
				#if self.carqueue[x] == [24,25]:
					#pass
					#self.carqueue.pop(x) #once a car's head is clear of the intersection, pop it
			elif self.PositionIsClear((self.carqueue[x][1])+1) and self.carqueue[x][1] < 20:
				self.carqueue[x][1]+=1
				self.carqueue[x][0]+=1
			elif (LightStatus == "green"):
				self.carqueue[x][1]+=1
				self.carqueue[x][0]+=1
			else:#if the space in front is occupied, we cannot move the car
				self.total_wait_time += 1
				pass#so we do nothing and move on to the car behind it
			#print self.PositionIsClear((self.carqueue[x][1])+1)
		'''if the car is clear of the intersection,
		remove it from the queue'''  	
		if [self.lanesize+5,self.lanesize+6] in self.carqueue:
			self.carqueue.pop(0)
		self.spawn()
		#print("Cars in lane:",self.carqueue)
		self.lanesum+=len(self.carqueue)
		
		if len(self.carqueue) > self.lanemax:
			self.lanemax=len(self.carqueue)

	def CarLocations(self):
		print("Cars in lane:",self.carqueue)
	'''Use the same formula Light uses for determining light status to determine what light status to use
	when calling MoveCar.  MoveCar determines movement by light status, Iterate determines movement by green time and where we are
	in the cycle, given whether or not a light starts off green.'''
	def Iterate(self,x,starts_green,green_time):
		if(starts_green):
			if((x)%((green_time+6)*2) < green_time):
				self.MoveCar("green")
			elif((x)%((green_time+6)*2) < green_time+6):
				self.MoveCar("yellow")
			else:
				self.MoveCar("red")
		else:
			if((x)%((green_time+6)*2) < green_time+6):
				self.MoveCar("red")
			elif((x)%((green_time+6)*2) < green_time+12):
				self.MoveCar("green")
			else:
				self.MoveCar("yellow")