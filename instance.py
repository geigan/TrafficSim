import light

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

