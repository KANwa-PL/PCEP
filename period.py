# Your task is to prepare a simple code able to evaluate the end time of a period of time, given as a number of minutes

hours = int(input("Starting time (hours): "))
minutes = int(input("Starting time (minutes): "))
duration = int(input("Event duration (minutes): "))

print("End of the period: " + str((hours + ((minutes + duration) // 60)) % 24), ":", (minutes + duration) % 60, sep="")
