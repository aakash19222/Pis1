def rotate(s, direction, k):
	"""
	This function takes a string, rotation direction and count
	as parameters and returns a string rotated in the defined
	direction count times.
	"""
	k = k%len(s)
	if direction == 'right':
		r = s[-k:] + s[:len(s)-k]
	elif direction == 'left':
		r = s[k:] + s[:k]
	else:
		r = ""
		print("Invalid direction")
	return r