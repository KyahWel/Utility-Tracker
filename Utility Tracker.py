from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
#-------------- INIT TKINTER -------------------#
root = Tk()
root.resizable(False,False)
root.iconbitmap('logo.ico')

#--------------- INIT DICTIONARY -----------------#
electrack = {'january':[],'february':[],'march':[],'april':[],'may':[],
				'june':[],'july':[],'august':[],'september':[],'october':[]
				,'november':[],'december':[]}

watertrack = {'january':[],'february':[],'march':[],'april':[],'may':[],
				'june':[],'july':[],'august':[],'september':[],'october':[]
				,'november':[],'december':[]}

listmonth = ['january','february','march','april','may','june','july','august','september','october','november','december']

def updateDictElect(month,price):
	electrack[month]=price

def updateDictWater(month,price):
	watertrack[month]=price


def hideAllFrames():
	for widget in mainframe.winfo_children():
		widget.destroy()
	for widget in secondframe.winfo_children():
		widget.destroy()
	for widget in thirdframe.winfo_children():
		widget.destroy()	
	for widget in fourthframe.winfo_children():
		widget.destroy()
	for widget in fifthframe.winfo_children():
		widget.destroy()
	for widget in sixthframe.winfo_children():
		widget.destroy()
	for widget in seventhframe.winfo_children():
		widget.destroy()
	for widget in eightframe.winfo_children():
		widget.destroy()
	for widget in ninthframe.winfo_children():
		widget.destroy()
	for widget in tenthframe.winfo_children():
		widget.destroy()

	mainframe.pack_forget()
	secondframe.pack_forget()
	thirdframe.pack_forget()
	fourthframe.pack_forget()
	fifthframe.pack_forget()
	sixthframe.pack_forget()
	seventhframe.pack_forget()
	eightframe.pack_forget()
	ninthframe.pack_forget()
	tenthframe.pack_forget()

#--------------- FRAME INIT -----------------#

def initwindowsize(size):
	return root.geometry(size)
#----------------------FIRST FRAME WIDGETS-----------------------------------#
def showMainFrame():
	initwindowsize("350x350")
	hideAllFrames()
	root.title('Homepage')

	def mousehoverEnter(e):
		exitButton.config(bg='red',fg='white',font=("Century Gothic",10,"bold"))

	def mousehoverLeave(e):
		exitButton.config(bg='white',fg='black',font=("Century Gothic",10))

	def mousehoverEnterA(e):
		mainbutton.config(bg='green',fg='white',font=("Century Gothic",10,"bold"))

	def mousehoverLeaveA(e):
		mainbutton.config(bg='white',fg='black',font=("Century Gothic",10))


	mainframe.pack(pady=50,padx=5)
	titleLabel = Label(mainframe,text="Consumption Tracker",pady=20)
	titleLabel.config(font=("Century Gothic",20,"bold"))
	titleLabel.pack()

	mainbutton = Button(mainframe, text="Main Menu",command=lambda:[showSecondFrame(),img.destroy()])
	mainbutton.config(font=("Century Gothic",10))
	mainbutton.pack()
	mainbutton.bind("<Enter>",mousehoverEnterA)
	mainbutton.bind("<Leave>",mousehoverLeaveA)

	exitButton = Button(mainframe, text="Quit",command=root.quit)
	exitButton.config(font=("Century Gothic",10))
	exitButton.pack()
	exitButton.bind("<Enter>",mousehoverEnter)
	exitButton.bind("<Leave>",mousehoverLeave)
	
	load = Image.open("logo.png")
	load = load.resize((105,102),Image.ANTIALIAS)
	render = ImageTk.PhotoImage(load)
	img = Label(image = render)
	img.image = render
	img.place(x=120,y=20)
