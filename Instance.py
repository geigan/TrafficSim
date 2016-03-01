import Light

class Instance(object):

	def __init__(self, GreenTime, TotalCycles):#start a simulation by inputting the green light time and the total duration
		self.GreenTime = GreenTime
		self.TotalCycles = TotalCycles #The time duration gives us the number of cycles.  Since no change can occur on a fraction of a cycle,
                                      #the time duration must be an integer
     
		#variables for outputting simulation stats when finished
		self.TotalWaitTime=0
		self.TotalCars=0
		self.LongestLaneLine=0
	
		self.NS=Light.Light("vertical",self.GreenTime,True)
		self.EW=Light.Light("horizontal",self.GreenTime,False)
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