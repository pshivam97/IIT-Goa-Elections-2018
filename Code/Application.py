import Tkinter as tk
import ttk,pickle,os,os.path
from PIL import Image
from PIL import ImageTk
import string,re, libraries
import random,sys
import smtplib
import base64


pass1 = "elections" #for email
passcode1 = "abhishek" #to restart
passcode2 = "bypass" #for email bypass check

class Candidate(object) :

	def __init__(self,name,imgpath) :
		self.name = name
		self.img = Image.open(imgpath).resize((150, 200), Image.ANTIALIAS)

class Application(tk.Tk) :
	def __init__(self,*args,**kwargs) :
		tk.Tk.__init__(self, *args, **kwargs)
		self.build_panes("GSec. Academics")

		w = 820 # width for the Tk root
		h = 680 # height for the Tk root

		# get screen width and height
		ws = self.winfo_screenwidth() # width of the screen
		hs = self.winfo_screenheight() # height of the screen

		# calculate x and y coordinates for the Tk root window
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)

		# set the dimensions of the screen
		# and where it is placed
		self.geometry('%dx%d+%d+%d' % (w, h, x, y))



	def build_panes(self,post) :
		print "building"
		self.Position = Positions_pane(self)
		self.selection = Selection_pane(self,post)
		self.Position.grid(row=0,column=0,sticky = tk.N+tk.W +tk.E +tk.S)
		self.selection.grid(row=0,column=1)


	def cast_vote(self,post,name) :
		curr_list[post]= name
		self.update_panes(post)

	def update_panes(self,post) :
		self.Position.destroy()
		self.selection.destroy()
		self.build_panes(post)

	def bye(self):
		self.destroy()


class Positions_pane(tk.Frame) :

	def __init__(self,parent) :
		self.color_scheme = ["#B7E3CC","#B7E3CC","#FEF9FF"] #background,label_background,text
		tk.Frame.__init__(self,parent,relief = tk.RAISED,bd = 3,bg = self.color_scheme[0])
		self.parent = parent
		logo = Image.open("Images/logo.jpg")
		logo = logo.resize((185,170), Image.ANTIALIAS)
		logo= ImageTk.PhotoImage(logo)
		logo_label = ttk.Label(self,image=logo,background = self.color_scheme[2])
		logo_label.image = logo
		logo_label.grid(row=0,column=0)
		temp = 2
		ttk.Label(self, text="Posts",width=12, anchor="center", wraplength=290, font=("Roboto", 18),background = "#470024", foreground=self.color_scheme[2],borderwidth=5).grid(row=1,column=0,sticky = tk.N)
		for i in curr_list :
			print i,"=------------------"
			if i == "BR-CSE" and branch != "CS":
				continue
			elif i == "BR-Electrical" and branch != "ELEC":
				continue
			elif i == "BR-Mechanical" and branch != "MECH":
				continue


			if curr_list[i]!= None :
				color =  "#06D6A0"
				text_col = "#022F40"
			else :
				color = "#1D3557"
				text_col = self.color_scheme[2]
			butt = tk.Button(self,text=i,command = lambda i=i : parent.update_panes(i))
			butt.grid(column=0,row=temp,sticky=tk.N+tk.S+tk.E+tk.W)
			butt.config(background = color,foreground=text_col, activebackground="pink")
			temp += 1

		b = tk.Button(self, command=self.parent.bye , text="Submit", background = "#563440",foreground="#D7DEDC").grid(row = temp,column = 0,pady=10)



class Selection_pane(tk.Frame) :

	def __init__(self,parent,post) :
		self.color_scheme = ["#7B4B94","#7B4B94","#F2DFD7"] #background,label_background,text
		tk.Frame.__init__(self,parent,relief = tk.GROOVE,bd = 3,bg=self.color_scheme[0])
		self.initialise(post)
		self.parent = parent

	def initialise(self,post) :
		tk.Label(self,text="=- " + str(post) + " -=",font=("Times", 24),bg=self.color_scheme[1],fg=self.color_scheme[2]).grid(column=0,row=0,columnspan = 2)
		if curr_list[post]!= None :
			print "Name"
			tk.Label(self,text=curr_list[post],font=("Times", 24),bg=self.color_scheme[1]).grid(column=0,row=1,columnspan = 2)
			his_image = Image.open("Candidates/" + post + "/" + curr_list[post]+".jpg")
			his_image = his_image.resize((140, 165), Image.ANTIALIAS)
			his_image = ImageTk.PhotoImage(his_image)
		else :
			print "No name"

			his_image = Image.open("Images/x.jpg")
			his_image = his_image.resize((140, 165), Image.ANTIALIAS)
			his_image = ImageTk.PhotoImage(his_image)

		select = tk.Label(self,image=his_image,bg=self.color_scheme[1])
		select.image=his_image
		select.grid(row=0,column = 2,rowspan = 2,columnspan=2,pady = 3)


		temp =0
		for i in applicants[post] :
			print "Candidates/" + post + "/" + i + ".jpg"
			person_image = Image.open("Candidates/" + post + "/" + i + ".jpg")
			person_image = person_image.resize((200, 245), Image.ANTIALIAS)
			person_image = ImageTk.PhotoImage(person_image)
			person_button = tk.Button(self, image=person_image, background=self.color_scheme[1], command=lambda i=i,post=post : self.parent.cast_vote(post,i) )
			person_button.image = person_image
			person_button.grid(row = 3+temp/3, column = temp%3)
			temp += 1

		while (temp<6) :
			person_image = Image.open("Images/nopicture-male.jpg")
			person_image = person_image.resize((200, 245), Image.ANTIALIAS)
			person_image = ImageTk.PhotoImage(person_image)
			person_button = tk.Button(self, image = person_image,background="black", command=lambda i=None,post=post : self.parent.cast_vote(post,i) )
			person_button.image = person_image
			person_button.grid(row=3+temp/3,column=temp%3)
			temp += 1

