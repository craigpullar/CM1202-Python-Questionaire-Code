from Tkinter import *
import tkMessageBox
from tkFileDialog import askopenfilename
import pickle
import cPickle
import shelve
import tempfile
import win32api
import win32print

#//\\//\\//\\//\\/#
#APPLICATION CLASS#
#//\\//\\//\\//\\/#
class Application(Frame):

    #Intialize application
    def __init__(self, master): #constructor.
        Frame.__init__(self, master)
        self.grid() #start grid
        self.updateScreen = 0 #create variable to keep track of screen currently displayed
        self.setCurrentScreen(0)
        self.screen = [splashScreen(self), loginScreen(self),
                       practiceTestQuestion(self),practiceResults(self),
                       testQuestionOne(self),testQuestionTwo(self),
                       testQuestionThree(self),testQuestionFour(self),
                       testQuestionFive(self),testResults(self)]
        #list of screen classes
        self.screen[self.currentScreen].draw() #draw the current screen
        

    #Set current screen
    @staticmethod
    def setCurrentScreen(input):
        Application.currentScreen = input

    #Update the display with current screen
    def updateFrame(self):
        if self.currentScreen != self.updateScreen:
            self.screen[self.currentScreen].draw()
            self.updateScreen = self.currentScreen
        self.after(10,self.updateFrame)#RESCHEDULE FUNCTION


#//\\//\\//\\//\\//#
#SPLASHSCREEN CLASS#
#//\\//\\//\\//\\//#
class splashScreen(Frame):

    #Initialize frame
    def __init__(self, master): #constructor.
        Frame.__init__(self, master)


    #Draw frame contents
    def draw(self):
        self.grid()
        self.grid_columnconfigure(index = 1,minsize=(self.winfo_screenwidth()))
        self.grid_rowconfigure(index = 1, minsize =(self.winfo_screenheight()/2))
        self.beginButton()
        self.heading()
        self.configure(bg ='blue')

    #Declare heading
    def heading(self):
        lblHeading = Label (self, text = "Welcome to the Aptitude Test", font =("ARIAL", 30, "bold"))
        lblHeading.grid (row = 1, column = 0, columnspan=2, sticky = W+E+N+S )
        lblHeading.configure(background='blue', fg = 'white')


    #Declare button
    def beginButton(self):  #practice button
        practiceButton = Button(self, text = "Begin", font = ("ARIAL", 20, "bold"))
        practiceButton["command"] = self.begin #when button clicked will call "practiceTest" method. Rename if you want.
        practiceButton.grid(row = 2, column = 1, sticky = N+S)
        practiceButton.configure(bg='white', fg='blue')

    #Clear the screen
    def clearScreen(self):
        self.grid_forget()

    #Navigate to LoginScreen
    def begin(self):
        Application.setCurrentScreen(1)
        self.clearScreen()


#//\\//\\//\\//\\/#
#LOGINSCREEN CLASS#
#//\\//\\//\\//\\/#
class loginScreen(Frame):

    #Intialize frame
    def __init__(self, root): #constructor.
        Frame.__init__(self, root)

    #Draw frame contents
    def draw(self):
        self.grid()
        self.grid_columnconfigure(index = 1,minsize=(self.winfo_screenwidth()/2))
        self.grid_rowconfigure(index = 1, minsize =(self.winfo_screenheight()/3))
        self.heading()
        self.loginDetails()
        self.practiceQuestionButton()
        self.testButton()
        self.configure(bg="blue")

    #Declare heading
    def heading(self):
        lblHeading = Label (self, text = "Details", font =("ARIAL", 30, "bold"))
        lblHeading.grid (row = 1, column = 0,columnspan=2, sticky = E+N+S)
        lblHeading.configure(bg='blue',fg='white')

    #Declare practice test button
    def practiceQuestionButton(self):  #practice button
        practiceButton = Button(self, text = "Practice Test", font = ("Arail", 8, "bold"))
        practiceButton["command"] = self.practiceTest #when button clicked will call "practiceTest" method. Rename if you want.
        practiceButton.grid(row = 10, column = 6, columnspan=6,padx=10)
        practiceButton.configure(fg='blue', bg='white')

    #Clear screen
    def clearScreen(self):
        self.grid_forget()

    #Navigate to practice test
    def practiceTest(self):
        Application.setCurrentScreen(2)
        self.clearScreen()

    #Declare test button
    def testButton(self):
        testButton = Button(self, text = "Test", font = ("Arial", 8, "bold"))
        testButton["command"] = self.test #when button clicked will call "Test" method. Rename if you want.
        testButton.grid(row = 4, column = 6, columnspan = 5)
        testButton.configure(fg='blue', bg='white')

    #Declare login details
    def loginDetails(self):
        lblFirstName = Label(self, text = "First Name:", font =("MS", 12, "bold"))
        lblFirstName.grid(row = 2, column = 1,sticky = N+S)
        lblFirstName.configure(fg='white',bg='blue')
        self.EnterFirstName = Entry(self)
        self.EnterFirstName.grid (row = 2, column = 2)

        lblSurname = Label(self, text = "Surname:", font =("MS", 12, "bold"))
        lblSurname.grid(row = 4, column = 1)
        lblSurname.configure(bg='blue',fg='white')
        self.EnterSurname = Entry(self)
        self.EnterSurname.grid(row = 4, column = 2)

        lblStudentNo = Label(self, text = "Student No:", font =("MS", 12, "bold"))
        lblStudentNo.grid(row = 6, column = 1)
        lblStudentNo.configure(bg='blue',fg='white')
        self.EnterStudentNo = Entry (self)
        self.EnterStudentNo.grid(row = 6, column = 2)

        lblYearOfStudy = Label(self, text = "Year of study:", font =("MS", 12, "bold"))
        lblYearOfStudy.grid(row = 8, column = 1)
        lblYearOfStudy.configure(bg='blue',fg='white')
        self.EnterYearOfStudy = Entry (self)
        self.EnterYearOfStudy.grid(row = 8, column = 2)

        lblDOB = Label(self, text = "Date of Birth:", font =("MS", 12, "bold"))
        lblDOB.grid(row = 10, column = 1)
        lblDOB.configure(bg='blue',fg='white')
        self.EnterDOB = Entry(self)
        self.EnterDOB.grid(row = 10, column = 2)

    #Navigate to test
    def test(self):
        #stores user details.
        firstName = self.EnterFirstName.get()
        surname = self.EnterSurname.get()
        studentNo = self.EnterStudentNo.get()
        year = self.EnterYearOfStudy.get()
        DOB = self.EnterDOB.get()
        if (firstName == "") or (surname == "") or (studentNo =="") or (year == "") or (DOB == ""):
            tkMessageBox.showinfo("Login Details", "Please fill in all your details.")
        else:
            details = open ("details.txt", "w")
            details.write(firstName +'\n' + surname + '\n' +
                      studentNo + '\n' + year + '\n' + DOB)
            details.close()
            Application.setCurrentScreen(4)
            self.clearScreen()


