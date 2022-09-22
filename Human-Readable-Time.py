def make_readable(seconds):

	""" This function takes a non-negative integer (seconds) 
	as input and returns the time in a human-readable format 
	(HH:MM:SS)"""
	if seconds > 0 and seconds >= 3600:
		HH = int(seconds / 3600)
		MM = int((seconds % 3600) / 60)
		SS = int(((seconds % 3600) / 60)%60)
		Human_readable = f"{HH}:{MM}:{SS}"
		return(Human_readable)
	elif seconds in range(1, 3600):
		HH = str(00)
		MM = int(seconds / 60)
		SS = int((seconds / 60)%60)
		Human_readable = f"{HH}:{MM}:{SS}"
		return(Human_readable)

	elif seconds in range(1, 60):
		HH = str(00)
		MM = str(00)
		SS = seconds % 60
		Human_readable = f"{HH}:{MM}:{SS}"
		return(Human_readable)
	else:
		print("seconds are less than 0")