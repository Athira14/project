import os

home = '.'

x= os.getcwd()

x=x.split("/")
print x[-1]

def rec(home):
	
	x=os.listdir(home)
	
	j = home.count('/')
	
	for i in range(len(x)):
	 
		print "\t"*(j+1),
		print x[i]
		if os.path.isdir(home+'/'+x[i]):
			rec(home+'/'+x[i])

		
rec(home)
