	#!/usr/bin/env python

from Tkinter import *

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.hellolabel = Label(self, text='Hello, world!')
		self.hellolabel.pack()
		self.quitButton = Buttion(self, text='Quit', command=self.quit)
		self.quitButton.pack()

app = Application()

app.master.title('Hello World')

app.mainloop