#----------------------SECOND FRAME WIDGETS----------------------------------#
def showSecondFrame():
	initwindowsize("300x400")
	root.title('Main Menu')
	hideAllFrames()

	def mousehoverEnter(e):
		backbutton.config(bg='red',fg='white',font=("Century Gothic",10,"bold"))
	def mousehoverLeave(e):
		backbutton.config(bg='white',fg='black',font=("Century Gothic",10))
	def mousehoverEnterA(e):
		Consumptionbutton.config(bg='green',fg='white',font=("Century Gothic",10,"bold"))
	def mousehoverLeaveA(e):
		Consumptionbutton.config(bg='white',fg='black',font=("Century Gothic",10))
	def mousehoverEnterB(e):
		Displaybutton.config(bg='green',fg='white',font=("Century Gothic",10,"bold"))
	def mousehoverLeaveB(e):
		Displaybutton.config(bg='white',fg='black',font=("Century Gothic",10))

	secondframe.pack(pady=40,padx=5)
	stitleLabel = Label(secondframe,text="Choose Below",pady=10)
	stitleLabel.config(font=("Century Gothic",20,"bold"))
	stitleLabel.pack()

	Consumptionbutton = Button(secondframe, text="Consumption",command=showThirdFrame)
	Consumptionbutton.config(font=("Century Gothic",10))
	Consumptionbutton.pack(pady=3)
	Consumptionbutton.bind("<Enter>",mousehoverEnterA)
	Consumptionbutton.bind("<Leave>",mousehoverLeaveA)

	Displaybutton = Button(secondframe, text="Display Track",command=showSixthFrame)
	Displaybutton.config(font=("Century Gothic",10))
	Displaybutton.pack(pady=3)
	Displaybutton.bind("<Enter>",mousehoverEnterB)
	Displaybutton.bind("<Leave>",mousehoverLeaveB)

	backbutton = Button(secondframe, text="Back",command=showMainFrame)
	backbutton.config(font=("Century Gothic",10))
	backbutton.pack(pady=3)
	backbutton.bind("<Enter>",mousehoverEnter)
	backbutton.bind("<Leave>",mousehoverLeave)
#----------------------- THIRD FRAME WIDGETS (Consumption) --------------------------------#
def showThirdFrame():
	initwindowsize("300x400")
	root.title('Consumption Page')
	hideAllFrames()

	def mousehoverEnter(e):
		backbutton.config(bg='red',fg='white',font=("Century Gothic",10,"bold"))
	def mousehoverLeave(e):
		backbutton.config(bg='white',fg='black',font=("Century Gothic",10))
	def mousehoverEnterA(e):
		Consumptionbutton.config(bg='green',fg='white',font=("Century Gothic",10,"bold"))
	def mousehoverLeaveA(e):
		Consumptionbutton.config(bg='white',fg='black',font=("Century Gothic",10))
	def mousehoverEnterB(e):
		Displaybutton.config(bg='green',fg='white',font=("Century Gothic",10,"bold"))
	def mousehoverLeaveB(e):
		Displaybutton.config(bg='white',fg='black',font=("Century Gothic",10))

	thirdframe.pack(pady=40,padx=5)
	ttitleLabel = Label(thirdframe,text="Choose Below",pady=10)
	ttitleLabel.config(font=("Century Gothic",20,"bold"))
	ttitleLabel.pack()

	Consumptionbutton = Button(thirdframe, text="Electricity",command=showFourthFrame)
	Consumptionbutton.config(font=("Century Gothic",10))
	Consumptionbutton.pack(pady=3)
	Consumptionbutton.bind("<Enter>",mousehoverEnterA)
	Consumptionbutton.bind("<Leave>",mousehoverLeaveA)

	Displaybutton = Button(thirdframe, text="Water",command=showNinthFrame)
	Displaybutton.config(font=("Century Gothic",10))
	Displaybutton.pack(pady=3)
	Displaybutton.bind("<Enter>",mousehoverEnterB)
	Displaybutton.bind("<Leave>",mousehoverLeaveB)

	backbutton = Button(thirdframe, text="Back",command=showSecondFrame)
	backbutton.config(font=("Century Gothic",10))
	backbutton.pack(pady=3)
	backbutton.bind("<Enter>",mousehoverEnter)
	backbutton.bind("<Leave>",mousehoverLeave)

