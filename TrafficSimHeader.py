class Instance(object):

    def __init__(self, GreenTime, TotalCycles):  #start a simulation by inputting the green light time and the total duration
      self.GreenTime = GreenTime
      self.TotalCycles = TotalCycles #The time duration gives us the number of cycles.  Since no change can occur on a fraction of a cycle,
                                      #the time duration must be an integer
     
     #variables for outputting simulation stats when finished
      self.AverageWaitTime=0
      self.TotalWaitTime=0
      self.TotalCars=0
      self.LongestLaneLine=0

   def AdvanceCycle(): #to be defined/implemented, advances cycle and triggers the changes to the current state of the lights and lanes.
   def GetCurrentCycle(): #to be defined/implemented, getter for supplying current cycle to other functions
   
   
class Car(object):

  def __init__(self, ID, FrontOrBack, Position):
    self.ID = ID #which car the object belongs to.
    self.FrontOrBack = FrontOrBack #either the front or back of a car
    self.Position = Position #current position in lane
  def DetermineMovement(): #to be defined/implemented, determines movement based on position in lane
  			#and current light after light state is determined
    
class Light(object):
  def __init__(self,Direction,GreenTime)
   self.Direction = Direction  #there are 2 light objects, one for the horizontal lanes and one for the vertical lanes
   self.GreenTime = GreenTime
   self.YellowTime = 6 
   self.RedTime=GreenTime+6
  
  def DetermineState(): #to be defined/implemented. Determines current light based on starting cycle when cycle is advanced.

class Lane(object):

    def __init__(self, direction):
        self.direction=direction  #there are two light objects, but four lane objects (N,S,E,W). Each light's directionc corresponds to two lanes.
        self.length=24 #length of lane before light, plus intersection
        self.spaces=[] #list storing Car objects
        
    def SpawnNewCar(): #to be defined, after a lane is finished with movement the lane checks whether it can spawn a car
    			#and does so if able
    def MoveCar():  #to be defined. Change the values of a Car object in spaces[] after a car determines movement

            
