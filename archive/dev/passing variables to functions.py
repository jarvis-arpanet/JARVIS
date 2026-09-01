def function_a():
	name = "Bob"
	age = "42"
	return name, age

def function_b():
	name, age = function_a()
	print name
	print age

function_b()