#----------------------- FOURTH FRAME WIDGETS (Electricity) --------------------------------#
def showFourthFrame():
	initwindowsize("370x500")
	hideAllFrames()
	def mousehoverEnter(e):
		backbutton.config(bg='red',fg='white')
	def mousehoverLeave(e):
		backbutton.config(bg='white',fg='black')
	def smousehoverEnter(e):
		submitbutton.config(bg='green',fg='white')
	def smousehoverLeave(e):
		submitbutton.config(bg='white',fg='black')
	def showmousehoverEnter(e):
		showbutton.config(bg='blue',fg='white')
	def showmousehoverLeave(e):
		showbutton.config(bg='white',fg='black')

	fourthframe.pack(fill="both",expand=1)
	titleLabel = Label(fourthframe,text="Electric Bill Calculator",pady=20)
	titleLabel.config(font=("Century Gothic",20,"bold"))
	titleLabel.pack()

	showbutton = Button(fourthframe, text="Show Receipt")
	showbutton.config(font=("Century Gothic",10))

	submitbutton = Button(fourthframe, text="Submit")
	submitbutton.config(font=("Century Gothic",10))

	backbutton = Button(fourthframe, text="Back",command=showThirdFrame)
	backbutton.config(font=("Century Gothic",10))
	backbutton.pack(pady=3)
	backbutton.bind("<Enter>",mousehoverEnter)
	backbutton.bind("<Leave>",mousehoverLeave)
	backbutton.place(x=200,y=390)

	info = LabelFrame(fourthframe,text="Personal Information",font=("Century Gothic",10,"bold"),padx=4,pady=20,width=200,height=350)
	info.pack()

	service_number = Label(info, text="Enter Service Number: ",font=("Century Gothic",10)).grid(row=0)
	customer_name = Label(info, text="Enter Customer's Name: ",font=("Century Gothic",10)).grid(row=1)
	entry1 = Entry(info)
	entry1.grid(row=0, column=1)
	entry2 = Entry(info)
	entry2.grid(row=1, column=1)

	reading_info = LabelFrame(fourthframe,text="Reading Information",font=("Century Gothic",10,"bold"),padx=20,pady=20,width=200,height=350)
	reading_info.pack()
	month_reading = Label(reading_info, text="Enter month: ",font=("Century Gothic",10)).grid(row=2)
	old_reading = Label(reading_info, text="Enter old reading: ",font=("Century Gothic",10)).grid(row=3)
	new_reading = Label(reading_info, text="Enter new reading: ",font=("Century Gothic",10)).grid(row=4)
	readmonth = Entry(reading_info)
	readmonth.grid(row=2,column=1)
	read1 = Entry(reading_info)
	read1.grid(row=3, column=1)
	read2 = Entry(reading_info)
	read2.grid(row=4, column=1)
	def displayinfo(event):
		service_num = entry1.get()
		nameget = entry2.get()
		monthread = str(readmonth.get())
		oldread = read1.get()
		newread = read2.get()
		if (monthread.lower() not in listmonth):
			messagebox.showinfo("Error","Invalid Month")
			showFourthFrame()
		elif(service_num.isdigit()==False):
			messagebox.showinfo("Error","Service number must be a number")
			showFourthFrame()
		elif(oldread.isdigit()==False):
			messagebox.showinfo("Error","Reading must be a number")
			showFourthFrame()
		elif(newread.isdigit()==False):
			messagebox.showinfo("Error","Reading must be a number")
			showFourthFrame()
		else:
			total_consumption = round(float(float(newread) - float(oldread)),2)
			rate_amount = round((float(newread)/total_consumption),2)
			estbill = round((total_consumption*rate_amount),2)
			updateDictElect(monthread.lower(),estbill)
			readmonth.config(state="disabled")
			entry1.config(state="disabled")
			entry2.config(state="disabled")
			read1.config(state="disabled")
			read2.config(state="disabled")

			showbutton.pack(pady=3)
			showbutton.bind("<Enter>",showmousehoverEnter)
			showbutton.bind("<Leave>",showmousehoverLeave)
			showbutton.place(x=130,y=430)
			showbutton.configure(command =lambda: showTenthFrame(service_num,nameget,float(oldread),float(newread),total_consumption,estbill,"kWh"))

			consumption = Label(reading_info, text=total_consumption,font=("Century Gothic",10)).grid(row=5,column=1,sticky='W') 
			rate = Label(reading_info, text=rate_amount,font=("Century Gothic",10)).grid(row=6,column=1,sticky='W') 
			bill = Label(reading_info, text=estbill,font=("Century Gothic",10)).grid(row=7,column=1,sticky='W') 

	total_cons = Label(reading_info, text="Total Consumption: ",font=("Century Gothic",10)).grid(row=5)
	rkwh = Label(reading_info, text="Rate amount per kWh: ",font=("Century Gothic",10)).grid(row=6)
	total_price = Label(reading_info, text="Estimated bill per month : ",font=("Century Gothic",10)).grid(row=7)

	submitbutton.pack(pady=3)
	submitbutton.bind("<Enter>",smousehoverEnter)
	submitbutton.bind("<Leave>",smousehoverLeave)
	submitbutton.bind("<Button-1>",displayinfo)
	submitbutton.place(x=120,y=390)

