def make_readable(seconds):

	""" This function takes a non-negative integer (seconds) 
	as input and returns the time in a human-readable format 
	(HH:MM:SS)"""
	
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = seconds - (h * 3600) - (m * 60)
    return f"{h:0>2d}:{m:0>2d}:{s:0>2d}"