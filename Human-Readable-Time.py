def make_readable(seconds):

	""" This function takes a non-negative integer (seconds) 
	as input and returns the time in a human-readable format 
	(HH:MM:SS)"""
	
	if seconds > 3600:
		HH = int(seconds / 3600)
		MM = int((seconds % 3600) / 60)
		SS = int(((seconds % 3600) / 60)%60)
		if HH < 10 or MM < 10 or SS < 10:
		    Human_readable = f"{str(HH).zfill(2)}:{str(MM).zfill(2)}:{str(SS).zfill(2)}"
		else:
		    Human_readable = f"{HH}:{MM}:{SS}"
		return(Human_readable)

	elif seconds >= 60 and seconds <= 3600:
		HH = 0
		MM = int(seconds / 60)
		SS = int(seconds % 60)
		if MM < 10 or SS < 10:
		    Human_readable = f"00:{str(MM).zfill(2)}:{str(SS).zfill(2)}"
		else:
		    Human_readable = f"00:{MM}:{SS}"
		return(Human_readable)

	elif seconds > 0 and seconds <= 60:
		SS = seconds
		if SS < 10:
		    Human_readable = f"00:00:{str(SS).zfill(2)}"
		else:
		    Human_readable = f"00:00:{SS}"
		return(Human_readable)
		
	else:
		Human_readable = "00:00:00"
		return(Human_readable)