#----------------------- FIFTH FRAME WIDGETS (Water) --------------------------------#
def showFifthFrame():
	initwindowsize("370x500")
	hideAllFrames()
	def mousehoverEnter(e):
		backbutton.config(bg='red',fg='white')
	def mousehoverLeave(e):
		backbutton.config(bg='white',fg='black')
	def smousehoverEnter(e):
		submitbutton.config(bg='green',fg='white')
	def smousehoverLeave(e):
		submitbutton.config(bg='white',fg='black')
	def showmousehoverEnter(e):
		showbutton.config(bg='blue',fg='white')
	def showmousehoverLeave(e):
		showbutton.config(bg='white',fg='black')


	fifthframe.pack(fill="both",expand=1)
	titleLabel = Label(fifthframe,text="Water Bill Calculator",pady=20)
	titleLabel.config(font=("Century Gothic",20,"bold"))
	titleLabel.pack()

	submitbutton = Button(fifthframe, text="Submit")
	submitbutton.config(font=("Century Gothic",10))

	showbutton = Button(fifthframe, text="Show Receipt")
	showbutton.config(font=("Century Gothic",10))

	backbutton = Button(fifthframe, text="Back",command=showThirdFrame)
	backbutton.config(font=("Century Gothic",10))
	backbutton.pack(pady=3)
	backbutton.bind("<Enter>",mousehoverEnter)
	backbutton.bind("<Leave>",mousehoverLeave)
	backbutton.place(x=200,y=390)

	info = LabelFrame(fifthframe,text="Personal Information",font=("Century Gothic",10,"bold"),padx=4,pady=20,width=200,height=350)
	info.pack()

	service_number = Label(info, text="Enter Service Number: ",font=("Century Gothic",10)).grid(row=0)
	customer_name = Label(info, text="Enter Customer's Name: ",font=("Century Gothic",10)).grid(row=1)
	entry1 = Entry(info)
	entry1.grid(row=0, column=1)
	entry2 = Entry(info)
	entry2.grid(row=1, column=1)

	reading_info = LabelFrame(fifthframe,text="Reading Information",font=("Century Gothic",10,"bold"),padx=20,pady=20,width=200,height=350)
	reading_info.pack()
	month_reading = Label(reading_info, text="Enter month: ",font=("Century Gothic",10)).grid(row=2)
	old_reading = Label(reading_info, text="Enter old reading: ",font=("Century Gothic",10)).grid(row=3)
	new_reading = Label(reading_info, text="Enter new reading: ",font=("Century Gothic",10)).grid(row=4)
	readmonth = Entry(reading_info)
	readmonth.grid(row=2,column=1)
	read1 = Entry(reading_info)
	read1.grid(row=3, column=1)
	read2 = Entry(reading_info)
	read2.grid(row=4, column=1)
	def displayinfo(event):
		nameget = entry2.get()
		service_num = entry1.get()
		monthread = str(readmonth.get())
		oldread = read1.get()
		newread = read2.get()
		if (monthread.lower() not in listmonth):
			messagebox.showinfo("Error","Invalid Month")
			showFourthFrame()
		elif(service_num.isdigit()==False):
			messagebox.showinfo("Error","Service number must be a number")
			showFourthFrame()
		elif(oldread.isdigit()==False):
			messagebox.showinfo("Error","Old Reading must be a number")
			showFourthFrame()
		elif(newread.isdigit()==False):
			messagebox.showinfo("Error","New Reading must be a number")
			showFourthFrame()
		else:
			total_consumption = round(float(float(newread) - float(oldread)),2)
			rate_amount = round((float(newread)/total_consumption),2)
			estbill = round((total_consumption*rate_amount),2)
			updateDictWater(monthread.lower(),estbill)
			readmonth.config(state="disabled")
			entry1.config(state="disabled")
			entry2.config(state="disabled")
			read1.config(state="disabled")
			read2.config(state="disabled")

			showbutton.pack(pady=3)
			showbutton.bind("<Enter>",showmousehoverEnter)
			showbutton.bind("<Leave>",showmousehoverLeave)
			showbutton.place(x=130,y=430)
			showbutton.configure(command =lambda: showTenthFrame(service_num,nameget,float(oldread),float(newread),total_consumption,estbill,"cu.m."))
			
			consumption = Label(reading_info, text=total_consumption,font=("Century Gothic",10)).grid(row=5,column=1,sticky='W') 
			rate = Label(reading_info, text=rate_amount,font=("Century Gothic",10)).grid(row=6,column=1,sticky='W') 
			bill = Label(reading_info, text=estbill,font=("Century Gothic",10)).grid(row=7,column=1,sticky='W') 

	total_cons = Label(reading_info, text="Total Consumption: ",font=("Century Gothic",10)).grid(row=5)
	rkwh = Label(reading_info, text="Rate amount per cu.m.: ",font=("Century Gothic",10)).grid(row=6)
	total_price = Label(reading_info, text="Estimated bill per month : ",font=("Century Gothic",10)).grid(row=7)

	submitbutton.pack(pady=3)
	submitbutton.bind("<Enter>",smousehoverEnter)
	submitbutton.bind("<Leave>",smousehoverLeave)
	submitbutton.bind("<Button-1>",displayinfo)
	submitbutton.place(x=120,y=390)

