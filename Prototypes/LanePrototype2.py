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

                    #print("Turn:",x)
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


	def Iterate(LightStatus):
	    MoveCar(LightStatus)

North=Lane()
South=Lane()
East=Lane()
West=Lane()
for x in range(6):
	x1= North.MoveCar("green")
	South.MoveCar("green")
	East.MoveCar("red")
	West.MoveCar("red")
	print("N:",North.carqueue)
	print("S:",South.carqueue)
	print("E:",East.carqueue)
	print("W:",West.carqueue)
print("Cars in north lane:",len(North.carqueue))
print("Cars in south lane:",len(South.carqueue))
print("Cars in east lane:",len(East.carqueue))
print("Cars in west lane:",len(West.carqueue))
for x in range(6):
	x1= North.MoveCar("yellow")
	South.MoveCar("yellow")
	East.MoveCar("red")
	West.MoveCar("red")
	print("N:",North.carqueue)
	print("S:",South.carqueue)
	print("E:",East.carqueue)
	print("W:",West.carqueue)
print("Cars in north lane:",len(North.carqueue))
print("Cars in south lane:",len(South.carqueue))
print("Cars in east lane:",len(East.carqueue))
print("Cars in west lane:",len(West.carqueue))
for x in range(6):
	x1= North.MoveCar("red")
	South.MoveCar("red")
	East.MoveCar("green")
	West.MoveCar("green")
	print("N:",North.carqueue)
	print("S:",South.carqueue)
	print("E:",East.carqueue)
	print("W:",West.carqueue)
print("Cars in north lane:",len(North.carqueue))
print("Cars in south lane:",len(South.carqueue))
print("Cars in east lane:",len(East.carqueue))
print("Cars in west lane:",len(West.carqueue))
for x in range(6):
	x1= North.MoveCar("red")
	South.MoveCar("red")
	East.MoveCar("yellow")
	West.MoveCar("yellow")
	print("N:",North.carqueue)
	print("S:",South.carqueue)
	print("E:",East.carqueue)
	print("W:",West.carqueue)
print("Cars in north lane:",len(North.carqueue))
print("Cars in south lane:",len(South.carqueue))
print("Cars in east lane:",len(East.carqueue))
print("Cars in west lane:",len(West.carqueue))
for x in range(6):
	x1= North.MoveCar("green")
	South.MoveCar("green")
	East.MoveCar("red")
	West.MoveCar("red")
	print("N:",North.carqueue)
	print("S:",South.carqueue)
	print("E:",East.carqueue)
	print("W:",West.carqueue)
print("Cars in north lane:",len(North.carqueue))
print("Cars in south lane:",len(South.carqueue))
print("Cars in east lane:",len(East.carqueue))
print("Cars in west lane:",len(West.carqueue))
for x in range(6):
	x1= North.MoveCar("yellow")
	South.MoveCar("yellow")
	East.MoveCar("red")
	West.MoveCar("red")
	print("N:",North.carqueue)
	print("S:",South.carqueue)
	print("E:",East.carqueue)
	print("W:",West.carqueue)
print("Cars in north lane:",len(North.carqueue))
print("Cars in south lane:",len(South.carqueue))
print("Cars in east lane:",len(East.carqueue))
print("Cars in west lane:",len(West.carqueue))
for x in range(6):
	x1= North.MoveCar("red")
	South.MoveCar("red")
	East.MoveCar("green")
	West.MoveCar("green")
	print("N:",North.carqueue)
	print("S:",South.carqueue)
	print("E:",East.carqueue)
	print("W:",West.carqueue)
print("Cars in north lane:",len(North.carqueue))
print("Cars in south lane:",len(South.carqueue))
print("Cars in east lane:",len(East.carqueue))
print("Cars in west lane:",len(West.carqueue))
for x in range(6):
	x1= North.MoveCar("red")
	South.MoveCar("red")
	East.MoveCar("yellow")
	West.MoveCar("yellow")
	print("N:",North.carqueue)
	print("S:",South.carqueue)
	print("E:",East.carqueue)
	print("W:",West.carqueue)
print("Cars in north lane:",len(North.carqueue))
print("Cars in south lane:",len(South.carqueue))
print("Cars in east lane:",len(East.carqueue))
print("Cars in west lane:",len(West.carqueue))
'''class Lane(object)for x in range(6):
	x1= North.MoveCar("green")
	South.MoveCar("green")
	East.MoveCar("red")
	West.MoveCar("red")
	print("N:",North.carqueue)
	print("S:",South.carqueue)
	print("E:",East.carqueue)
	print("W:",West.carqueue)
print("Cars in north lane:",len(North.carqueue))
print("Cars in south lane:",len(South.carqueue))
print("Cars in east lane:",len(East.carqueue))
print("Cars in west lane:",len(West.carqueue))
for x in range(6):
	x1= North.MoveCar("yellow")
	South.MoveCar("yellow")
	East.MoveCar("red")
	West.MoveCar("red")
	print("N:",North.carqueue)
	print("S:",South.carqueue)
	print("E:",East.carqueue)
	print("W:",West.carqueue)
print("Cars in north lane:",len(North.carqueue))
print("Cars in south lane:",len(South.carqueue))
print("Cars in east lane:",len(East.carqueue))
print("Cars in west lane:",len(West.carqueue))
for x in range(6):
	x1= North.MoveCar("red")
	South.MoveCar("red")
	East.MoveCar("green")
	West.MoveCar("green")
	print("N:",North.carqueue)
	print("S:",South.carqueue)
	print("E:",East.carqueue)
	print("W:",West.carqueue)
print("Cars in north lane:",len(North.carqueue))
print("Cars in south lane:",len(South.carqueue))
print("Cars in east lane:",len(East.carqueue))
print("Cars in west lane:",len(West.carqueue))
for x in range(6):
	x1= North.MoveCar("red")
	South.MoveCar("red")
	East.MoveCar("yellow")
	West.MoveCar("yellow")
	print("N:",North.carqueue)
	print("S:",South.carqueue)
	print("E:",East.carqueue)
	print("W:",West.carqueue)
print("Cars in north :

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
