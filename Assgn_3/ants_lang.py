# Matthew Perez
# Langston's Ants, expanded
# Features: 
# 	Color map change
#	Multiple Ants
# 	Wrap behavior
#	randomize ant starting position

import matplotlib
matplotlib.use('TkAgg')

import pylab as PL
import random as RD
import scipy as SP
import numpy as NP

RD.seed()

#Variable initialization
width = 100
height = 100
populationSize = 2


class Ant(object):
	def __init__(self, direction=0, pos=(width/2,height/2), color='g'):
		self.pos = pos
		self.dir = direction #0=N, 1=E, 2=S, 3=W
		self.color = color

	def step(self):
		global board

		#check board color. Board counter, use modulo to simulate black and white functionality
		if board[self.pos[1]][self.pos[0]] % 2 == 0:
			self.dir -= 1
			board[self.pos[1]][self.pos[0]]+=1


		elif board[self.pos[1]][self.pos[0]] % 2 == 1:
			self.dir+=1
			board[self.pos[1]][self.pos[0]]+=1

		#advance ant and wrap based on width/height
		dir_loc = self.dir % 4
		if dir_loc == 0:
			self.pos = (self.pos[0] % width, (self.pos[1]+1) % height)
		elif dir_loc == 1:
			self.pos = ((self.pos[0]+1) % width, self.pos[1]% height)
		elif dir_loc == 2:
			self.pos = (self.pos[0] % width, (self.pos[1]-1)% height)
		elif dir_loc == 3:
			self.pos = ((self.pos[0]-1) % width, self.pos[1]% height)

		#No wrap around
		# if self.pos[0] < 0 or self.pos[0] > height or self.pos[1] < 0 or self.pos[1] > width:
		# 	print("********* ant fell off the board *********")
		# 	exit()
		# print('after step', self.pos, 'dir', self.dir)
		# print('after board', board)


def model_init():
	#initialize model
	global ant_list, board, time

	#keep track of ants
	ant_list = []

	#create environment
	board = NP.zeros([height,width]) #careful with board = mapped (y, x)
	time = 0

	#create x amount of ants
	for i in range(populationSize):
		ant_start_dir = RD.randint(0,3)
		ant_start_pos = (RD.randint(0,width-1), RD.randint(0,height-1))

		my_ant = Ant(ant_start_dir, ant_start_pos)
		ant_list.append(my_ant)

def model_draw():
	global ant_list, board, time

	PL.cla()
	#PL.pcolor(board, cmap=PL.cm.hot) #heat map
	PL.pcolor(board, cmap=PL.cm.prism) #for pretty pictures
	PL.axis('image')
	PL.hold(True)

	#list of x_pos of all ants (+0.5 to put in middle of square)
	x = [ag.pos[0] + 0.5 for ag in ant_list]
	y = [ag.pos[1] + 0.5 for ag in ant_list]
	colors = [ag.color for ag in ant_list]

	PL.scatter(x, y, c=colors)
	PL.hold(False) #clear board with each step
	PL.title('Time = ' + str(time))


def model_step():
	global ant_list, board, time

	time+=1
	#progress ant
	for ant in ant_list:
		ant.step()


def main():
	#run simulator
	import sys
	sys.path.append("../pycx-0.32")
	import pycxsimulator

	#create GUI object with default settings
	#start takes 3 functions [model_init, model_draw, model_stap]
	pycxsimulator.GUI().start(func=[model_init, model_draw, model_step])

if __name__ == "__main__":
	main()