#----------------------- SIXTH FRAME WIDGETS (Display Track) --------------------------------#
def showSixthFrame():
	initwindowsize("300x400")
	root.title('Display Page')
	hideAllFrames()
	def mousehoverEnter(e):
		backbutton.config(bg='red',fg='white',font=("Century Gothic",10,"bold"))
	def mousehoverLeave(e):
		backbutton.config(bg='white',fg='black',font=("Century Gothic",10))
	def mousehoverEnterA(e):
		displayelectric.config(bg='green',fg='white',font=("Century Gothic",10,"bold"))
	def mousehoverLeaveA(e):
		displayelectric.config(bg='white',fg='black',font=("Century Gothic",10))
	def mousehoverEnterB(e):
		displaywater.config(bg='green',fg='white',font=("Century Gothic",10,"bold"))
	def mousehoverLeaveB(e):
		displaywater.config(bg='white',fg='black',font=("Century Gothic",10))

	sixthframe.pack(pady=40,padx=5)
	ttitleLabel = Label(sixthframe,text="Choose Below",pady=10)
	ttitleLabel.config(font=("Century Gothic",20,"bold"))
	ttitleLabel.pack()

	displayelectric = Button(sixthframe, text="Electricity",command=showSeventhFrame)
	displayelectric.config(font=("Century Gothic",10))
	displayelectric.pack(pady=3)
	displayelectric.bind("<Enter>",mousehoverEnterA)
	displayelectric.bind("<Leave>",mousehoverLeaveA)

	displaywater = Button(sixthframe, text="Water",command=showEightFrame)
	displaywater.config(font=("Century Gothic",10))
	displaywater.pack(pady=3)
	displaywater.bind("<Enter>",mousehoverEnterB)
	displaywater.bind("<Leave>",mousehoverLeaveB)

	backbutton = Button(sixthframe, text="Back",command=showSecondFrame)
	backbutton.config(font=("Century Gothic",10))
	backbutton.pack(pady=3)
	backbutton.bind("<Enter>",mousehoverEnter)
	backbutton.bind("<Leave>",mousehoverLeave)

