class Instance(object):

    def __init__(self, GreenTime, TotalCycles):  #start a simulation by inputting the green light time and the total duration
      self.GreenTime = GreenTime
      self.TotalCycles = TotalCycles #The time duration gives us the number of cycles.  Since no change can occur on a fraction of a cycle,
                                      #the time duration must be an integer
      self.AverageWaitTime=0
      self.TotalWaitTime=0
      self.TotalCars=0
      self.LongestLaneLine=0

   def AdvanceCycle(): #to be defined/implemented
   def GetCurrentCycle(): #to be defined/implemented
   
   
class Car(object):

  def __init__(self, ID, FrontOrBack, Position):
    self.ID = ID
    self.FrontOrBack = FrontOrBack
    self.Position = Position
  def DetermineMovement(): #to be defined/implemented
    
class Light(object):
  def __init__(self,Direction,GreenTime)
   self.Direction = Direction  #there are 2 light objects, one for the horizontal lanes and one for the vertical lanes
   self.GreenTime=GreenTime
   self.YellowTime=6
   self.RedTime=GreenTime+6
   
	def DetermineState() #to be defined/implemented
	
class Lane(object):

    def __init__(self, direction):
        self.direction=direction  #there are two light objects, but four lane objects (N,S,E,W)
        self.length=20
        self.spaces=[] #list storing Car objects
        
    def SpawnNewCar() #to be defined. 
    def MoveCar()  #to be defined.  Change the values of the Car objects in spaces[] when given the AdvanceCyle signal from Instance

            
