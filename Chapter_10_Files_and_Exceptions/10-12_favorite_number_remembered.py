import json

def get_stored_fav_num():
	"""Get stored favorite number if available."""
	filename = 'favNum.json'
	try:
		with open(filename) as f_obj:
			favNum = json.load(f_obj)
	except OSError:
		return None
	else:
		return favNum
	
def get_new_fav_num():
	favNum = input("What is your favorite number? ")
	filename = 'favNum.json'
	with open(filename, 'w') as f_obj:
		json.dump(favNum, f_obj)
	return favNum

def display_fav_num():
	"""Display the favorite number that is stored"""
	favNum = get_stored_fav_num()
	if favNum:
		print ("I know your favorite number! It's " + favNum+ "!")
	else:
		favNum = get_new_fav_num()
		print("We'll remember your favorite number when you come back!")
		
display_fav_num()