#----------------------- SEVENTH FRAME WIDGETS (Show Electricity) --------------------------------#
def showSeventhFrame():
	initwindowsize("470x550")
	hideAllFrames()
	def mousehoverEnter(e):
		backbutton.config(bg='red',fg='white')
	def mousehoverLeave(e):
		backbutton.config(bg='white',fg='black')

	seventhframe.pack(fill="both",expand=1)
	titleLabel = Label(seventhframe,text="Electricity Bill Monthly Breakdown",pady=20)
	titleLabel.config(font=("Century Gothic",20,"bold"))
	titleLabel.pack()

	backbutton = Button(seventhframe, text="Back",command=showSixthFrame)
	backbutton.config(font=("Century Gothic",10))
	backbutton.pack(pady=3)
	backbutton.bind("<Enter>",mousehoverEnter)
	backbutton.bind("<Leave>",mousehoverLeave)
	backbutton.place(x=220,y=500)

	info = LabelFrame(seventhframe,text="Monthly Billing Breakdown",font=("Century Gothic",10,"bold"),padx=4,pady=20,width=200,height=350)
	info.pack()

	janreading = Label(info, text="January Bill Reading",font=("Century Gothic",12)).grid(row=0,sticky='W')
	febreading = Label(info, text="February Bill Reading",font=("Century Gothic",12)).grid(row=1,sticky='W')
	marreading = Label(info, text="March Bill Reading",font=("Century Gothic",12)).grid(row=2,sticky='W')
	aprilreading = Label(info, text="April Bill Reading",font=("Century Gothic",12)).grid(row=3,sticky='W')
	mayreading = Label(info, text="May Bill Reading",font=("Century Gothic",12)).grid(row=4,sticky='W')
	junereading = Label(info, text="June Bill Reading",font=("Century Gothic",12)).grid(row=5,sticky='W')
	julyreading = Label(info, text="July Bill Reading",font=("Century Gothic",12)).grid(row=6,sticky='W')
	augreading = Label(info, text="August Bill Reading",font=("Century Gothic",12)).grid(row=7,sticky='W')
	sepreading = Label(info, text="September Bill Reading",font=("Century Gothic",12)).grid(row=8,sticky='W')
	octreading = Label(info, text="October Bill Reading",font=("Century Gothic",12)).grid(row=9,sticky='W')
	novreading = Label(info, text="November Bill Reading",font=("Century Gothic",12)).grid(row=10,sticky='W')
	decreading = Label(info, text="December Bill Reading",font=("Century Gothic",12)).grid(row=11,sticky='W')

	janreadings = Label(info, text=">> {:} pesos".format(electrack["january"]),font=("Century Gothic",12)).grid(row=0,column=1,sticky='W')
	febreadings = Label(info, text=">> {:} pesos".format(electrack["february"]),font=("Century Gothic",12)).grid(row=1,column=1,sticky='W')
	marreadings = Label(info, text=">> {:} pesos".format(electrack["march"]),font=("Century Gothic",12)).grid(row=2,column=1,sticky='W')
	aprilreadings = Label(info, text=">> {:} pesos".format(electrack["april"]),font=("Century Gothic",12)).grid(row=3,column=1,sticky='W')
	mayreadings = Label(info, text=">> {:} pesos".format(electrack["may"]),font=("Century Gothic",12)).grid(row=4,column=1,sticky='W')
	junereadings = Label(info, text=">> {:} pesos".format(electrack["june"]),font=("Century Gothic",12)).grid(row=5,column=1,sticky='W')
	julyreadings = Label(info, text=">> {:} pesos".format(electrack["july"]),font=("Century Gothic",12)).grid(row=6,column=1,sticky='W')
	augreadings = Label(info, text=">> {:} pesos".format(electrack["august"]),font=("Century Gothic",12)).grid(row=7,column=1,sticky='W')
	sepreadings = Label(info, text=">> {:} pesos".format(electrack["september"]),font=("Century Gothic",12)).grid(row=8,column=1,sticky='W')
	octreadings = Label(info, text=">> {:} pesos".format(electrack["october"]),font=("Century Gothic",12)).grid(row=9,column=1,sticky='W')
	novreadings = Label(info, text=">> {:} pesos".format(electrack["november"]),font=("Century Gothic",12)).grid(row=10,column=1,sticky='W')
	decreadings = Label(info, text=">> {:} pesos".format(electrack["december"]),font=("Century Gothic",12)).grid(row=11,column=1,sticky='W')

