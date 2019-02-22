# Matthew Perez
# Langston's Ants, simple
# Only 1 ant. Can change board size

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
patch_color = {'white':0, 'black':10}


class Ant(object):
	def __init__(self, direction=0, pos=(width/2,height/2), color='g'):
		self.pos = pos #start ant in middle of board
		self.dir = direction
		self.color = color

	def step(self):
		global board

		#check board color
		#print('pre step', self.pos, 'dir', self.dir)
		#exit()
		if board[self.pos[1]][self.pos[0]] == patch_color['white']:
			self.dir -= 1
			board[self.pos[1]][self.pos[0]] = patch_color['black']


		elif board[self.pos[1]][self.pos[0]] == patch_color['black']:
			self.dir+=1
			board[self.pos[1]][self.pos[0]] = patch_color['white']

		#advance ant
		#0=N, 1=E, 2=S, 3=W
		dir_loc = self.dir % 4
		if dir_loc == 0:
			self.pos = (self.pos[0], self.pos[1]+1)
		elif dir_loc == 1:
			self.pos = (self.pos[0]+1, self.pos[1])
		elif dir_loc == 2:
			self.pos = (self.pos[0], self.pos[1]-1)
		elif dir_loc == 3:
			self.pos = (self.pos[0]-1, self.pos[1])

		#No wrap around
		if self.pos[0] < 0 or self.pos[0] > height or self.pos[1] < 0 or self.pos[1] > width:
			print("********* ant fell off the board *********")
			exit()

		# print('after step', self.pos, 'dir', self.dir)
		# print('after board', board)


def model_init():
	#initialize model
	global ant, board, time

	#create environment
	board = NP.zeros([height,width]) #careful with board = mapped (y, x)
	time = 0

	#create ant with random starting direction
	ant_start_dir = RD.randint(0,3)
	ant = Ant(ant_start_dir)

def model_draw():
	global ant, board, time

	PL.cla()
	PL.pcolor(board, cmap=PL.cm.binary)
	PL.axis('image')
	PL.hold(True)

	#list of x_pos of all ants (+0.5 to put in middle of square)
	x = ant.pos[0] + 0.5
	y = ant.pos[1] + 0.5
	colors = ant.color

	PL.scatter(x, y, c=colors)
	PL.hold(False) #clear board with each step
	PL.title('Time = ' + str(time)) #show timestep


def model_step():
	global ant, board, time

	time+=1
	#progress ant
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