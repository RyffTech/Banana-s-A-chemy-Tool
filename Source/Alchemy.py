"""
Initial Coding Started 22:43, 2016-30-7
:::Logs:::
2016-1-8 == added check for to many stats, added check for no recipe, added tri stat pots
2016-1-8 == added background image

TO DO LIST:
'NEED TO FINISH ADDING IN SINGLE STAT POTS'

Author = Chris Riffle
Version = 0.1.0
"""

from Tkinter import *
import Tkinter as tk
import os
import sys
import time


class alchemyApp():
	
	def __init__(self, master):
	
		self.master = master
		master.title("BANANA'S ALCHEMY TOOL")
		master.iconbitmap('banana.ico')
		master.configure(bg="black")
		master.maxsize(600,420)
		master.minsize(600,420)
		
		self.background   = PhotoImage(file="bgpic.gif")
		bg_label = tk.Label(root, image =self.background)
		bg_label.place(x=0,y=0,relwidth=1,relheight=1)
		
		
		
		self.flowerA = PhotoImage(file="A.gif")
		self.flowerB = PhotoImage(file="B.gif")
		self.flowerC = PhotoImage(file="C.gif")
		self.flowerD = PhotoImage(file="D.gif")
		self.flowerE = PhotoImage(file="E.gif")
		self.flowerF = PhotoImage(file="F.gif")
		self.flowerG = PhotoImage(file="G.gif")
		self.blank   = PhotoImage(file="1.gif")
		self.tomany1 = PhotoImage(file="2m1.gif")
		self.tomany2 = PhotoImage(file="2m2.gif")
		self.tomany3 = PhotoImage(file="2m3.gif")
		self.norec1 = PhotoImage(file="norec1.gif")	
		self.norec2 = PhotoImage(file="norec2.gif")
		self.norec3 = PhotoImage(file="norec3.gif")	
		self.btback = PhotoImage(file="btbg.gif")
		self.wood   = PhotoImage(file="wood.gif")
		
		tk.Label(root, image = self.flowerA)#.grid(row=7,column=6, sticky=W)
		tk.Label(root, image = self.flowerB)#.grid(row=7,column=6, sticky=W)
		tk.Label(root, image = self.flowerC)#.grid(row=7,column=6, sticky=W)
		tk.Label(root, image = self.flowerD)#.grid(row=7,column=6, sticky=W)
		tk.Label(root, image = self.flowerE)#.grid(row=7,column=6, sticky=W)
		tk.Label(root, image = self.flowerF)#.grid(row=7,column=6, sticky=W)
		tk.Label(root, image = self.flowerG)#.grid(row=7,column=6, sticky=W)
		
		self.stats()
	def checkNumbers(self):
		self.total = (self.hitpoints.get() + self.endurance.get() + self.mana.get() +
		self.wisdom.get() + self.intuition.get() + self.agility.get() +
		self.strength.get() + self.hand2hand.get() + self.sword.get() +
		self.twohanded.get() + self.dagger.get() + self.staff.get() +
		self.rage.get() + self.attack.get() + self.parry.get() +
		self.tactics.get() + self.warcry.get() + self.surroundhit.get() +
		self.speedskill.get() + self.immunity.get() + self.bartering.get() +
		self.perception.get() + self.stealth.get() +self.duration.get() +
		self.bless.get() + self.heal.get() + self.freeze.get() +
		self.lightning.get() + self.magicshield.get() + self.fire.get() +
		self.pulse.get() + self.light.get()) 
		
		if self.total >= 4:
			
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.tomany1,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.tomany2,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.tomany3,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=8, sticky=W)
			root.after(1000,self.findButton())
			
		else:
			self.findRecipe()
			
	def stats(self):	
		self.hitpoints = IntVar()
		self.endurance = IntVar()
		self.mana = IntVar()
		self.wisdom = IntVar()
		self.intuition = IntVar()
		self.agility = IntVar()
		self.strength = IntVar()
		self.hand2hand = IntVar()
		self.sword = IntVar()
		self.twohanded = IntVar()
		self.dagger = IntVar()
		self.staff = IntVar()
		self.rage = IntVar()
		self.attack = IntVar()
		self.parry = IntVar()
		self.tactics = IntVar()
		self.warcry = IntVar()
		self.surroundhit = IntVar()
		self.speedskill = IntVar()
		self.immunity = IntVar()
		self.bartering = IntVar()
		self.perception = IntVar()
		self.stealth = IntVar()
		self.duration = IntVar()
		self.bless = IntVar()
		self.heal = IntVar()
		self.freeze = IntVar()
		self.magicshield = IntVar()
		self.lightning = IntVar()
		self.fire = IntVar()
		self.pulse = IntVar()
		self.light = IntVar()
		
		a = Checkbutton(root, text="HP          ",fg="black", variable=self.hitpoints).grid(row=0,columnspan = 2, sticky=W)
		b = Checkbutton(root, text="Endurance   ",fg="black", variable=self.endurance).grid(row=1, sticky=W)
		c = Checkbutton(root, text="Mana        ",fg="black", variable=self.mana).grid(row=2, sticky=W)
		d = Checkbutton(root, text="Wisdom      ",fg="black", variable=self.wisdom).grid(row=3, sticky=W)
		e = Checkbutton(root, text="Intuition   ",fg="black", variable=self.intuition).grid(row=4, sticky=W)
		f = Checkbutton(root, text="Agility     ",fg="black", variable=self.agility).grid(row=5, sticky=W)
		g = Checkbutton(root, text="Strength    ",fg="black", variable=self.strength).grid(row=6, sticky=W)
		h = Checkbutton(root, text="Dagger      ",fg="black", variable=self.dagger).grid(row=7, sticky=W)
		i = Checkbutton(root, text="Staff       ",fg="black", variable=self.staff).grid(row=8, sticky=W)
		j = Checkbutton(root, text="Hand 2 Hand ",fg="black", variable=self.hand2hand).grid(row=9, sticky=W)
		k = Checkbutton(root, text="Sword       ",fg="black", variable=self.sword).grid(row=10, sticky=W)
		l = Checkbutton(root, text="2 Handed    ",fg="black", variable=self.twohanded).grid(row=11, sticky=W)
		m = Checkbutton(root, text="Rage        ",fg="black", variable=self.rage).grid(row=12, sticky=W)
		n = Checkbutton(root, text="Attack      ",fg="black", variable=self.attack).grid(row=13, sticky=W)
		o = Checkbutton(root, text="Parry       ",fg="black", variable=self.parry).grid(row=14, sticky=W)
		p = Checkbutton(root, text="Tactics     ",fg="black", variable=self.tactics).grid(row=15, sticky=W)
		q = Checkbutton(root, text="Warcry      ",fg="black", variable=self.warcry).grid(row=0, column=1, sticky=W)
		r = Checkbutton(root, text="Surround Hit",fg="black",bd=0, variable=self.surroundhit).grid(row=1, column=1,sticky=W)
		s = Checkbutton(root, text="Speed SKill ",fg="black", variable=self.speedskill).grid(row=2, column=1, sticky=W)
		t = Checkbutton(root, text="Immunity    ",fg="black", variable=self.immunity).grid(row=3, column=1, sticky=W)
		u = Checkbutton(root, text="Bartering   ",fg="black", variable=self.bartering).grid(row=4, column=1, sticky=W)
		v = Checkbutton(root, text="Perception  ",fg="black", variable=self.perception).grid(row=5, column=1, sticky=W)
		w = Checkbutton(root, text="Stealth     ",fg="black", variable=self.stealth).grid(row=6, column=1, sticky=W)
		x = Checkbutton(root, text="Duration    ",fg="black", variable=self.duration).grid(row=7, column=1, sticky=W)
		y = Checkbutton(root, text="Bless       ",fg="black", variable=self.bless).grid(row=8, column=1, sticky=W)
		z = Checkbutton(root, text="Heal        ",fg="black", variable=self.heal).grid(row=9, column=1, sticky=W)
		aa = Checkbutton(root, text="Freeze      ",fg="black", variable=self.freeze).grid(row=10, column=1, sticky=W)
		bb = Checkbutton(root, text="Magic Shield",fg="black",bd=0, variable=self.magicshield).grid(row=11, column=1, sticky=W)
		cc = Checkbutton(root, text="Lightning   ",fg="black", variable=self.lightning).grid(row=12, column=1, sticky=W)
		dd = Checkbutton(root, text="Fire        ",fg="black", variable=self.fire).grid(row=13, column=1, sticky=W)
		ee = Checkbutton(root, text="Pulse       ",fg="black", variable=self.pulse).grid(row=14, column=1, sticky=W)
		ff = Checkbutton(root, text="Light       ",fg="black", variable=self.light).grid(row=15, column=1, sticky=W)
		
		tk.Label(root, image = self.wood,bd=0).grid(row=7,column=3, sticky=W)
		tk.Label(root, image = self.wood,bd=0).grid(row=7,column=4,padx=0,pady=0, sticky=W)
		tk.Label(root, image = self.wood,bd=0).grid(row=7,column=5,padx=0,pady=0, sticky=W)
		tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6,padx=0,pady=0, sticky=W)
		tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7,padx=0,pady=0,sticky=W)
		tk.Label(root, image = self.wood,bd=0).grid(row=7,column=8,padx=0,pady=0,sticky=W)
		self.findButton()
		
	def findButton(self):
		button = Button(root, height=1, width=10, text="CHECK", command=self.checkNumbers).grid(row=4,column=2)
		
		#22334
	def findRecipe(self):
		
		if self.intuition.get() == 1 and self.agility.get()==1 and self.strength.get()==1:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=7, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=8, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.wisdom.get() == 1 and self.agility.get()==1 and self.mana.get()==1:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.wisdom.get() == 1 and self.intuition.get()==1 and self.strength.get()==1:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.lightning.get() == 1 and self.magicshield.get()==1 and self.freeze.get()==1:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.lightning.get() == 1 and self.freeze.get()==1 and self.pulse.get()==1:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.attack.get() == 1 and self.parry.get()==1 and self.freeze.get()==1:
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.fire.get() == 1 and self.magicshield.get()==1 and self.freeze.get()==1:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.fire.get() == 1 and self.freeze.get()==1 and self.pulse.get()==1:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.hitpoints.get() == 1 and self.sword.get()==1 and self.rage.get()==1:
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.hitpoints.get() ==1 and self.rage.get()==1 and self.immunity.get()==1:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.sword.get() ==1 and self.attack.get()==1 and self.parry.get()==1:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.intuition.get() ==1 and self.wisdom.get()==1 and self.fire.get()==1:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.intuition.get() ==1 and self.wisdom.get()==1 and self.lightning.get()==1:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.attack.get() ==1 and self.lightning.get()==1 and self.immunity.get()==1:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.twohanded.get() ==1 and self.attack.get()==1 and self.parry.get()==1:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.attack.get() ==1 and self.fire.get()==1 and self.immunity.get()==1:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.lightning.get() ==1 and self.immunity.get()==1 and self.pulse.get()==1:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.lightning.get() ==1 and self.magicshield.get()==1 and self.immunity.get()==1:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.lightning.get() ==1 and self.magicshield.get()==1 and self.pulse.get()==1:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.attack.get() ==1 and self.parry.get()==1 and self.immunity.get()==1:
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.fire.get() ==1 and self.immunity.get()==1 and self.pulse.get()==1:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.fire.get() ==1 and self.immunity.get()==1 and self.magicshield.get()==1:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.fire.get() ==1 and self.pulse.get()==1 and self.magicshield.get()==1:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.immunity.get() ==1 and self.pulse.get()==1  and self.total == 2:
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.dagger.get() ==1 and self.attack.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.immunity.get() ==1 and self.tactics.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.magicshield.get() ==1 and self.pulse.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.immunity.get() ==1 and self.magicshield.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.immunity.get() ==1 and self.fire.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.twohanded.get() ==1 and self.attack.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.rage.get() ==1 and self.tactics.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.twohanded.get() ==1 and self.parry.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.dagger.get() ==1 and self.lightning.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.dagger.get() ==1 and self.fire.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.staff.get() ==1 and self.lightning.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.staff.get() ==1 and self.fire.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.sword.get() ==1 and self.attack.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.sword.get() ==1 and self.parry.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.lightning.get() ==1 and self.immunity.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.dagger.get() ==1 and self.parry.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.lightning.get() ==1 and self.pulse.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.lightning.get() ==1 and self.fire.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.pulse.get() ==1 and self.fire.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.parry.get() ==1 and self.pulse.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.pulse.get() ==1 and self.attack.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.fire.get() ==1 and self.magicshield.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.tactics.get() ==1 and self.attack.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.lightning.get() ==1 and self.magicshield.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.parry.get() ==1 and self.attack.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.stealth.get() ==1 and self.perception.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.sword.get() ==1 and self.tactics.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.freeze.get() ==1 and self.fire.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.freeze.get() ==1 and self.lightning.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.freeze.get() ==1 and self.warcry.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.freeze.get() ==1 and self.pulse.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.wisdom.get() ==1 and self.tactics.get()==1 and self.total == 2:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.duration.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.magicshield.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		elif self.fire.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.pulse.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.immunity.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.rage.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.freeze.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.staff.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.hand2hand.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.dagger.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.sword.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.lightning.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.warcry.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.attack.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.surroundhit.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.perception.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.stealth.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.parry.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.bless.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.heal.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.tactics.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.bartering.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.light.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.endurance.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerG,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.mana.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerF,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.hitpoints.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerE,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.strength.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerD,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.agility.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerC,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.intuition.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerB,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
			
		elif self.wisdom.get() ==1 and self.total ==1:
			tk.Label(root, image = self.flowerA,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			root.after(1000,self.findButton())
		
		else:
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=3, sticky=W)
			tk.Label(root, image = self.norec1,bd=0).grid(row=7,column=4, sticky=W)
			tk.Label(root, image = self.norec2,bd=0).grid(row=7,column=5, sticky=W)
			tk.Label(root, image = self.norec3,bd=0).grid(row=7,column=6, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=7, sticky=W)
			tk.Label(root, image = self.wood,bd=0).grid(row=7,column=8, sticky=W)
			root.after(1000,self.findButton())
			
	def recipes(self):
		self.flowers = {"A",'B','C','D','E','F','G'}
		
		
		
root = Tk()
app=alchemyApp(root)
root.mainloop()