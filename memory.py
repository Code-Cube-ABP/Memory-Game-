'''
-------------------------------------------------
|	              Card Expore	      			|
|  				  Memory Game			 	 	|
|	 									 		|
|	 			 								|
|	Author :-  A. B. Pardikar           		|
|	Date:- Wed 08 Nov 2023 02:29:36 PM IST   	|
|	   											|
-------------------------------------------------
'''
# import the Module
import simpleguitk as gui 
from random import shuffle as SH
from random import randrange as R
#--------Colors------------------------
colors = ['White','Red','Green','Blue','Cyan','Magenta',
'Purple','Maroon','Orange','Yellow','Brown','Gray','Olive',
'Violet','Tan','Teal','Pink',"DeepPink","DarkOrange",
"Lime","Aqua",'Fuchsia','Navy','Silver','Black']
#---------------------------------------
W = 50
Width = W*16
Hight = 150
# Globals
values = list(range(0,8))+list(range(0,8))
SH(values)
V = []
location = []
position = list()
state = turns = 0

# Helper functions
def Newgame():
	global state, values, V, turns
	global location, position
	state = turns = 0
	V = []
	location = []
	position = list()
	SH(values)
	turn.set_text("Turns:- "+str(turns))
#print(values)
def click(pos):
	global state,turns,location,W,position,V,values
	turns += 1
	turn.set_text("Turns:- "+str(turns))
	for i in range(16):
		if pos[0] in range(i*W,(i+1)*W):
			box = i
#	print(V)
	if str(values[box]) in V:
			turns -= 1
	posi =[box*W+14,90]
	position.append(posi)
	V.append(str(values[box]))
	loc = [(box*W,0),((box+1)*W,0),((box+1)*W,Hight),(box*W,Hight)]
	location.append(loc)
	if state == 0:
		state = 1
	elif state == 1:
		state = 2
	else:
		if V[-3] != V[-2]:
			V.pop(-2); V.pop(-2)
			position.pop(-2); position.pop(-2)
			location.pop(-2); location.pop(-2)
		state = 1
#		
#		print(V)
# Define Event Handler
# define canvas function for drawing
def draw(canvas):
	for line in range(16):
		canvas.draw_line([line*W,0],[line*W,Hight+20], 3, colors[-2])
	for i in range(len(location)):
		canvas.draw_polygon(location[i], 3, colors[-2], colors[-1])
	for j in range(len(V)):
		canvas.draw_text(V[j], position[j], 34, colors[0])

# creat a frame
frame = gui.create_frame("Card Explore",Width,Hight)
frame.set_canvas_background(colors[12])
# Register Event handler
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
frame.add_button('Restart',Newgame,100)
turn = frame.add_label("Turns:- "+str(turns))
# start the frame
frame.start()

