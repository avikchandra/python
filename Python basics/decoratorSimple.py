def runStage(f):
	def insertHeader(*args):
		print("----")
		f(*args)
		print("----")
	return insertHeader

@runStage
def f2(name):
	print("Hi", name)

@runStage
def f3(name):
    print("Hello", name)

f2("A")
f3("B")