#----------------------- EIGHT FRAME WIDGETS --------------------------------#
def showEightFrame():
	initwindowsize("470x550")
	hideAllFrames()
	def mousehoverEnter(e):
		backbutton.config(bg='red',fg='white')
	def mousehoverLeave(e):
		backbutton.config(bg='white',fg='black')

	eightframe.pack(fill="both",expand=1)
	titleLabel = Label(eightframe,text="Water Bill Monthly Breakdown",pady=20)
	titleLabel.config(font=("Century Gothic",20,"bold"))
	titleLabel.pack()

	backbutton = Button(eightframe, text="Back",command=showSixthFrame)
	backbutton.config(font=("Century Gothic",10))
	backbutton.pack(pady=3)
	backbutton.bind("<Enter>",mousehoverEnter)
	backbutton.bind("<Leave>",mousehoverLeave)
	backbutton.place(x=220,y=500)

	info = LabelFrame(eightframe,text="Monthly Billing Breakdown",font=("Century Gothic",10,"bold"),padx=4,pady=20,width=200,height=350)
	info.pack()

	janreading = Label(info, text="January Bill Reading",font=("Century Gothic",12)).grid(row=0,sticky='W')
	febreading = Label(info, text="February Bill Reading",font=("Century Gothic",12)).grid(row=1,sticky='W')
	marreading = Label(info, text="March Bill Reading",font=("Century Gothic",12)).grid(row=2,sticky='W')
	aprilreading = Label(info, text="April Bill Reading",font=("Century Gothic",12)).grid(row=3,sticky='W')
	mayreading = Label(info, text="May Bill Reading",font=("Century Gothic",12)).grid(row=4,sticky='W')
	junereading = Label(info, text="June Bill Reading",font=("Century Gothic",12)).grid(row=5,sticky='W')
	julyreading = Label(info, text="July Bill Reading",font=("Century Gothic",12)).grid(row=6,sticky='W')
	augreading = Label(info, text="August Bill Reading",font=("Century Gothic",12)).grid(row=7,sticky='W')
	sepreading = Label(info, text="September Bill Reading",font=("Century Gothic",12)).grid(row=8,sticky='W')
	octreading = Label(info, text="October Bill Reading",font=("Century Gothic",12)).grid(row=9,sticky='W')
	novreading = Label(info, text="November Bill Reading",font=("Century Gothic",12)).grid(row=10,sticky='W')
	decreading = Label(info, text="December Bill Reading",font=("Century Gothic",12)).grid(row=11,sticky='W')

	janreadings = Label(info, text=">> {:} pesos".format(watertrack["january"]),font=("Century Gothic",12)).grid(row=0,column=1,sticky='W')
	febreadings = Label(info, text=">> {:} pesos".format(watertrack["february"]),font=("Century Gothic",12)).grid(row=1,column=1,sticky='W')
	marreadings = Label(info, text=">> {:} pesos".format(watertrack["march"]),font=("Century Gothic",12)).grid(row=2,column=1,sticky='W')
	aprilreadings = Label(info, text=">> {:} pesos".format(watertrack["april"]),font=("Century Gothic",12)).grid(row=3,column=1,sticky='W')
	mayreadings = Label(info, text=">> {:} pesos".format(watertrack["may"]),font=("Century Gothic",12)).grid(row=4,column=1,sticky='W')
	junereadings = Label(info, text=">> {:} pesos".format(watertrack["june"]),font=("Century Gothic",12)).grid(row=5,column=1,sticky='W')
	julyreadings = Label(info, text=">> {:} pesos".format(watertrack["july"]),font=("Century Gothic",12)).grid(row=6,column=1,sticky='W')
	augreadings = Label(info, text=">> {:} pesos".format(watertrack["august"]),font=("Century Gothic",12)).grid(row=7,column=1,sticky='W')
	sepreadings = Label(info, text=">> {:} pesos".format(watertrack["september"]),font=("Century Gothic",12)).grid(row=8,column=1,sticky='W')
	octreadings = Label(info, text=">> {:} pesos".format(watertrack["october"]),font=("Century Gothic",12)).grid(row=9,column=1,sticky='W')
	novreadings = Label(info, text=">> {:} pesos".format(watertrack["november"]),font=("Century Gothic",12)).grid(row=10,column=1,sticky='W')
	decreadings = Label(info, text=">> {:} pesos".format(watertrack["december"]),font=("Century Gothic",12)).grid(row=11,column=1,sticky='W')

#----------------------- NINTH FRAME WIDGETS (Water Choice) --------------------------------#
def showNinthFrame():
	initwindowsize("300x400")
	hideAllFrames()
	def mousehoverEnter(e):
		backbutton.config(bg='red',fg='white',font=("Century Gothic",10,"bold"))
	def mousehoverLeave(e):
		backbutton.config(bg='white',fg='black',font=("Century Gothic",10))
	def mousehoverEnterA(e):
		displayelectric.config(bg='green',fg='white',font=("Century Gothic",10,"bold"))
	def mousehoverLeaveA(e):
		displayelectric.config(bg='white',fg='black',font=("Century Gothic",10))
	def mousehoverEnterB(e):
		displaywater.config(bg='green',fg='white',font=("Century Gothic",10,"bold"))
	def mousehoverLeaveB(e):
		displaywater.config(bg='white',fg='black',font=("Century Gothic",10))

	ninthframe.pack(pady=40,padx=5)
	ttitleLabel = Label(ninthframe,text="Choose Below",pady=10)
	ttitleLabel.config(font=("Century Gothic",20,"bold"))
	ttitleLabel.pack()

	displayelectric = Button(ninthframe, text="Own Meter",command=showFifthFrame)
	displayelectric.config(font=("Century Gothic",10))
	displayelectric.pack(pady=3)
	displayelectric.bind("<Enter>",mousehoverEnterA)
	displayelectric.bind("<Leave>",mousehoverLeaveA)

	displaywater = Button(ninthframe, text="Submeter",command=showFifthFrame)
	displaywater.config(font=("Century Gothic",10))
	displaywater.pack(pady=3)
	displaywater.bind("<Enter>",mousehoverEnterB)
	displaywater.bind("<Leave>",mousehoverLeaveB)

	backbutton = Button(ninthframe, text="Back",command=showSecondFrame)
	backbutton.config(font=("Century Gothic",10))
	backbutton.pack(pady=3)
	backbutton.bind("<Enter>",mousehoverEnter)
	backbutton.bind("<Leave>",mousehoverLeave)