#//\\//\\//\\//\\//\\//\#
#PRACTICE QUESTION CLASS#
#//\\//\\//\\//\\//\\//\#
class practiceTestQuestion(Frame):

    #Initialize frame
    def __init__(self, master): #constructor
        Frame.__init__(self, master)

    #Draw frame contents
    def draw(self):
        self.grid()
        self.heading()
        self.questionAndAnswer()
        self.submitButton()
        self.configure(bg='blue')
        self.grid_columnconfigure(index = 1,minsize=(self.winfo_screenwidth()/2))
        self.grid_rowconfigure(index = 1, minsize =(self.winfo_screenheight()/3))

    #Declare heading
    def heading(self):
        lblHeading = Label (self, text = "Practice Question", font =("ARIAL", 20, "bold"))
        lblHeading.grid (row = 1, column = 1,columnspan=5, sticky= W+E+N+S)
        lblHeading.configure(bg='blue', fg='white')

        lblQuestion = Label (self, text = "Identify the missing number at the end of the series.", font =("ARIAL", 12, "bold"))
        lblQuestion.grid (row = 1, column = 1,columnspan=5, sticky = W+E+S)
        lblQuestion.configure(bg='blue',fg='white')

    #Declare questions
    def questionAndAnswer(self):
        self.one = IntVar()
        self.two = IntVar()
        self.three = IntVar()

        #question 1
        lblQuestion1 = Label (self, text = "1)	3, 11, 19, 27, ?", font = ("ARIAL", 10))
        lblQuestion1.grid(row = 4, column = 0, sticky = W,padx=50)
        lblQuestion1.configure(bg='blue',fg='white')

        #radio buttons
        R1Q1 = Radiobutton(self, text = "33", variable=self.one, value=33)
        R1Q1.grid(row=4, column= 2)
        R1Q1.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R2Q1 = Radiobutton(self, text = "35", variable=self.one, value=35)
        R2Q1.grid(row=4, column= 3)
        R2Q1.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R3Q1 = Radiobutton(self, text = "37", variable=self.one, value=37)
        R3Q1.grid(row=4, column= 4)
        R3Q1.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R4Q1 = Radiobutton(self, text = "39", variable=self.one, value=39)
        R4Q1.grid(row=4, column= 5)
        R4Q1.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R5Q1 = Radiobutton(self, text = "41", variable=self.one, value=41)
        R5Q1.grid(row=4, column= 6)
        R5Q1.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')

        #question 2
        lblQuestion2 = Label (self, text = "2)	3, 6, 11, 18, ?", font = ("ARIAL", 10))
        lblQuestion2.grid(row = 6, column = 0, sticky = W,padx=50)
        lblQuestion2.configure(bg='blue',fg='white')

        #radio buttons
        R1Q2 = Radiobutton(self, text = "24", variable=self.two, value=24)
        R1Q2.grid(row=6, column= 2)
        R1Q2.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R2Q2 = Radiobutton(self, text = "25", variable=self.two, value=25)
        R2Q2.grid(row=6, column= 3)
        R2Q2.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R3Q2 = Radiobutton(self, text = "26", variable=self.two, value=26)
        R3Q2.grid(row=6, column= 4)
        R3Q2.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R4Q2 = Radiobutton(self, text = "27", variable=self.two, value=27)
        R4Q2.grid(row=6, column= 5)
        R4Q2.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R5Q2 = Radiobutton(self, text = "28", variable=self.two, value=28)
        R5Q2.grid(row=6, column= 6)
        R5Q2.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')

        #question 3
        lblQuestion3 = Label (self, text = "3)	516, 497, 478, 459, ?", font = ("ARIAL", 10))
        lblQuestion3.grid(row = 8, column = 0, sticky = E,padx=50)
        lblQuestion3.configure(bg='blue',fg='white')

        #radio buttons
        R1Q3 = Radiobutton(self, text = "436", variable=self.three, value=436)
        R1Q3.grid(row=8, column= 2)
        R1Q3.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R2Q3 = Radiobutton(self, text = "440", variable=self.three, value=440)
        R2Q3.grid(row=8, column= 3)
        R2Q3.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R3Q3 = Radiobutton(self, text = "438", variable=self.three, value=438)
        R3Q3.grid(row=8, column= 4)
        R3Q3.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R4Q3 = Radiobutton(self, text = "452", variable=self.three, value=452)
        R4Q3.grid(row=8, column= 5)
        R4Q3.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R5Q3= Radiobutton(self, text = "442", variable=self.three, value=442)
        R5Q3.grid(row=8, column= 6)
        R5Q3.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')

    #Declare submit button
    def submitButton(self):
        butSubmit = Button(self, text='Submit',font=('ARIAL', 8,'bold'))
        butSubmit['command']=self.storeAnswers
        butSubmit.grid(row=18, column=12, columnspan=2)
        butSubmit.configure(bg='white', fg='blue')

    #Clear screen
    def clearScreen(self):
        self.grid_forget()

    #Store answers
    def storeAnswers(self):
        score = 0
        q1 = self.one.get()
        q2 = self.two.get()
        q3 = self.three.get()
        if (q1 == 0) or (q2 == 0) or (q3 == 0):
            tkMessageBox.showinfo("Practice Question", "Please answer every question")
        else:
            if q1 == 35:
                score += 1
            if q2 == 27:
                score += 1
            if q3 == 440:
                score += 1
            percentage = (score/3.0 *100)
            percentage = "%.2f" % percentage

            practice_answers = open("practiceAnswers.txt", "w")

            cPickle.dump(q3, practice_answers)
            cPickle.dump(q2, practice_answers)
            cPickle.dump(q1, practice_answers)
            cPickle.dump(score, practice_answers)
            cPickle.dump(percentage, practice_answers)
            tkMessageBox.showinfo("Practice Question", "Answers Submitted")
            practice_answers.close()
            Application.setCurrentScreen(3)
            self.clearScreen()


