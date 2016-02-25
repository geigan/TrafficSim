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



class Light(object):
	def __init__(self,Direction,GreenTime,StartsGreen):
		self.Direction = Direction  #there are 2 light objects, one for the horizontal lanes and one for the vertical lanes
		self.GreenTime = GreenTime
		self.YellowTime = 6 
		self.RedTime=GreenTime+6
		self.StartsGreen=StartsGreen
		self.Top=Lane(20)
		self.Bottom=Lane(20)
		self.spawnprobability=100

	def ChangeSpawnProbability(self,SP):
		self.spawnprobability=SP
		self.Top.spawnP = self.spawnprobability
		self.Bottom.spawnP = self.spawnprobability

	def DetermineState(self,x): #to be defined/implemented. Determines current light based on starting cycle when cycle is advanced.
		if(self.StartsGreen):
			if((x)%((self.GreenTime+6)*2) < self.GreenTime):
				'''print(self.Direction,"is green")
				print the light status for diagnostic purposes'''
				self.Top.Iterate(x,self.StartsGreen,self.GreenTime)
				self.Bottom.Iterate(x,self.StartsGreen,self.GreenTime)
			elif((x)%((self.GreenTime+6)*2) < self.GreenTime+self.YellowTime):
				#print(self.Direction,"is yellow")
				self.Top.Iterate(x,self.StartsGreen,self.GreenTime)
				self.Bottom.Iterate(x,self.StartsGreen,self.GreenTime)
			else:
				#print(self.Direction,"is red")
				self.Top.Iterate(x,self.StartsGreen,self.GreenTime)
				self.Bottom.Iterate(x,self.StartsGreen,self.GreenTime)
		else:
			if((x)%((self.GreenTime+6)*2) < self.RedTime):
				#print(self.Direction,"is red")
				self.Top.Iterate(x,self.StartsGreen,self.GreenTime)
				self.Bottom.Iterate(x,self.StartsGreen,self.GreenTime)
			elif((x)%((self.GreenTime+6)*2) < self.RedTime+self.YellowTime):
				#print(self.Direction,"is green")
				self.Top.Iterate(x,self.StartsGreen,self.GreenTime)
				self.Bottom.Iterate(x,self.StartsGreen,self.GreenTime)
			else:
				#print(self.Direction,"is yellow")
				self.Top.Iterate(x,self.StartsGreen,self.GreenTime)
				self.Bottom.Iterate(x,self.StartsGreen,self.GreenTime)
class Instance(object):

	def __init__(self, GreenTime, TotalCycles):#start a simulation by inputting the green light time and the total duration
		self.GreenTime = GreenTime
		self.TotalCycles = TotalCycles #The time duration gives us the number of cycles.  Since no change can occur on a fraction of a cycle,
                                      #the time duration must be an integer
     
		#variables for outputting simulation stats when finished
		self.TotalWaitTime=0
		self.TotalCars=0
		self.LongestLaneLine=0
	
		self.NS=Light("vertical",self.GreenTime,True)
		self.EW=Light("horizontal",self.GreenTime,False)
		print("green:",self.NS.GreenTime)
		print("yellow:",self.NS.YellowTime)
		print("red:",self.NS.RedTime)
	#def Clock(z):
	def GetSpawnChance(self,SpawnChance):
		self.SpawnChance=SpawnChance
		self.NS.ChangeSpawnProbability(self.SpawnChance)
		self.EW.ChangeSpawnProbability(self.SpawnChance)

		#protip: in Sublime, hit Tab for autocomplete

	def AverageWaitTime(self):

		TimeWaited = 0
		TimeWaited += self.NS.Top.total_wait_time
		TimeWaited += self.NS.Bottom.total_wait_time
		TimeWaited += self.EW.Top.total_wait_time
		TimeWaited += self.EW.Bottom.total_wait_time
		#print("Time Waited:",TimeWaited)

		CarTotal = 0
		CarTotal += self.NS.Top.number_of_cars
		CarTotal += self.NS.Bottom.number_of_cars
		CarTotal += self.EW.Top.number_of_cars
		CarTotal += self.EW.Bottom.number_of_cars
		#print("Car Total:",CarTotal)

		x = TimeWaited/CarTotal
		
		print("Average wait time:",str(x) )
		

	def AverageLaneSize(self):
		average_lane_size = 0
		average_lane_size += self.NS.Top.lanesum
		average_lane_size += self.NS.Bottom.lanesum
		average_lane_size += self.EW.Top.lanesum
		average_lane_size += self.EW.Bottom.lanesum

		average_lane_size /= (self.TotalCycles*4)

		#return average_lane_size
		print("Average lane length:",str(average_lane_size) )

	def RunSim(self):
		for x in range(self.TotalCycles):
			#print("Cycle:",x+1)
			self.NS.DetermineState(x)
			self.EW.DetermineState(x)

		#print("Average wait time:",str(self.AverageWaitTime() ) )
		self.AverageWaitTime()

		#print("Average lane length:",str(self.AverageLaneSize() ) )
		self.AverageLaneSize()

		print("Maximum lane length:",str( max([self.NS.Top.lanemax,self.NS.Bottom.lanemax,self.EW.Top.lanemax,self.EW.Bottom.lanemax]) ) ) 
		
		print("Cars in north lane after", self.TotalCycles,"cycles:",len(self.NS.Top.carqueue) )
		self.NS.Top.CarLocations()

		print("Cars in south lane after", self.TotalCycles,"cycles:",len(self.NS.Bottom.carqueue))
		self.NS.Bottom.CarLocations()
	
		print("Cars in east lane after", self.TotalCycles,"cycles:",len(self.EW.Top.carqueue))
		self.EW.Top.CarLocations()
	
		print("Cars in west lane after", self.TotalCycles,"cycles:",len(self.EW.Bottom.carqueue))
		self.EW.Bottom.CarLocations()

		#self.longestlaneline = max([self.NS.Top.carqueue,self.NS.Bottom.carqueue,self.EW.Top.carqueue,self.EW.Bottom.carqueue])
			#protip: with nothing highlighted, Ctrl+C copies the whole ine in Sublime

   #def AdvanceCycle():#to be defined/implemented, advances cycle and triggers the changes to the current state of the lights and lanes.
   #def GetCurrentCycle(): #to be defined/implemented, getter for supplying current cycle to other functions

'''for this tentative prototype, we assume the user
gives positive integers for all input.  
Processing for special cases may be implemented later.'''
def main():
	#while True:
	Cycles=input("Enter the time length:")
	#if Cycles == "q":
		#break
	if Cycles == "":
		Cycles = 20
	else:
		Cycles = int(Cycles)
	GreenTime=input("Enter the duration of the green light:")
	#if GreenTime == "q":
		#break
	if GreenTime == "":
		GreenTime = 20
	else:
		GreenTime = int(GreenTime)
	SpawnChance=input("Enter the percentage spawn chance from 1 to 100:")
	#if SpawnChance == "q":
		#break
	if SpawnChance == "":
		SpawnChance = 100
	else:
		SpawnChance = int(SpawnChance)		
	Highway=Instance(GreenTime,Cycles)
	Highway.GetSpawnChance(SpawnChance)
	Highway.RunSim()
main()
