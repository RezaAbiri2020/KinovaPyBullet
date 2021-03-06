import pygame as pg
import numpy as np
import time
import os
import csv

class UI(object):
	def __init__(self, log):
		self.screen = pg.display.get_surface()
		self.done = False 
		self.mode = 0
		self.makeButtons()
		self.newTime = time.time()
		self.modeList = ['Horizontal Translation', 'Vertical Trans, Orientation 1', 'Orientation 2, 3', 'Gripper']
		self.colorList = [pg.Color('dodgerblue'), pg.Color('red'), pg.Color('orange'), pg.Color('green')]
		self.font = pg.font.Font(None, 40)
		self.updateText()
		self.state = -1
		self.prevState = -1
		self.log = log
		self.maxMode = 3

		if self.log:
			dataDir = time.strftime("%Y%m%d")

			if not os.path.exists(dataDir):
				os.makedirs(dataDir)
			trialInd = len(os.listdir(dataDir))
			self.fn = dataDir + "/data00" + str(trialInd) + ".csv"
			self.startLogger(self.fn)

	def makeButtons(self):
		self.xl = []
		self.xu = []
		self.yl = []
		self.yu = []
		button = []
		rect = []
		self.screen.fill((0,0,0))

		for i in range(9):
			button.append(pg.image.load('img/a' + str(self.mode) + '_' + str(i+1) + '.png').convert())
			rect.append(button[i].get_rect())
			row = i // 3
			col = np.mod(i,3)
			rect[i].center = 100 + 150*col, 400 - row*150
			self.xl.append(rect[i].x)
			self.xu.append(rect[i].x + rect[i].w)
			self.yl.append(rect[i].y)
			self.yu.append(rect[i].y + rect[i].h)
			self.screen.blit(button[i], rect[i])
			self.x = 0
			self.y = 0
			pg.draw.rect(self.screen, (0,0,0), rect[i], 1)

		pg.display.update()

	def updateText(self):

		self.makeButtons

		pgTxt1 = 'Mode ' + str(self.mode + 1) + ': ' + self.modeList[self.mode]
		color = self.colorList[self.mode]

		self.screen.fill((0,0,0), (0,0,500, 50))  
		self.txt_surface1 = self.font.render(pgTxt1, True, color)
		self.screen.blit(self.txt_surface1, (10, 10))
		pg.display.flip()

	def update(self):	

		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.done = True

		m = pg.mouse.get_pos()
		self.x = m[0]
		self.y = m[1]

		if time.time() - self.newTime > 0.2 :
			self.newTime = time.time()

			self.prevState = self.state
			self.state = -1

			for i in range(9):
				if  (self.xl[i]  <= m[0] <=  self.xu[i]) & (self.yl[i]  <= m[1] <=  self.yu[i]):
					self.state = i+1


			if self.state == 3 and self.prevState != 3:
				if self.mode < self.maxMode:
					self.mode = self.mode + 1
				else:
					self.mode = 0
				self.updateText()	
		if self.log:
			self.updateLogger()

	def startLogger(self, fn):
			self.file  = open(fn, "w", newline = '')
			self.fileObj = csv.writer(self.file)
			self.logOpen = True
			self.logT = time.time()

	def updateLogger(self):

		if time.time() - self.logT > 0.01:
			self.logT = time.time()
			line = [time.time(), self.x, self.y, self.state, self.mode]
			self.fileObj.writerow(line)

	def closeLogger(self):
		self.file.close()
		self.logOpen = False	
			

if __name__ == "__main__":
	pg.init()
	pg.display.set_mode((500,500))
	pg.display.set_caption("Control Interface")
	runUI = UI(1)

	while not runUI.done:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				runUI.closeLogger()
				runUI.done = True
		runUI.update()
	pg.quit()