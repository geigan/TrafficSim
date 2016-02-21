class Light(object):
	def __init__(self,Direction,GreenTime,StartsGreen):
		self.Direction = Direction  #there are 2 light objects, one for the horizontal lanes and one for the vertical lanes
		self.GreenTime = GreenTime
		self.YellowTime = 6 
		self.RedTime=GreenTime+6
		self.StartsGreen=StartsGreen
	def DetermineState(x): #to be defined/implemented. Determines current light based on starting cycle when cycle is advanced.
		if(StartsGreen):
			if((x)%((self.GreenTime+6)*2) < NS.GreenTime):
				print(NS.Direction,"is green")
			elif((x)%((self.GreenTime+6)*2) < NS.GreenTime+NS.YellowTime):
				print(NS.Direction,"is yellow")
			else:
				print(NS.Direction,"is red")
		else:
			if((x)%((self.GreenTime+6)*2) < EW.RedTime):
				print(EW.Direction,"is red")
			elif((x)%((self.GreenTime+6)*2) < EW.RedTime+EW.YellowTime):
				print(EW.Direction,"is green")
			else:
				print(EW.Direction,"is yellow")
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
			
			'''	#if(StartsGreen):
			if((x)%((self.GreenTime+6)*2) < NS.GreenTime):
				print(NS.Direction,"is green")
			elif((x)%((self.GreenTime+6)*2) < NS.GreenTime+NS.YellowTime):
				print(NS.Direction,"is yellow")
			else:
				print(NS.Direction,"is red")
		#else:
			if((x)%((self.GreenTime+6)*2) < EW.RedTime):
				print(EW.Direction,"is red")
			elif((x)%((self.GreenTime+6)*2) < EW.RedTime+EW.YellowTime):
				print(EW.Direction,"is green")
			else:
				print(EW.Direction,"is yellow")'''
			#NS.DetermineState(True,(x+1)%((self.GreenTime+6)*2)  )
			#EW.DetermineState(False,(x+1)%((self.GreenTime+6)*2) )
		
   #def AdvanceCycle():#to be defined/implemented, advances cycle and triggers the changes to the current state of the lights and lanes.
   #def GetCurrentCycle(): #to be defined/implemented, getter for supplying current cycle to other functions