#//\\//\\//\\//\\//\\//#
#PRACTICE RESULTS CLASS#
#//\\//\\//\\//\\//\\//#
class practiceResults(Frame):

    #Initialize frame
    def __init__(self, master):
        Frame.__init__(self,master)

    #Draw frame content
    def draw(self):
        self.grid()
        self.returnButton()
        self.pickleResults()
        self.pageLayout()
        self.configure(bg='blue')
        self.grid_columnconfigure(index = 1,minsize=(self.winfo_screenwidth()/2))
        self.grid_rowconfigure(index = 1, minsize =(self.winfo_screenheight()/6))

    def pageLayout(self):
        lblHeading= Label (self, text = "Practice Feedback", font = ("ARIAL", 20, "bold"))
        lblHeading.grid (column = 0, row = 0, columnspan = 5,sticky=W+E+N+S,pady=50)
        lblHeading.configure(bg='blue', fg='white')

        lblQuestion1 = Label (self, text = "1)	3, 11, 19, 27, ?", font = ("MS", 10))
        lblQuestion1.grid(row = 2, column = 0, sticky = W,padx=50)
        lblQuestion1.configure(bg='blue', fg='white')
        lblQuestion2 = Label (self, text = "2)	3, 6, 11, 18, ?", font = ("MS", 10))
        lblQuestion2.grid(row = 3, column = 0, sticky = W,padx=50)
        lblQuestion2.configure(bg='blue', fg='white')
        lblQuestion3 = Label (self, text = "3)	516, 497, 478, 459, ?", font = ("MS", 10))
        lblQuestion3.grid(row = 4, column = 0, sticky = W,padx=50)
        lblQuestion3.configure(bg='blue', fg='white')

        lblcorrectAnswer =Label (self, text = "Correct Answer", font = ("ARIAL", 12, "bold"))
        lblcorrectAnswer.grid (column = 1, row = 1)
        lblcorrectAnswer.configure(bg='blue', fg='white')

        lblq1correct = Label (self, text ="35", font = ("MS", 10))
        lblq1correct.grid(column= 1, row = 2)
        lblq1correct.configure(bg='blue', fg='white')
        lblq2correct = Label (self, text ="27", font = ("MS", 10))
        lblq2correct.grid(column= 1, row = 3)
        lblq2correct.configure(bg='blue', fg='white')
        lblq3correct = Label (self, text ="440", font = ("MS", 10))
        lblq3correct.grid(column= 1, row = 4)
        lblq3correct.configure(bg='blue', fg='white')

        lbltheirAnswer = Label (self, text = "Your answer", font = ("ARIAL", 12, "bold"))
        lbltheirAnswer.grid(row = 1, column = 2)
        lbltheirAnswer.configure(bg='blue', fg='white')


    #Pickle function getting results
    def pickleResults(self):
        unpicklefile = open("practiceAnswers.txt", "r")
        q3 = pickle.load(unpicklefile)
        q2 = pickle.load(unpicklefile)
        q1 = pickle.load(unpicklefile)
        score = pickle.load(unpicklefile)
        score = str(score) + "/3"
        percentage = pickle.load(unpicklefile)
        percentage = str(percentage) + "%"
        lblq3 = Label (self, text = q3, font = ("MS", 10))
        lblq3.grid(column = 2, row = 4)
        lblq3.configure(bg='blue', fg='white')
        lblq2 = Label (self, text = q2, font = ("MS", 10))
        lblq2.grid(column = 2, row = 3)
        lblq2.configure(bg='blue', fg='white')
        lblq1 = Label (self, text = q1, font = ("MS", 10))
        lblq1.grid(column = 2, row = 2)
        lblq1.configure(bg='blue', fg='white')

        lblYouScored = Label (self, text = "You scored:", font = ("ARIAL", 12 ))
        lblYouScored.grid(row = 5, column = 2,pady=20)
        lblYouScored.configure(bg='blue', fg='white')

        lblScore = Label (self, text = score, font = ("ARIAL", 12))
        lblScore.grid(row = 5, column = 3)
        lblScore.configure(bg='blue', fg='white')

        lblPercentage = Label (self, text = "Percentage score:", font = ("ARIAL", 12))
        lblPercentage.grid(row = 6, column =2)
        lblPercentage.configure(bg='blue', fg='white')
        lblYourPercentage = Label(self, text = percentage, font = ("ARIAL", 12, "bold"))
        lblYourPercentage.grid(row = 6, column =3)
        lblYourPercentage.configure(bg='blue', fg='white')


    #Declare return button
    def returnButton(self):
        butSubmit = Button(self, text='Return',font=('MS', 8,'bold'))
        butSubmit['command']= self.navigate
        butSubmit.grid(row=10, column=2, sticky = E,pady=20)
        butSubmit.configure(bg='white', fg='blue')

    #Clear screen
    def clearScreen(self):
        self.grid_forget()

    #Navigate back to login
    def navigate(self):
        Application.setCurrentScreen(1)
        self.clearScreen()

