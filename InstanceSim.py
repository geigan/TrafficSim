class Lane(object):
	def __init__(self):
		print("Lane created.")
		self.carqueue=[]

	def MoveCar(self,LightStatus):
	#cars follow one set of rules with a green light
	#starting at the head of the queue and moving towards the tail, for each
            
                for x,item in reversed(list(enumerate(self.carqueue))):  #iterate through the queue in descending order,
                    if self.carqueue[x][1] > 20:
                            self.carqueue[x][1]+=1
                            self.carqueue[x][0]+=1
                            if self.carqueue[x]==[25,26]:
                                    self.carqueue.pop(0) #once a car's head and tail is clear of the intersection, pop it
                    elif ( self.PositionIsClear((self.carqueue[x][1])+1) ) and (self.carqueue[x][1] < 20):
                            self.carqueue[x][1]+=1
                            self.carqueue[x][0]+=1

                            '''x
                            xxx'''
                    elif self.PositionIsClear((self.carqueue[x][1])+1) and LightStatus=="green":
                            self.carqueue[x][1]+=1
                            self.carqueue[x][0]+=1

                    else:
                            pass
		self.spawn()#at the end of the movement turn, roll the dice and see if a car spawns
        def spawn(self):
		if self.PositionIsClear(2) and self.PositionIsClear(1):
			self.carqueue.append([1,2])

        def PositionIsClear(self,location):
            for x in self.carqueue:
                    for y in x:
                            if y==location:
                                    return False
            return True
            #protip: to shift left all lines by one tab, highlight those lines and hit Shift+TabError






	def __init__(self):
		print("Lane created.")
		self.carqueue=[]
	def spawn(self):
		if PositionIsClear(2) and PositionIsClear(1):
			self.carqueue.append([1,2])

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
					self.carqueue[x][1]+=1
					self.carqueue[x][0]+=1
					if self.carqueue[x][1] > 25:
						self.carqueue.pop() #once a car's head is clear of the intersection, pop it
				elif PositionIsClear((self.carqueue[x][1])+1):
					self.carqueue[x][1]+=1
					self.carqueue[x][0]+=1
				print("Car:",x)
			spawn(self.carqueue)
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
			elif((x)%((self.GreenTime+6)*2) < green_time+12):
				self.MoveCar("green")
			else:
				self.MoveCar("yellow")



class Light(object):
	def __init__(self,Direction,GreenTime,StartsGreen):
		self.Direction = Direction  #there are 2 light objects, one for the horizontal lanes and one for the vertical lanes
		self.GreenTime = GreenTime
		self.YellowTime = 6 
		self.RedTime=GreenTime+6
		self.StartsGreen=StartsGreen
		self.Top=Lane()
		self.Bottom=Lane()
	def DetermineState(self,x): #to be defined/implemented. Determines current light based on starting cycle when cycle is advanced.
		if(self.StartsGreen):
			if((x)%((self.GreenTime+6)*2) < self.GreenTime):
				print(self.Direction,"is green")
				self.Top.Iterate(x,self.StartsGreen,self.GreenTime)
				self.Bottom.Iterate(x,self.StartsGreen,self.GreenTime)
			elif((x)%((self.GreenTime+6)*2) < self.GreenTime+self.YellowTime):
				print(self.Direction,"is yellow")
				self.Top.Iterate(x,self.StartsGreen,self.GreenTime)
				self.Bottom.Iterate(x,self.StartsGreen,self.GreenTime)
			else:
				print(self.Direction,"is red")
				self.Top.Iterate(x,self.StartsGreen,self.GreenTime)
				self.Bottom.Iterate(x,self.StartsGreen,self.GreenTime)
		else:
			if((x)%((self.GreenTime+6)*2) < self.RedTime):
				print(self.Direction,"is red")
				self.Top.Iterate(x,self.StartsGreen,self.GreenTime)
				self.Bottom.Iterate(x,self.StartsGreen,self.GreenTime)
			elif((x)%((self.GreenTime+6)*2) < self.RedTime+self.YellowTime):
				print(self.Direction,"is green")
				self.Top.Iterate(x,self.StartsGreen,self.GreenTime)
				self.Bottom.Iterate(x,self.StartsGreen,self.GreenTime)
			else:
				print(EW.Direction,"is yellow")
				self.Top.Iterate(x,self.StartsGreen,self.GreenTime)
				self.Bottom.Iterate(x,self.StartsGreen,self.GreenTime)
class Instance(object):

	def __init__(self, GreenTime, TotalCycles):#start a simulation by inputting the green light time and the total duration
		self.GreenTime = GreenTime
		self.TotalCycles = TotalCycles #The time duration gives us the number of cycles.  Since no change can occur on a fraction of a cycle,
                                      #the time duration must be an integer
     
		#variables for outputting simulation stats when finished
		self.AverageWaitTime=0
		self.TotalWaitTime=0
		self.TotalCars=0
		self.LongestLaneLine=0
	
		NS=Light("vertical",self.GreenTime,True)
		EW=Light("horizontal",self.GreenTime,False)
		print("green:",NS.GreenTime)
		print("yellow:",NS.YellowTime)
		print("red:",NS.RedTime)
	#def Clock(z):
		for x in range(self.TotalCycles):
			print("Cycle:",x+1)
			NS.DetermineState(x)
			EW.DetermineState(x)
		print("Cars in north lane after", self.TotalCycles,"cycles:",len(NS.Top.carqueue))
		print("Cars in south lane after", self.TotalCycles,"cycles:",len(NS.Bottom.carqueue))
		print("Cars in east lane after", self.TotalCycles,"cycles:",len(EW.Top.carqueue))
		print("Cars in west lane after", self.TotalCycles,"cycles:",len(EW.Bottom.carqueue))
   #def AdvanceCycle():#to be defined/implemented, advances cycle and triggers the changes to the current state of the lights and lanes.
   #def GetCurrentCycle(): #to be defined/implemented, getter for supplying current cycle to other functions
def main():
	Highway=Instance(6,10)
main()