#-----------------------TENTH FRAME WIDGETS (receipt)--------------------------------#
def showTenthFrame(servicenumber,name,old,new,total,estimatedbill,unit):
	initwindowsize("470x550")
	hideAllFrames()
	def mousehoverEnter(e):
		backbutton.config(bg='green',fg='white')
	def mousehoverLeave(e):
		backbutton.config(bg='white',fg='black')

	tenthframe.pack(fill="both",expand=1)

	titleLabel2 = Label(tenthframe,text="     UTILITY TRACKER",pady=50)
	titleLabel2.config(font=("Century Gothic",20,"bold"))
	titleLabel2.place(x=200,y=40)
	titleLabel2.pack()
	
	titleLabel = Label(tenthframe,text="------------------- Receipt ------------------",pady=20)
	titleLabel.config(font=("Century Gothic",15,"bold"))
	titleLabel.pack()

	backbutton = Button(tenthframe, text="Back to Main Menu",command=showSecondFrame)
	backbutton.config(font=("Century Gothic",10))
	backbutton.pack(pady=3)
	backbutton.bind("<Enter>",mousehoverEnter)
	backbutton.bind("<Leave>",mousehoverLeave) #x=165
	backbutton.place(x=165,y=450)

	info = LabelFrame(tenthframe,text="",padx=4)
	info.pack()

	sernumber = Label(info, text="Service Number",font=("Century Gothic",11)).grid(row=0,sticky='W')
	custname = Label(info, text="Name of Customer",font=("Century Gothic",11)).grid(row=1,sticky='W')
	oreading = Label(info, text="Old Reading",font=("Century Gothic",12)).grid(row=2,sticky='W')
	nreading = Label(info, text="New Reading",font=("Century Gothic",12)).grid(row=3,sticky='W')
	tconsump = Label(info, text="Total Consumption",font=("Century Gothic",12)).grid(row=4,sticky='W')
	estimatebill = Label(info, text="Estimated Bill for the month",font=("Century Gothic",12)).grid(row=5,sticky='W')

	sernumbers = Label(info, text=": {:}".format(servicenumber),font=("Century Gothic",12)).grid(row=0,column=1,sticky='W')
	custnames = Label(info, text=": {:}".format(name),font=("Century Gothic",12)).grid(row=1,column=1,sticky='W')
	oreadings = Label(info, text=": {:.2f}".format(old),font=("Century Gothic",12)).grid(row=2,column=1,sticky='W')
	nreadings = Label(info, text=": {:.2f}".format(new),font=("Century Gothic",12)).grid(row=3,column=1,sticky='W')
	tconsumps = Label(info, text=": {:.2f} {:}".format(total,unit),font=("Century Gothic",12)).grid(row=4,column=1,sticky='W')
	estimatebills = Label(info, text=": {:.2f} pesos".format(estimatedbill),font=("Century Gothic",12)).grid(row=5,column=1,sticky='W')
	
	title1Label = Label(tenthframe,text="----------------------------------------------",pady=10)
	title1Label.config(font=("Century Gothic",15,"bold"))
	title1Label.place(y=400, anchor="center")
	title1Label.pack()

	load = Image.open("logo.png")
	load = load.resize((105,102),Image.ANTIALIAS)
	render = ImageTk.PhotoImage(load)
	img = Label(tenthframe,image = render)
	img.image = render
	img.place(x=40,y=25)

#--------------------- INIT FRAMES -----------------------------------------------#
mainframe = Frame(root,padx=7,pady=60) #Main
secondframe = Frame(root,padx=7,pady=40) # Main Menu
thirdframe = Frame(root,padx=7,pady=40)  # Consumption
fourthframe = Frame(root,width=370,height=500) # Electricity
fifthframe = Frame(root,width=370,height=500) # Water (with meter)
sixthframe = Frame(root,padx=7,pady=40)  # Display
seventhframe = Frame(root,width=470,height=550) # Electricity Display
eightframe = Frame(root,width=470,height=550) # Water Display
ninthframe = Frame(root,padx=7,pady=40) # Water Choice
tenthframe = Frame(root,width=470,height=550) # Receipt
#----------------------- TEST AREA ------------------------------------------#
showMainFrame()
root.mainloop()