class Multi_box(object) :
	def __init__(self,disp_text,show = "") :
		self.text = ""
		self.root = tk.Tk()
		self.root.title("Elections IITGoa 2018")
		self.root.configure(background="#B7E3CC")
		w = 600
		h = 400
		ws = self.root.winfo_screenwidth()
		hs = self.root.winfo_screenheight()
		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)
		self.root.geometry('%dx%d+%d+%d' % (w, h, x, y))
		banner = ttk.Label(self.root, text= "  IIT Goa Elections 2018  ")
		banner.config(font=("Times", 44),background = "#7B4B94",foreground="#FEF9FF")
		banner.pack()
		ttk.Label(self.root,text= disp_text,background="#B7E3CC",foreground="#140F2D",font=("Times",15)).pack(pady=50)
		self.e = tk.Entry(self.root,show=show, width= 35)
		self.e.pack()
		self.e.focus_set()
		b = tk.Button(self.root,command=self.submit,text = "  Submit  ")
		b.config(background="#00072D",foreground = "#FEF9FF")
		b.pack()
		self.root.mainloop()

	def submit(self) :
		global email
		self.text =  self.e.get()
		self.root.destroy()
		return


votes = dict()
posts = next(os.walk('./Candidates'))[1] # [Gsec Academics , Gsec Cultural, Gsec Sports]

for each_post in posts :
    votes[each_post] = dict()
    persons = []

    for person in os.listdir('./Candidates/' + str(each_post)) :
        if person == '.DS_Store' :
            continue

        name_of_person = os.path.splitext(os.path.basename(str(person)))[0]
        persons.append(name_of_person)

    for each_name in persons :
        votes[each_post][each_name] = 0

	votes[each_post][None] = 0

applicants = dict()


for post in votes:
	temp = []
	for applicant_name in votes[post] :
		if applicant_name != None :
			temp.append(applicant_name)
	applicants[post] = temp


smtp_server = smtplib.SMTP('smtp.gmail.com',587)
smtp_server.ehlo()
smtp_server.starttls()

# For security reasons the actual email address and password used have been removed. You can add your own email address and password here
smtp_server.login('electionsiitgoa2018@gmail.com',"password-removed")

for i in range(170) :
	curr_list = {}

#------------------------Login Checks -------------------------------------------
	restart = True
	while (restart) :

		restart = False
		while (True) :
			email = Multi_box("Enter your proper IIT Goa mail id to continue")
			email = email.text.strip()
			if email == "quit" :
				quit()
			elif "elections" in email :
				break
			delimiter = '@|\.'
			email_check = re.split(delimiter,email)
			print email_check
			if (len(email_check) != 6 and pass1 not in email ) :
				continue
			if not (email_check[3] == 'iitgoa' and email_check[4] == 'ac' and email_check[5]=='in') :
				continue
			if not(len(email_check[2]) == 5 and libraries.get_verification(email,sys.argv[1],sys.argv[2])) :#email in done_mail :
				continue
			break
		print email
		if pass1 in email :
			branch = email.strip(pass1)
			content = passcode2
		else :
			branch = email_check[2]
			if branch[4] == "1" :
				branch = "CS"
			elif branch[4] =="2" :
				branch ="ELEC"
			elif branch[4] == "3" :
				branch = "MECH"
			content = str(random.randint(100000,1000000))
			smtp_server.sendmail('electionsiitgoa2018@gmail.com',email,"Indian Institute of Technology Goa, Student Council Elections 2018\n\n--- Your One time passcode is : " + content)

		if branch not in ["CS","ELEC","MECH"] :
			restart = True
		print branch


		while (True) :
			passcode = Multi_box("Enter the passcode sent to you IIT Goa Mail ID",show = "*")
			passcode = passcode.text.strip()
			if passcode == content :
				break
			elif passcode == "restart" :
				restart = True
				break
#======================================================================================

	for j in votes :
		curr_list[j] = None

	app = Application()
	app.mainloop()

	print curr_list

	for post_of_voted_person, voted_person in curr_list.items() :
		votes[post_of_voted_person][voted_person] += 1 #Votes Dictionary updation

	with open("Updated_Results.elc",'wb') as file_out :
		pickle.dump(votes,file_out)

	try :
		with open(".electionresult","a") as file_out :
			for i in curr_list :
				file_out.write(i+":"+str(curr_list[i])+",")
			file_out.write("\n")
	except :
		with open(".electionresult","w") as file_out :
			for i in curr_list :
				file_out.write(i+":"+str(curr_list[i])+",")
			file_out.write("\n")


	while(True) :
		passme = Multi_box("Thank you For Voting.\nSoftware developed by Abhishek Varghese & Shivam Pandey.\n\nEnter Admin Passcode to continue -",show = "*")
		passme = passme.text
		if passme == "string" :
			break
		elif passme == "electionsquit" :
			quit()

smtp_server.close()