#//\\//\\//\\//\\//#
#QUESTION ONE CLASS#
#//\\//\\//\\//\\//#
class testQuestionOne(Frame):

    #Initialize frame
    def __init__(self, master): #constructor
	    Frame.__init__(self, master)

    #Draw frame contents
    def draw(self):
        self.grid()
        self.heading()
        self.questionAndAnswer()
        self.submitButton()
        self.configure(bg='blue')
        self.grid_columnconfigure(index = 1,minsize=(self.winfo_screenwidth()/3))
        self.grid_rowconfigure(index = 1, minsize =(self.winfo_screenheight()/4))

    #Declare heading
    def heading(self):
        lblHeading = Label (self, text = "Question 1", font =("ARIAL", 20, "bold"))
        lblHeading.grid (row = 0, column = 0, columnspan = 1,sticky = W,pady=10,padx=10)
        lblHeading.configure(bg='blue', fg='white')
        lblQuestion = Label (self, font=("ARIAL",12),text = "The diagram below is a map showing towns called A, B, C, etc.and the roads connecting them. The roads are all one-way and cars can only \n travel in the direction of the arrow. Each section of road links two towns, and the number marked on the road is the distance in miles \n between the two towns.")
        lblQuestion.grid (row = 1, column = 0, columnspan = 3, sticky = N,pady=30,padx=10)
        lblQuestion.configure(bg='blue', fg='white')

    #Declare questions
    def questionAndAnswer(self):
        self.oneA = StringVar()
        self.oneB = StringVar()
        self.oneC = StringVar()

        #question1a
        lblQuestion1a = Label (self, text = "a) 	What is the shortest distance from A to E?")
        lblQuestion1a.grid (row = 6, column = 1, columnspan = 2,sticky = W )
        lblQuestion1a.configure(bg='blue', fg='white')

        #radio buttons
        R1Q1a = Radiobutton(self, text = "23 Miles", variable=self.oneA, value = "23")
        R1Q1a.grid (row = 10, column = 1, sticky = N)
        R1Q1a.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R2Q1a = Radiobutton(self, text = "19 Miles", variable=self.oneA, value = "19")
        R2Q1a.grid (row = 11, column = 1, sticky = N)
        R2Q1a.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R3Q1a = Radiobutton(self, text = "17 Miles", variable=self.oneA, value = "17")
        R3Q1a.grid (row = 12, column = 1, sticky = N)
        R3Q1a.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')

        #question1b
        lblQuestion1b = Label (self, text = "b)	A passenger writes down names of towns in the order that he passes\n through them. Which of the following routes is possible according to the above \nmap?")
        lblQuestion1b.grid (row = 14, column = 1, columnspan = 2, sticky = W)
        lblQuestion1b.configure(bg='blue', fg='white')

        #radio buttons
        R1Q1b = Radiobutton(self, text = "BEGDC", variable=self.oneB, value = 'BEGDC')
        R1Q1b.grid (row = 16, column = 1, sticky = W)
        R1Q1b.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R2Q1b = Radiobutton(self, text = "ACBEG", variable=self.oneB, value = 'ACBEG')
        R2Q1b.grid (row = 16, column = 1, sticky = N)
        R2Q1b.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R3Q1b = Radiobutton(self, text = "FBCEG", variable=self.oneB, value = 'FBCEG')
        R3Q1b.grid (row = 16, column = 1, sticky = E)
        R3Q1b.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R4Q1b = Radiobutton(self, text = "AFGED", variable=self.oneB, value = 'AFGED')
        R4Q1b.grid (row = 18, column = 1, sticky = W)
        R4Q1b.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R5Q1b = Radiobutton(self, text = "FBEGD", variable=self.oneB, value = 'FBEGD')
        R5Q1b.grid (row = 18, column = 1, sticky = N)
        R5Q1b.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R6Q1b = Radiobutton(self, text = "ACBFG", variable=self.oneB, value = 'ACBFG')
        R6Q1b.grid (row = 18, column = 1, sticky = E)
        R6Q1b.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')


        #question1c
        lblQuestion1c = Label (self, text = "c)	Due to roadworks, the road from A to C is not in use. What is the shortest distance from A to C, avoiding this road?")
        lblQuestion1c.grid (row = 20, column = 0,  columnspan = 3, sticky = W,padx=30,pady=30)
        lblQuestion1c.configure(bg='blue', fg='white')

        #radio buttons
        R1Q1c = Radiobutton(self, text = "19 Miles", variable=self.oneC, value = 19)
        R1Q1c.grid (row = 22, column = 0, sticky = N)
        R1Q1c.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R2Q1c = Radiobutton(self, text = "20 Miles", variable=self.oneC, value = 20)
        R2Q1c.grid (row = 23, column = 0, sticky = N)
        R2Q1c.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R3Q1c = Radiobutton(self, text = "22 Miles", variable=self.oneC, value = 22)
        R3Q1c.grid (row = 24, column = 0, sticky = N)
        R3Q1c.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')

        #image
        photo = PhotoImage(file="q1_map.gif")
        w = Label(self, image=photo)
        w.photo = photo
        w.grid(row= 8, column=0, rowspan = 10,padx=30)

    #Declare button
    def submitButton(self):
        butSubmit = Button(self, text = 'Submit',font = ('MS', 8,'bold'))
        butSubmit['command'] = self.storeAnswers
        butSubmit.grid(row = 28, column = 2, columnspan = 1, sticky = E)
        butSubmit.configure(bg='white', fg='blue')

    #Clear screen
    def clearScreen(self):
        self.grid_forget()

    #Store answers
    def storeAnswers(self):
        score1 = 0
        q1a = self.oneA.get()
        q1b = self.oneB.get()
        q1c = self.oneC.get()
        if (q1a == "") or (q1b == "") or (q1c == ""):
            tkMessageBox.showinfo("Practice Question", "Please answer every question")
        else:
            if q1a == "19":
                score1 += 1
            if q1b == "ACBEG"  or "FBEGD":
                score1 += 1
            if q1c == "22":
                score1 += 1
            test_answers = open("testAnswers.txt", "w")
            test_answers.write(str(score1)+'\n')
            test_answers.close()
            Application.setCurrentScreen(5)
            self.clearScreen()


