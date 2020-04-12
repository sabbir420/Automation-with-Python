import re
def rearrange_name(name):
	#patter = r"^([\w \.-]*), ([\w \.-]*)$"
	pattern = r"^(\w*), (\w*\s[A-Z]{1}[\.])$"
	result = re.search(pattern, name)
	if result is None:
		return name
	return "{} {}".format(result[2], result[1])
	
print(rearrange_name("Peter, Kevin"))
print(rearrange_name("Jovi, Bon"))
print(rearrange_name("Kennedy, John F."))