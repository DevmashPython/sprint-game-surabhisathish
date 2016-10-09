import msvcrt
import time

finish=10
c=0
print "press enter_key to get started!"

raw_input()
s_time=time.time()

while(1):
	key=msvcrt.getch()
	if key=='\xe0':
		c=c+1
		print "-->",
		if c==finish:
			print'\t press down arrow'
			break
c=0	
print '\t\t\t\t\t',
while(1):			
	key=msvcrt.getch()
	if key=='\xe0':	
		c=c+1
		print "|"
		print '\t\t\t\t\t',
		if c==finish:
			break	
c=0	
while(1):			
	key=msvcrt.getch()		
	if key=='\xe0':		
		c=c+1
		print "-->",
		if c==finish:
			break

time_elapsed=time.time()-s_time
print "\ncongrats you have finished the game"
print "\ntime taken to complete the game is "+str(round(time_elapsed))

'''
1. Mention controls for the game.
2. The game should be lost on pressing the wrong key
3. fix controls for the game
'''