#//\\//\\//\\//\\//#
#QUESTION TWO CLASS#
#//\\//\\//\\//\\//#
class testQuestionTwo(Frame):

    #Initialize frame
    def __init__(self, master): #constructor
        Frame.__init__(self, master)

    #Draw frame contents
    def draw(self):
        self.grid()
        self.heading()
        self.questionAndAnswer()
        self.submitButton()
        self.configure(bg='blue')
        self.grid_columnconfigure(index = 1,minsize=(self.winfo_screenwidth()/2))
        self.grid_rowconfigure(index = 1, minsize =(self.winfo_screenheight()/4))

    #Declare heading
    def heading(self):
        lblHeading = Label (self, text = "Question 2", font =("ARIAL", 20, "bold"))
        lblHeading.grid (row = 0, column = 0, columnspan = 1, sticky= W,padx=10,pady=10)
        lblHeading.configure(bg='blue', fg='white')
        lblQuestion = Label (self, font=("ARIAL",12),text = "The words listed below are formed from some of the letters present in the diagram. \n Which of the words can you make if you start at the top left corner and follow the arrows?  Select the words which can be made.")
        lblQuestion.grid (row = 1, column = 0, columnspan = 3, sticky = W,padx=10)
        lblQuestion.configure(bg='blue', fg='white')

    #Declare questions
    def questionAndAnswer(self):
        self.varCB1 = IntVar()
        self.varCB2 = IntVar()
        self.varCB3 = IntVar()
        self.varCB4 = IntVar()
        self.varCB5 = IntVar()
        self.varCB6 = IntVar()
        self.varCB7 = IntVar()
        self.varCB8 = IntVar()
        self.varCB9 = IntVar()
        self.varCB10 = IntVar()


        #question 2
        photo = PhotoImage(file="graph.gif")
        w = Label(self, image=photo)
        w.photo = photo
        w.grid(row= 4, column=0, rowspan = 10,padx=50)


        #radio buttons
        CB1 = Checkbutton(self, text=" SING ", variable=self.varCB1)
        CB1.grid(row=4, column=1, sticky=W,padx=300)
        CB1.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        CB2 = Checkbutton(self, text=" GIRL ", variable=self.varCB2)
        CB2.grid(row=5, column=1,  sticky=W,padx=300)
        CB2.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        CB3 = Checkbutton(self, text=" DENT ", variable=self.varCB3)
        CB3.grid(row=6, column=1, sticky=W,padx=300)
        CB3.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        CB4 = Checkbutton(self, text=" STAND ", variable=self.varCB4)
        CB4.grid(row=7, column=1, sticky=W,padx=300)
        CB4.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        CB5 = Checkbutton(self, text=" SLANG ", variable=self.varCB5)
        CB5.grid(row=8, column=1, sticky=W,padx=300)
        CB5.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        CB6 = Checkbutton(self, text=" SALT ", variable=self.varCB6)
        CB6.grid(row=9, column=1, sticky=W,padx=300)
        CB6.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        CB7 = Checkbutton(self, text=" SLIT ", variable=self.varCB7)
        CB7.grid(row=10, column=1, sticky=W,padx=300)
        CB7.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        CB8 = Checkbutton(self, text=" SAND ", variable=self.varCB8)
        CB8.grid(row=11, column=1, sticky=W,padx=300)
        CB8.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        CB9 = Checkbutton(self, text=" SINGLE ", variable=self.varCB9)
        CB9.grid(row=12, column=1, sticky=W,padx=300)
        CB9.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        CB10 = Checkbutton(self, text=" STING ", variable=self.varCB10)
        CB10.grid(row=13, column=1, sticky=W,padx=300)
        CB10.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')


    #Clear screen
    def clearScreen(self):
        self.grid_forget()

    #Declare button
    def submitButton(self):
        butSubmit = Button(self, text='Submit',font=('MS', 8,'bold'))
        butSubmit['command']=self.storeAnswers
        butSubmit.grid(row=18, column=2, columnspan=1)
        butSubmit.configure(bg='white',fg='blue')

    #Store answers
    def storeAnswers(self):
        score2 = 0
        q1a = self.varCB1.get()
        q1b = self.varCB2.get()
        q1c = self.varCB3.get()
        q1d = self.varCB4.get()
        q1e = self.varCB5.get()
        q1f = self.varCB6.get()
        q1g = self.varCB7.get()
        q1h = self.varCB8.get()
        q1i = self.varCB9.get()
        q1j = self.varCB10.get()

        checkarray = [q1a, q1h, q1i, q1d, q1e, q1f, q1g, q1b,q1c, q1j]
        answered = 0
        unanswered = 0
        for i in (checkarray):
            if i == 0:
                unanswered += 1
        if unanswered == 10:
            tkMessageBox.showinfo("Question 2", "Please tick at least one box")
        else:

            if q1a == 1 and score2 >=0:
                score2 += 1
            if q1h == 1 and score2 >=0:
                score2 += 1
            if q1i == 1 and score2 >=0:
                score2 += 1
            if q1b == 1 and score2 >0:
                score2 -= 1
            if q1c == 1 and score2 >0:
                score2 -= 1
            if q1d == 1 and score2 >0:
                score2 -= 1
            if q1e == 1 and score2 >0:
                score2 -= 1
            if q1f == 1 and score2 >0:
                score2 -= 1
            if q1g == 1 and score2 >0:
                score2 -= 1
            if q1j == 1 and score2 >0:
                score2 -= 1

            test_answers = open("testAnswers.txt", "a")
            test_answers.write(str(score2)+'\n')
            test_answers.close()
            Application.setCurrentScreen(6)
            self.clearScreen()



#//\\//\\//\\//\\//\\#
#QUESTION THREE CLASS#
#//\\//\\//\\//\\//\\#
class testQuestionThree(Frame):

    #Initialize frame
    def __init__(self, master):
        Frame.__init__(self, master)

    #Draw frame contents
    def draw(self):
        self.grid()
        self.heading()
        self.questionAndAnswer()
        self.submitButton()
        self.configure(bg='blue')
        self.grid_columnconfigure(index = 1,minsize=(self.winfo_screenwidth()/12))
        self.grid_rowconfigure(index = 1, minsize =(self.winfo_screenheight()/4))

    #Declare heading
    def heading(self):
        lblHeading = Label (self, text =  "Question 3", font =("ARIAL", 20, "bold"))
        lblHeading.grid (row = 0, column = 0, sticky = W,padx=10,pady=10)
        lblHeading.configure(bg='blue', fg='white')
        lblQuestion = Label (self,font =("ARIAL", 12), text = "Work through the following instructions and find the value of answer. \n  (Hint: Draw a table of values for a and b as you work through the statements.)")
        lblQuestion.grid (row = 1, column = 0, sticky = W, padx=30)
        lblQuestion.configure(bg='blue', fg='white')

    #Declare Questions
    def questionAndAnswer(self):
        self.three = IntVar()

        #question 3
        lblQuestion3 = Label (self, text = "\n (1) A = 1,\n (2) B = 8,\n (3) Add 1 to S,\n (4) Subtract a from B,\n (5) If B is greater than 0 then add 3 to A,\n (6) If A is less than 6 then go to (3), else go to(7),\n (7) Set answer to 2 x A",font = ("MS", 8), justify = LEFT)
        lblQuestion3.grid(row = 2, column = 0, sticky = W)
        lblQuestion3.configure(bg='blue', fg='white')

        #radio buttons
        R1Q3 = Radiobutton(self, text = "Answer = 11", variable=self.three, value = 11,)
        R1Q3.grid(row = 10, column = 0, sticky = E,pady=30)
        R1Q3.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R2Q3 = Radiobutton(self, text = "Answer = 17", variable=self.three, value = 17)
        R2Q3.grid(row = 10, column = 1, sticky = W,)
        R2Q3.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R3Q1 = Radiobutton(self, text = "Answer = 16", variable=self.three, value = 16)
        R3Q1.grid(row = 10, column = 2, sticky = W, )
        R3Q1.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R4Q3 = Radiobutton(self, text = "Answer = 13", variable=self.three, value = 13)
        R4Q3.grid(row = 10, column = 3, sticky = W,)
        R4Q3.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R5Q3 = Radiobutton(self, text = "Answer = 19", variable=self.three, value = 19)
        R5Q3.grid(row = 10, column = 4, sticky = W,)
        R5Q3.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')

    #Declare submit button
    def submitButton(self):
        butSubmit = Button(self, text = 'Submit',font = ('MS', 8,'bold'))
        butSubmit['command'] = self.storeAnswers
        butSubmit.grid(row = 12, column = 4)
        butSubmit.configure(bg='white', fg='blue')

    #Clear screen
    def clearScreen(self):
        self.grid_forget()

    #Store answers
    def storeAnswers(self):
        q3 = self.three.get()
        if q3 == 0:
            tkMessageBox.showinfo("Question 3", "Please tick at least one box")
        if q3 == 16:
            score3 = 1
        else:
            score3 = 0

        test_answers = open("testAnswers.txt", "a")
        test_answers.write(str(score3)+'\n')
        test_answers.close()
        Application.setCurrentScreen(7)
        self.clearScreen()


