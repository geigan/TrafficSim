class Lane(object):

    def __init__(self):
        print("Lane created.")
        self.carqueue=[]
        
    def spawn(self):
        if PositionIsClear(2) and PositionIsClear(1):
            self.carqueue.append[[1,2]]
			
def PositionIsClear(self,location):
		for x in self.carqueue:
			for y in x:
				if y==location:
					return False
			
		return True
    
	def MoveCar(self,LightStatus):
		#cars follow one set of rules with a green light
		#starting at the head of the queue and moving towards the tail, for each
		if LightStatus == "Green":
			for x in reversed(self.carqueue):  #iterate through the queue in descending order, 
										#starting with the frontmost car and ending with the last one
				if self.carqueue[x][1] > 20:
					self.carqueue[x][1]+=1,self.carqueue[x][0]+=1
					if self.carqueue[x][1] > 25:
						self.carqueue.pop() #once a car's head is clear of the intersection, pop it
				elif PositionIsClear((self.carqueue[x][1])+1):
					self.carqueue[x][1]+=1,self.carqueue[x][0]+=1
				print("Car:",x)
			spawn(self.carqueue)
				
	def Iterate(LightStatus):
		MoveCar(LightStatus)
'''class Lane(object):

    def __init__(self):
        print("Lane created.")
        self.carqueue=[]
        
    def spawn(self):
        if PositionIsClear(self.carqueue,2) and PositionIsClear(self.carqueue,1):
            self.carqueue.append[[1,2]]
			
	def PositionIsClear(self,self.carqueue,location):
		for x in self.carqueue:
			for y in x:
				if y==location:
					return False
			
		return True
    
	def MoveCar(self,self.carqueue,LightStatus):
		#cars follow one set of rules with a green light
		#starting at the head of the queue and moving towards the tail, for each
		if LightStatus == "Green":
			for x in reversed(self.carqueue):  #iterate through the queue in descending order, 
										#starting with the frontmost car and ending with the last one
				if self.carqueue[x][1] > 20:
					self.carqueue[x][1]+=1,self.carqueue[x][0]+=1
					if self.carqueue[x][1] > 25:
						self.carqueue.pop() #once a car's head is clear of the intersection, pop it
				elif PositionIsClear(self.carqueue,(self.carqueue[x][1])+1):
					self.carqueue[x][1]+=1,self.carqueue[x][0]+=1
				print("Car:",x)
			spawn(self.carqueue)
				
	def Iterate(LightStatus):
		MoveCar(self.carqueue,LightStatus)'''