'''
-------------------------------------------------
|	              Card Expore	      			|
|  				  Memory Game			 	 	|
|	 									 		|
|	 			 								|
|	Author :-  A. B. Pardikar           		|
|	Date:- Tue 12 Dec 2023 01:57:05 PM IST   	|
|	   											|
-------------------------------------------------
'''
# import the Module
import simpleguitk as gui 
from random import shuffle as SH
#--------Colors------------------------
colors = ['White','Red','Green','Blue','Cyan','Magenta',
'Purple','Maroon','Orange','Yellow','Brown','Gray','Olive',
'Violet','Tan','Teal','Pink',"DeepPink","DarkOrange",
"Lime","Aqua",'Fuchsia','Navy','Silver','Black']
#---------------------------------------
r = 5;c = 5
W = 50;Width = W*r
H = 100;Hight = H*c
# Globals
value = list(range(0,6))
values = value+value+value+value
values.append(0)
SH(values)
V = []
location = []
position = list()
state = turns = 0
#print(values)
# Helper functions
def Level0():
	global state, values, V, turns
	global location, position
	state = turns = 0
	turn.set_text("Turns:- "+str(turns))
	V = [];	location = [];	position = list()
	value = list(range(0,6))
	values = value+value+value+value
	values.append(0)
	SH(values)
def Level1():
	global state, values, V, turns
	global location, position
	state = turns = 0
	turn.set_text("Turns:- "+str(turns))
	V = [];	location = [];	position = list()
	value = list(range(0,4))
	values = value+value+value+value+list(range(4,9))+list(range(4,9))
	values.pop(0)
	SH(values)
def Level2():
	global state, values, V, turns
	global location, position
	state = turns = 0
	turn.set_text("Turns:- "+str(turns))
	V = [];	location = [];	position = list()
	value = list(range(0,3))
	values = value+value+value+value+list(range(3,10))+list(range(3,10))
	values.pop(0)
	SH(values)
def Level3():
	global state, values, V, turns
	global location, position
	state = turns = 0
	turn.set_text("Turns:- "+str(turns))
	V = [];	location = [];	position = list()
	value = list(range(0,2))
	values = value+value+value+value+list(range(2,10))+list(range(2,10))
	values.append(0)
	SH(values)

def click(pos):
	global state,turns,location,position,V,values
	turns += 1
	turn.set_text("Turns:- "+str(turns))
	for i in range(r):
		for j in range(c):
			if pos[0] in range(j*W,(j+1)*W)and pos[1] in range(i*H,(i+1)*H):
				box = (i,j)
#	print(box)
	if str(values[box[0]*5+box[1]]) in V:
			turns -= 1
#	if len(str(values[box[0]*5+box[1]])) == 2:
#		posi =[box[1]*W+8,(box[0]+1)*H-22]
#	else:
	posi =[box[1]*W+12,(box[0]+1)*H-22]
	position.append(posi)
#	print(position)
	V.append(str(values[box[0]*5+box[1]]))
	loc = [(box[1]*W,box[0]*H),((box[1]+1)*W,box[0]*H),
	((box[1]+1)*W,(box[0]+1)*H),(box[1]*W,(box[0]+1)*H)]
	location.append(loc)
#	print(location)
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
		
#		print(V)
# Define Event Handler
# define canvas function for drawing
def draw(canvas):
	for line in range(r):
		canvas.draw_line([line*W,0],[line*W,Hight+20], 3, colors[-2])
	for line in range(1,c+1):
		canvas.draw_line([0,line*H],[Width+20,line*H],3,colors[-2])
	for i in range(len(location)):
		canvas.draw_polygon(location[i], 3, colors[-2], colors[-1])
	for j in range(len(V)):
		canvas.draw_text(V[j], position[j], 28, colors[0])

# creat a frame
frame = gui.create_frame("Card Explore",Width,Hight)
frame.set_canvas_background(colors[12])
# Register Event handler
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)
turn = frame.add_label("Turns:- "+str(turns))
frame.add_label('')
frame.add_button('Level0',Level0,100);frame.add_label('')
frame.add_button('Level1',Level1,100);frame.add_label('')
frame.add_button('Level2',Level2,100);frame.add_label('')
frame.add_button('Level3',Level3,100);frame.add_label('')

# start the frame
frame.start()