#//\\//\\//\\//\\//\#
#QUESTION FOUR CLASS#
#//\\//\\//\\//\\//\#
class testQuestionFour(Frame):

    #Declare frame
    def __init__(self, master): #constructor
            Frame.__init__(self, master)

    #Draw frame contents
    def draw(self):
        self.grid()
        self.heading()
        self.questionAndAnswer()
        self.submitButton()
        self.configure(bg='blue')
        self.grid_columnconfigure(index = 1,minsize=(self.winfo_screenwidth()/2))
        self.grid_rowconfigure(index = 1, minsize =(self.winfo_screenheight()/3))

    #Declare heading
    def heading(self):
        lblHeading = Label (self, text = "Question 4", font =("ARIAL", 20, "bold"))
        lblHeading.grid (row = 0, column = 0, columnspan = 1,sticky = W,padx=10,pady=10)
        lblHeading.configure(bg='blue', fg='white')

    #Declare question
    def questionAndAnswer(self):
        self.selected = IntVar()

        #question
        lblQuestion = Label (self,font =("ARIAL", 12), text = "x is one quarter of y.\n q is twice x.\n  p is one third of q.\n What is the relationship between p and y? Select the correct answer.")
        lblQuestion.grid (row = 1, column = 1, sticky = W+E+N+S)
        lblQuestion.configure(bg='blue', fg='white')

        #radio buttons
        R1Q1 = Radiobutton(self, text = "3p = 2y", variable=self.selected, value = 1)
        R1Q1.grid (row = 12, column = 1, sticky = W,padx=100)
        R1Q1.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R2Q1 = Radiobutton(self, text = "2p = 3y", variable=self.selected, value = 2)
        R2Q1.grid (row = 13, column = 1, sticky = W,padx=100)
        R2Q1.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R3Q1 = Radiobutton(self, text = "y = 2p", variable=self.selected, value = 3)
        R3Q1.grid (row = 14, column = 1, sticky = W,padx=100)
        R3Q1.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R4Q1 = Radiobutton(self, text = "6p = y", variable=self.selected, value = 4)
        R4Q1.grid (row = 15, column = 1, sticky = W,padx=100)
        R4Q1.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')
        R5Q1 = Radiobutton(self, text = "5y = p", variable=self.selected, value = 5)
        R5Q1.grid (row = 16, column = 1, sticky = W,padx=100)
        R5Q1.configure(bg='blue',fg='white',selectcolor ='blue',activebackground= 'blue',activeforeground='white')

    #Declare button
    def submitButton(self):
        butSubmit = Button(self, text = 'Submit',font = ('MS', 8,'bold'))
        butSubmit['command'] = self.storeAnswers
        butSubmit.grid(row = 28, column = 2, columnspan = 1, sticky = E)
        butSubmit.configure(bg='white',fg='blue')

    #Clear screen
    def clearScreen(self):
        self.grid_forget()

    #Store answers
    def storeAnswers(self):
        q4 = self.selected.get()
        if q4 == 0:
            tkMessageBox.showinfo("Question 3", "Please tick at least one box")
        else:
            if q4 == 4:
                score4 = 1
            else:
                score4 = 0
            test_answers = open("testAnswers.txt", "a")
            test_answers.write(str(score4)+'\n')
            test_answers.close()
            Application.setCurrentScreen(8)
            self.clearScreen()


