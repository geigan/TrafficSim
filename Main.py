import Instance

'''for this tentative prototype, we assume the user
gives positive integers for all input.  
Processing for special cases may be implemented later.'''
def main():
	#while True:
	print("If no values are entered, the default time length is 20,")
	print("the default green light duration is 6,")
	print("and the default chance to generate a new car is 100%.")
	print("Press enter to use default values.")

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
		GreenTime = 6
	else:
		GreenTime = int(GreenTime)
	SpawnChance=input("Enter the percentage spawn chance from 1 to 100:")
	#if SpawnChance == "q":
		#break
	if SpawnChance == "":
		SpawnChance = 100
	else:
		SpawnChance = int(SpawnChance)		
	Highway=Instance.Instance(GreenTime,Cycles)
	Highway.GetSpawnChance(SpawnChance)
	Highway.RunSim()
main()
