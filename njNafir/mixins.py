import random, string

def get_unique_path(how_many=12):
	range_ = how_many
	chars = string.ascii_lowercase + string.digits
	path = ''.join(random.choice(chars) for _ in range(range_))
	return path