#//\\//\\//\\//\\//\#
#QUESTION FIVE CLASS#
#//\\//\\//\\//\\//\#
class testQuestionFive(Frame):

    #Intialize frame
    def __init__(self, master): #constructor
	    Frame.__init__(self, master)

    #Draw frame contents
    def draw(self):
        self.grid()
        self.heading()
        self.questionAndAnswer()
        self.submitButton()
        self.configure(bg='blue')
        self.grid_columnconfigure(index = 1,minsize=(self.winfo_screenwidth()/2))
        self.grid_rowconfigure(index = 1, minsize =(self.winfo_screenheight()/3))

    #Declare heading
    def heading(self):
        lblHeading = Label (self, text = "Question 5", font =("ARIAL", 20, "bold"))
        lblHeading.grid (row = 0, column = 0, columnspan = 1,sticky = W,padx=10,pady=10)
        lblHeading.configure(bg='blue', fg='white')

    #Declare question
    def questionAndAnswer(self):

        #question
        lblQuestion = Label (self,font =("ARIAL", 12), text = "Below is a partially completed table showing the results of applying certain operators to a sequence of \n letters. Each operation changes one sequence of letters into another sequence of letters or single letter \n (eg.  house into h ). The operators are indicated by capital letters such as FIRST, LAST etc")
        lblQuestion.grid (row = 1, column = 0,columnspan =2, sticky = W+E+N+S)
        lblQuestion.configure(bg='blue', fg='white')

        lblQuestionInstruction = Label (self,font =("ARIAL", 12), text ="Fill in the three missing results in the table.")
        lblQuestionInstruction.grid(row = 2, column = 0, columnspan = 3, sticky = N)
        lblQuestionInstruction.configure(bg='blue', fg='white')

        #question labels
        operationLabel = Label(self, text = "Operations", font = ("MS", 12, "bold"))
        operationLabel.grid(row = 16, column = 0, columnspan = 1, sticky = N)
        operationLabel.configure(bg='blue', fg='white')
        resultLabel = Label(self, text = "Results", font = ("MS", 12, "bold"))
        resultLabel.grid(row = 16, column = 1, columnspan = 1, sticky = N)
        resultLabel.configure(bg='blue', fg='white')

        #operation labels
        operationOneLabel= Label(self, text="(FIRST (house))")
        operationOneLabel.grid(row = 17, column = 0, columnspan = 1, sticky = N)
        operationOneLabel.configure(bg='blue', fg='white')
        operationTwoLabel= Label(self, text="(LAST (house))")
        operationTwoLabel.grid(row = 18, column = 0, columnspan = 1, sticky = N)
        operationTwoLabel.configure(bg='blue', fg='white')
        operationThreeLabel= Label(self, text="(JOIN (dust) (man))")
        operationThreeLabel.grid(row = 19, column = 0, columnspan = 1, sticky = N)
        operationThreeLabel.configure(bg='blue', fg='white')
        operationFourLabel= Label(self, text="(JOIN (FIRST (house)) (LAST(house) ) )")
        operationFourLabel.grid(row = 20, column = 0, columnspan = 1, sticky = N)
        operationFourLabel.configure(bg='blue', fg='white')
        operationFiveLabel= Label(self, text="(FIRST (REVERSE (abcde) ) )")
        operationFiveLabel.grid(row = 21, column = 0, columnspan = 1, sticky = N)
        operationFiveLabel.configure(bg='blue', fg='white')
        operationSixLabel= Label(self, text="( JOIN (REVERSE(jkl)) (FIRST (REVERSE (pgr) ) ) )")
        operationSixLabel.grid(row = 22, column = 0, columnspan = 1, sticky = N)
        operationSixLabel.configure(bg='blue', fg='white')
        operationSevenLabel = Label(self, text="( LAST (JOIN(FIRST(REVERSE(fg) ) ) (JOIN(rst) (LAST(jk)) ) ) )")
        operationSevenLabel.grid(row = 23, column = 0, columnspan = 1, sticky = N)
        operationSevenLabel.configure(bg='blue', fg='white')

        #results labels
        resultsOneLabel = Label(self,text="h")
        resultsOneLabel.grid(row= 17, column = 1, columnspan = 2, sticky= N)
        resultsOneLabel.configure(bg='blue', fg='white')
        resultsTwoLabel = Label(self,text="e")
        resultsTwoLabel.grid(row= 18, column = 1, columnspan = 2, sticky= N)
        resultsTwoLabel.configure(bg='blue', fg='white')
        resultsThreeLabel = Label(self,text="dustman")
        resultsThreeLabel.grid(row= 19, column = 1, columnspan = 2, sticky= N)
        resultsThreeLabel.configure(bg='blue', fg='white')
        resultsFourLabel = Label(self,text="yllib")
        resultsFourLabel.grid(row= 20, column = 1, columnspan = 2, sticky= N)
        resultsFourLabel.configure(bg='blue', fg='white')

        #results input
        self.resultsFiveInput = Entry(self)
        self.resultsFiveInput.grid(row = 21, column = 1, columnspan = 2, sticky = N)
        self.resultsSixInput = Entry(self)
        self.resultsSixInput.grid(row = 22, column = 1, columnspan = 2, sticky = N)
        self.resultsSevenInput = Entry(self)
        self.resultsSevenInput.grid(row = 23, column = 1, columnspan = 2, sticky = N)

    #Clear screen
    def clearScreen(self):
        self.grid_forget()

    #Declare button
    def submitButton(self):
        butSubmit = Button(self, text = 'Submit',font = ('MS', 8,'bold'))
        butSubmit['command'] = self.storeAnswers
        butSubmit.grid(row = 28, column = 2, sticky = W)
        butSubmit.configure(bg='white',fg='blue')

    #Store answers
    def storeAnswers(self):
        score5 = 0
        resultsFive = self.resultsFiveInput.get()
        resultsSix = self.resultsSixInput.get()
        resultsSeven = self.resultsSevenInput.get()
        if (resultsFive == "") or (resultsSix == "") or (resultsSeven == ""):
            tkMessageBox.showinfo("Question 2", "Please fill in every box")
        else:

            if resultsFive == "e":
                score5 += 1
            if resultsSix == "lkjr":
                score5 += 1
            if resultsSeven == "k":
                score5 += 1
            test_answers = open("testAnswers.txt", "a")
            test_answers.write(str(score5)+'\n')
            test_answers.close()
            Application.setCurrentScreen(9)
            self.clearScreen()


