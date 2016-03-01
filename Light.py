import Lane

class Light(object):
	def __init__(self,Direction,GreenTime,StartsGreen):
		self.Direction = Direction  #there are 2 light objects, one for the horizontal lanes and one for the vertical lanes
		self.GreenTime = GreenTime
		self.YellowTime = 6 
		self.RedTime=GreenTime+6
		self.StartsGreen=StartsGreen
		self.Top=Lane.Lane(20)
		self.Bottom=Lane.Lane(20)
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