#//\\//\\//\\//\\//#
#TEST RESULTS CLASS#
#//\\//\\//\\//\\//#
class testResults(Frame):

    #Initialize frame
    def __init__(self, master):
        Frame.__init__(self,master)

    #Draw frame content
    def draw(self):
        self.grid()
        self.printButton()
        self.returnButton()
        self.heading()
        self.pickleResults()
        self.configure(bg='blue')
        self.grid_columnconfigure(index = 1,minsize=(self.winfo_screenwidth()/3))
        self.grid_rowconfigure(index = 1, minsize =(self.winfo_screenheight()/3))

      #Declare heading
    def heading(self):
        lblHeading = Label (self, text = "RESULTS", font =("ARIAL", 20, "bold"))
        lblHeading.grid (row = 0, column = 0, columnspan = 1,sticky = W,padx=10,pady=10)
        lblHeading.configure(bg='blue', fg='white')


    #Pickle function getting results
    def pickleResults(self):
        unpicklefile = open("testAnswers.txt", "r")
        score1 = unpicklefile.readline()
        score2 = unpicklefile.readline()
        score3 = unpicklefile.readline()
        score4 = unpicklefile.readline()
        score5 = unpicklefile.readline()
        totalScore = (float(score1) + float(score2) + float(score3) + float(score4) + float(score5))
        stringTotal = str(totalScore) + "/12"
        percentage = (totalScore/11 *100)
        percentage = "%.2f" % percentage
        percentage = str(percentage) + "%"


        if score1 == "":
            displayScore1 = "0/3"
        else:
            displayScore1 = score1 + "/3"

        if score2 == "":
           displayScore2 = "0/3"
        else:
            displayScore2 = score2 + "/3"

        if score3 == "":
            displayScore3 = "0/1"
        else:
            displayScore3 = score3 + "/1"

        if score4 == "":
            displayScore4 = "0/1"
        else:
            displayScore4 = score4 + "/1"

        if score5 == "":
            displayScore5 = "0/3"
        else:
            displayScore5 = score5 + "/3"

        #page layout
        lblQuestion1 = Label (self, text = "Question #1:", font = ("ARIAL", 12))
        lblQuestion1.grid(row = 1, column = 0, sticky = E,padx=100)
        lblQuestion1.configure(bg='blue', fg='white')
        lblQuestion2 = Label (self, text = "Question #2:", font = ("ARIAL", 12))
        lblQuestion2.grid(row = 2, column = 0, sticky = E,padx=100)
        lblQuestion2.configure(bg='blue', fg='white')
        lblQuestion3 = Label (self, text = "Question #3:", font = ("ARIAL", 12))
        lblQuestion3.grid(row = 3, column = 0, sticky = E,padx=100)
        lblQuestion3.configure(bg='blue', fg='white')
        lblQuestion4 = Label (self, text = "Question #4:", font = ("ARIAL", 12))
        lblQuestion4.grid(row = 4, column = 0, sticky = E,padx=100)
        lblQuestion4.configure(bg='blue', fg='white')
        lblQuestion5 = Label (self, text = "Question #5:", font = ("ARIAL", 12))
        lblQuestion5.grid(row = 5, column = 0, sticky = E,padx=100)
        lblQuestion5.configure(bg='blue', fg='white')

        lblq1score = Label (self, text = displayScore1, font = ("ARIAL", 12))
        lblq1score.grid(column= 1, row = 1,sticky=W)
        lblq1score.configure(bg='blue', fg='white')
        lblq2score = Label (self, text =displayScore2, font = ("ARIAL", 12))
        lblq2score.grid(column= 1, row = 2,sticky=W)
        lblq2score.configure(bg='blue', fg='white')
        lblq3score = Label (self, text =displayScore3, font = ("ARIAL", 12))
        lblq3score.grid(column= 1, row = 3,sticky=W)
        lblq3score.configure(bg='blue', fg='white')
        lblq4score = Label (self, text =displayScore4, font = ("ARIAL", 12))
        lblq4score.grid(column= 1, row = 4,sticky=W)
        lblq4score.configure(bg='blue', fg='white')
        lblq5score = Label (self, text =displayScore5, font = ("ARIAL", 12))
        lblq5score. grid(column= 1, row = 5,sticky=W)
        lblq5score.configure(bg='blue', fg='white')

        lblYouScored = Label (self, text = "You scored:", font = ("ARIAL", 14))
        lblYouScored.grid(row = 6, column = 2, sticky = E)
        lblYouScored.configure(bg='blue', fg='white')
        lblScore = Label (self, text = stringTotal, font = ("ARIAL", 14))
        lblScore.grid(row = 6, column = 3)
        lblScore.configure(bg='blue', fg='white')

        lblPercentage = Label (self, text = "Percentage score:", font = ("ARIAL", 14))
        lblPercentage.grid(row = 7, column =2)
        lblPercentage.configure(bg='blue', fg='white')
        lblYourPercentage = Label(self, text = percentage, font = ("ARIAL", 14))
        lblYourPercentage.grid(row = 7, column =3)
        lblYourPercentage.configure(bg='blue', fg='white')

        #user details
        detailsFile = open("details.txt", "r")
        firstName = detailsFile.readline()
        surname = detailsFile.readline()
        studentNo = detailsFile.readline()
        year = detailsFile.readline()
        DOB = detailsFile.readline()

        lblfirstName1 = Label (self, text = "First Name:", font = ("ARIAL", 12))
        lblfirstName1.grid(column= 2, row = 1)
        lblfirstName1.configure(bg='blue', fg='white')
        lblsurname1 = Label (self, text = "Surname:", font = ("ARIAL", 12))
        lblsurname1.grid(column= 2, row = 2)
        lblsurname1.configure(bg='blue', fg='white')
        lblstudentNo1 = Label (self, text = "Student No:", font = ("ARIAL", 12))
        lblstudentNo1.grid(column= 2, row = 3)
        lblstudentNo1.configure(bg='blue', fg='white')
        lblyear1 = Label (self, text ="Year of Study:", font =("ARIAL", 12))
        lblyear1.grid(column= 2, row = 4)
        lblyear1.configure(bg='blue', fg='white')
        lblDOB1 = Label (self, text ="Date of Birth:", font = ("ARIAL", 12))
        lblDOB1.grid(column= 2, row = 5)
        lblDOB1.configure(bg='blue', fg='white')

        lblfirstName = Label (self, text = firstName, font = ("ARIAL", 12))
        lblfirstName.grid(column= 3, row = 1)
        lblfirstName.configure(bg='blue', fg='white')
        lblsurname = Label (self, text = surname, font = ("ARIAL", 12))
        lblsurname.grid(column= 3, row = 2)
        lblsurname.configure(bg='blue', fg='white')
        lblstudentNo = Label (self, text = studentNo, font = ("ARIAL", 12))
        lblstudentNo.grid(column= 3, row = 3)
        lblstudentNo.configure(bg='blue', fg='white')
        lblyear = Label (self, text =year, font = ("ARIAL", 12))
        lblyear.grid(column= 3, row = 4)
        lblyear.configure(bg='blue', fg='white')
        lblDOB = Label (self, text =DOB, font = ("ARIAL", 12))
        lblDOB.grid(column= 3, row = 5)
        lblDOB.configure(bg='blue', fg='white')

    #Print button
    def printButton(self):
        butPrint = Button(self, text='Print',font=('MS', 8,'bold'))
        butPrint['command']= self.Print
        butPrint.grid(row=12, column=0, columnspan=1, sticky = N)
        butPrint.configure(bg='white', fg='blue')

    #Declare return button
    def returnButton(self):
        butSubmit = Button(self, text='Return',font=('MS', 8,'bold'))
        butSubmit['command']= self.navigate
        butSubmit.grid(row=11, column=0, columnspan=1, sticky = N)
        butSubmit.configure(bg='white', fg='blue')

    #Clear screen
    def clearScreen(self):
        self.grid_forget()

    def Print(self):
        printfile = tempfile.mktemp ("print.txt")
        open (printfile, "w").write ("This is a test")
        win32api.ShellExecute (
          0,
          "printto",
          printfile,
          '"%s"' % win32print.GetDefaultPrinter (),
          ".",
          0
            )

    #Navigate back to login
    def navigate(self):
        Application.setCurrentScreen(1)
        self.clearScreen()


#//\\//\\//\\/#
#MAIN FUNCTION#
#//\\//\\//\\/#
def main():

    running = True
    root = Tk()
    root.title("Aptitude Test")
    root.overrideredirect(True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
    root.configure(background='blue')
    app = Application(root)
    root.after(0,app.updateFrame)
    root.mainloop()
main()



