"""
Junhui Park
IST
10 May 2024
GUI for Master Project
Period 1
"""

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from auditionDb import AuditionDb

class MyGui:
    #connect to database 
    def connectionManager(self):
        if (not self.auditionDb.connected):
            #calling connect function on the database file 
            answer = self.auditionDb.connect()

            #change label of button after it connects 
            self.connectButton.config(text = "Disconnect")
            self.auditionDb.connected = True

            #update the connection label based on the answer of connect on database
            self.connectLabel.config(text = answer)

            #load data from database and display it
            self.auditionDb.load()
            self.showRecord(0)
        else:
            #disconnect from database
            answer = self.auditionDb.disconnect()

            #set button text to connect
            self.connectButton.config(text = "Connect")
            self.auditionDb.connected = False

            #update connection label to whatever the disconnect() returns
            self.connectLabel.config(text = answer)

    #exit entire program
    def exitAll(self):
        self.mainWindow.destroy()

    #pop up on menu explaining the database
    def dataInfo(self):
        messagebox.showinfo("Data Info", "Your datas are saved through mySQL tables.")

    #pop up on menu explaining the program
    def helpPopup(self):
        messagebox.showinfo("About", "Program to track audition scores for chair placement.")

    #set blank on all text box
    def setBlank(self):
        self.studentNameEntry.delete(0, tk.END)
        self.instrumentEntry.delete(0, tk.END)
        self.etudeScoreEntry.delete(0, tk.END)
        self.sightReadingScoreEntry.delete(0, tk.END)
        self.totalScoreEntry.delete(0, tk.END)
        
    def showRecord(self, recNum):
        #assign record numbers for all the datas
        self.holdRecord = self.auditionDb.records[recNum]

        #show student name
        self.studentNameEntry.delete(0, tk.END)
        self.studentNameEntry.insert(0, self.holdRecord[1])

        #show instrument
        self.instrumentEntry.delete(0, tk.END)
        self.instrumentEntry.insert(0, self.holdRecord[2])
        
        #show etude scores
        self.etudeScoreEntry.delete(0, tk.END)
        self.etudeScoreEntry.insert(0, self.holdRecord[3])

        #show sight reading scores
        self.sightReadingScoreEntry.delete(0, tk.END)
        self.sightReadingScoreEntry.insert(0, self.holdRecord[4])

        #show total scores
        self.totalScoreEntry.delete(0, tk.END)
        self.totalScoreEntry.insert(0, self.holdRecord[5])

    def insertRec(self):
        if (not self.insertEntry):
            #set all textbox blank
            self.setBlank()

            #set button into submit
            self.addScoreButton.config(text= "Submit")
            self.insertEntry = True
        else:
            #call retrieveRec into get all the record entered in the textbox
            self.retrieveRec()

            #insert into database
            answer = self.auditionDb.insert()
            self.showRecord(0)

            #change button label and feedback label
            self.addScoreButton.config(text = "New Auditionee")
            self.feedbackLabel.config(text = answer)
            self.insertEntry = False

    def retrieveRec(self):
        #get all the records entered in the textbox
        self.stuName = self.studentNameEntry.get()
        self.instType = self.instrumentEntry.get()
        self.etuScore = self.etudeScoreEntry.get()
        self.srScore = self.sightReadingScoreEntry.get()
        self.ttlScore = self.totalScoreEntry.get()
        
        #insert data into the list in db
        self.auditionDb.insertRec = [self.stuName, self.instType, self.etuScore, self.srScore, self.ttlScore]
             
    def deleteRec(self):
        #get the id for the data you want to delete
        self.deleteNumber = self.holdRecord[0]

        #delete the data using delete function on database file
        answer = self.auditionDb.delete(self.deleteNumber)
        self.showRecord(0)

        #update label
        self.feedbackLabel.config(text = answer) 

    def confirmDelete(self):
        #pop up to delete the data
        confirmDeleteData = messagebox.askquestion(self.mainWindow, message = "Press OK to delete " + self.studentNameEntry.get()+".")
        
        if (confirmDeleteData == "yes"):
            #delete data if clicked yes
            answer = self.deleteRec()

            #update label based on return answer
            self.feedbackLabel.config(text=answer)
        else:
            self.feedbackLabel.config(text= "Delete Cancelled")

    def jumpRec(self, jump):
        #jump record based on the button you click
        self.currentRec += jump 
        
        #prevent out of bounds
        if (self.currentRec >= len(self.auditionDb.records)):
            self.currentRec = (len(self.auditionDb.records)-1)
        if (self.currentRec < 0):
            self.currentRec = 0
        
        #display the data corresponding to the changed id
        self.showRecord(self.currentRec)

    def saveUpdateRec(self):
        #get the new data typed in
        self.id = self.holdRecord[0]
        self.sn = self.studentNameEntry.get()
        self.inst = self.instrumentEntry.get()
        self.es = self.etudeScoreEntry.get()
        self.sr = self.sightReadingScoreEntry.get()
        self.ts = self.totalScoreEntry.get()

        #update record list
        self.auditionDb.updateRec = [self.id, self.sn, self.inst, self.es, self.sr, self.ts]
        self.answer = self.auditionDb.updateCurrentRec()

        #reload the database and display it
        self.auditionDb.load()
        self.showRecord(0)
        self.feedbackLabel.config(text = self.answer)

    def setToZero(self):
        self.currentRec = 0 

    def displaySortedData(self, newRecNum):
        #prevent out of bounds
        if (self.auditionDb.cursor.rowcount >= 0):
            #read the option selected on the dropdown menu
            instrument = self.selectedOption.get()
            print(instrument)

            #get specific data for instrument
            answer = self.auditionDb.getSortedList(instrument)
            
            #call sortedRec list
            self.newSortRecord = self.auditionDb.sortedRec[newRecNum]

            #display data in student name
            self.studentNameEntry2.delete(0, tk.END)
            self.studentNameEntry2.insert(0, self.newSortRecord[1])

            #display total score
            self.totalScoreEntry2.delete(0, tk.END)
            self.totalScoreEntry2.insert(0, self.newSortRecord[5])

            #update the label 
            self.showSortLabel.config(text = answer)
        else:
            pass

    #function to show the names in order from highest score to lowest score
    def displaySortedName(self):
        #read the option selected on the dropdown menu
        instrument = self.selectedOption.get()

        #get names of student that plays certain instrument
        names = str(self.auditionDb.getSortedStudentNames(instrument))

        #replace brakets, quotation marks, and commas in the list
        names = names.replace("[", "")
        names = names.replace("]", "")
        names = names.replace("(", "")
        names = names.replace(")", "")
        names = names.replace("'", "")
        names = names.replace("'", "")
        names = names.replace(",,", ",")

        #display names in the messagebox
        self.orderedNames = messagebox.showinfo(self.mainWindow, message = names)

    def jumpSortedData(self, jump):
        #jump record based on the button you click
        self.currentSortedRec += jump 
        
        #prevent out of bounds
        if (self.currentSortedRec >= len(self.auditionDb.sortedRec)):
            self.currentSortedRec = (len(self.auditionDb.sortedRec)-1)
        if (self.currentSortedRec < 0):
            self.currentSortedRec = 0
        
        #display the data corresponding to the changed id
        self.displaySortedData(self.currentSortedRec)


    def setSortedtoZero(self):
        #set the textbox blank
        self.studentNameEntry2.delete(0, tk.END)
        self.totalScoreEntry2.delete(0, tk.END)

    def __init__(self):
            #setting window
            self.mainWindow = tk.Tk()

            #title and window size
            self.mainWindow.title("Audition")
            self.mainWindow.geometry("1000x700")

            #setting auditionDb class as an object
            self.auditionDb = AuditionDb()

            #variables initialization
            self.insertEntry = False
            self.currentRec = 0 
            self.currentSortedRec = 0

            #image frame
            frame = tk.Frame(self.mainWindow)
            frame.place(x= -5, y = -2)

            #call background image
            img = ImageTk.PhotoImage(Image.open("auditionee2.png"))
            imglabel = tk.Label(frame, image = img)
            imglabel.pack()

            #menu bar
            self.menubar = tk.Menu()

            #first menu titled File
            self.fileMenu = tk.Menu(self.menubar)
            self.menubar.add_cascade(menu = self.fileMenu, label = "File")

            #exit option under menu title file
            self.fileMenu.add_command(label = "Exit", command = self.exitAll)
            self.mainWindow.config(menu = self.menubar)

            #data info menu under file
            self.fileMenu.add_command(label = "Data Info", command = self.dataInfo)
            self.mainWindow.config(menu = self.menubar)

            #connect under file
            self.fileMenu.add_command(label = "Connect", command = self.connectionManager)
            self.mainWindow.config(menu = self.menubar)

            #disconnect under file
            self.fileMenu.add_command(label = "Disconnect", command = self.connectionManager)
            self.mainWindow.config(menu = self.menubar)

            #second menu titled data
            self.dataMenu = tk.Menu(self.menubar)
            self.menubar.add_cascade(menu = self.dataMenu, label = "Data")

            #'add auditionee' menu under data
            self.dataMenu.add_command(label = "Add Auditionee", command = lambda: self.insertRec())
            self.mainWindow.config(menu = self.menubar)

            #'delete auditionee' menu under data
            self.dataMenu.add_command(label = "Delete Auditionee", command = lambda: self.confirmDelete)
            self.mainWindow.config(menu = self.menubar)

            #'update auditionee' menu under data
            self.dataMenu.add_command(label = "Update Auditionee", command = lambda: self.saveUpdateRec)
            self.mainWindow.config(menu = self.menubar)

            #third menu titled navigation 
            self.navigation = tk.Menu(self.menubar)
            self.menubar.add_cascade(menu = self.navigation, label = "Navigation")

            #previous auditionee under navigation menu
            self.navigation.add_command(label = "Previous Auditionee", command = lambda: self.jumpRec(-1))
            self.mainWindow.config(menu = self.menubar)

            #next auditionee under navigation menu
            self.navigation.add_command(label = "Next Auditionee", command = lambda: self.jumpRec(1))
            self.mainWindow.config(menu = self.menubar)

            #first auditionee under navigation menu
            self.navigation.add_command(label = "First Auditionee", command = lambda: lambda: self.showRecord(0))
            self.mainWindow.config(menu = self.menubar)

            #last auditionee under navigation menu
            self.navigation.add_command(label = "Last Auditionee", command= lambda: self.jumpRec(len(self.auditionDb.records)-1))
            self.mainWindow.config(menu = self.menubar)

            #fourth menu titled Help
            self.helpMenu = tk.Menu(self.menubar)
            self.menubar.add_cascade(menu = self.helpMenu, label = "Help")

            #about under help menu that shows pop up menu
            self.helpMenu.add_command(label = "About", command = self.helpPopup)
            self.mainWindow.config(menu = self.menubar)

            #button to connect to database
            self.connectButton = tk.Button(self.mainWindow, text = "Connect", command = self.connectionManager)
            self.connectButton.place(x=55, y = 80)

            #label to see if connection was successful
            self.connectLabel = tk.Label(self.mainWindow, text = " ")
            self.connectLabel.place(x = 55, y = 108)

            #label to give feedback
            self.feedbackLabel = tk.Label(self.mainWindow, text = " ")
            self.feedbackLabel.place(x = 55, y= 380)

            #entry to show student name
            self.studentNameEntry = tk.Entry(self.mainWindow, width = 25)
            self.studentNameEntry.place(x = 190, y= 150)

            #label to indicate student name
            self.studentNameLabel = tk.Label(self.mainWindow, text = "Name")
            self.studentNameLabel.place(x = 55, y= 150)

            #entry to show instrument 
            self.instrumentEntry = tk.Entry(self.mainWindow, width = 25)
            self.instrumentEntry.place(x = 190, y = 195)

            #label to indicate instrument
            self.instrumentLabel = tk.Label(self.mainWindow, text = "Instrument")
            self.instrumentLabel.place(x= 55, y=195)

            #entry to show etude score
            self.etudeScoreEntry = tk.Entry(self.mainWindow, width = 25)
            self.etudeScoreEntry.place(x= 190, y= 240)

            #label to indicate etude score
            self.etudeScoreLabel = tk.Label(self.mainWindow, text = "Etude Score")
            self.etudeScoreLabel.place(x= 55, y=240)

            #entry to show sight reading score
            self.sightReadingScoreEntry = tk.Entry(self.mainWindow, width = 25)
            self.sightReadingScoreEntry.place(x = 190, y = 285)

            #label to indicate sight reading score
            self.sightReadingLabel = tk.Label(self.mainWindow, text = "Sight Reading Score")
            self.sightReadingLabel.place(x= 55, y=285)

            #entry to show total score
            self.totalScoreEntry = tk.Entry(self.mainWindow, width = 25)
            self.totalScoreEntry.place(x = 190, y= 330)
            
            #label to indicate total score
            self.totalScoreLabel = tk.Label(self.mainWindow, text = "Total Score")
            self.totalScoreLabel.place(x= 55, y=330)

            #button to add auditionee
            self.addScoreButton = tk.Button(self.mainWindow, text = "New Auditionee", height = 2, command = lambda: self.insertRec())
            self.addScoreButton.place(x= 40, y= 480)

            #button to update auditionee info
            self.updateScoreButton = tk.Button(self.mainWindow, text = "Update Auditionee", height = 2, command = lambda: self.saveUpdateRec())
            self.updateScoreButton.place(x = 175, y = 480)

            #button to delete auditionee
            self.deleteScoreButton = tk.Button(self.mainWindow, text = "Delete Auditionee", height = 2, command = lambda: self.confirmDelete())
            self.deleteScoreButton.place(x = 327, y= 480)

            #button to go to first record
            self.firstRecButton = tk.Button(self.mainWindow, text = "|<", width = 2, height =2, command = lambda: [self.setToZero(), self.showRecord(0)])
            self.firstRecButton.place(x= 55, y= 415)
            
            #button to go back two record
            self.twebefRecButton = tk.Button(self.mainWindow, text = "<<", width = 2, height= 2, command = lambda: self.jumpRec(-2))
            self.twebefRecButton.place(x = 115, y=415)

            #button to go back one record
            self.beforeRecButton = tk.Button(self.mainWindow, text = "<", width = 2, height =2, command = lambda: self.jumpRec(-1))
            self.beforeRecButton.place(x = 175, y = 415)

            #button to go to one record after
            self.oneRecButton = tk.Button(self.mainWindow, text = ">", width = 2, height = 2, command= lambda: self.jumpRec(1))
            self.oneRecButton.place(x=235, y= 415)

            #button to go to two record after
            self.twoRecButton = tk.Button(self.mainWindow, text = ">>", width = 2, height = 2, command = lambda: self.jumpRec(2))
            self.twoRecButton.place(x=295, y=415)

            #button to go to last record
            self.endRecButton = tk.Button(self.mainWindow, text = ">|", width = 2, height = 2, command = lambda: self.jumpRec(len(self.auditionDb.records)-1))
            self.endRecButton.place(x=355, y=415)


            #select Instrument
            options = ["Flute", 
                       "Oboe", 
                       "Clarinet", 
                       "Saxophone", 
                       "Bassoon", 
                       "Trumpet", 
                       "French Horn", 
                       "Trombone", 
                       "Euphonium", 
                       "Tuba", 
                       "Percussion"]

            #select option in dropdown
            self.selectedOption = tk.StringVar()
            self.selectedOption.set("Flute")

            #instrument dropdown and place it
            self.instrumentDropdown = tk.OptionMenu(self.mainWindow, self.selectedOption, *options)
            self.instrumentDropdown.pack()
            self.instrumentDropdown.place(x= 520, y= 80)

            #button to show certain datas that plays the selected instrument
            self.showSelectionButton = tk.Button(self.mainWindow, text = "Show Selection", command = lambda: self.displaySortedData(0))
            self.showSelectionButton.place(x=645, y= 80)

            #entry to show student name under dropdown
            self.studentNameEntry2 = tk.Entry(self.mainWindow, width = 25)
            self.studentNameEntry2.place(x = 655, y= 150)

            #label to indicate student name
            self.studentNameLabel2 = tk.Label(self.mainWindow, text = "Name")
            self.studentNameLabel2.place(x = 520, y = 150)

            #entry to show total score under dropdown
            self.totalScoreEntry2 = tk.Entry(self.mainWindow, width = 25)
            self.totalScoreEntry2.place(x=655, y = 195)

            #label to indicate total score
            self.totalScoreLabel2 = tk.Label(self.mainWindow, text = "Total Score")
            self.totalScoreLabel2.place(x=520, y = 195)

            #button to go to first record
            self.firstSortRecButton = tk.Button(self.mainWindow, text = "|<", width = 2, height =2, command = lambda: [self.setSortedtoZero(), self.displaySortedData(0)])
            self.firstSortRecButton.place(x= 550, y= 260)

            #button to go back two record
            self.twobefSortRecButton = tk.Button(self.mainWindow, text = "<<", width = 2, height =2, command = lambda: self.jumpSortedData(-2))
            self.twobefSortRecButton.place(x= 610, y= 260)

            #button to go back one record
            self.beforeSortRecButton = tk.Button(self.mainWindow, text = "<", width = 2, height =2, command = lambda: self.jumpSortedData(-1))
            self.beforeSortRecButton.place(x= 670, y= 260)
            
            #button to go one record front
            self.oneSortRecButton = tk.Button(self.mainWindow, text = ">", width = 2, height =2, command = lambda: self.jumpSortedData(1))
            self.oneSortRecButton.place(x= 730, y= 260)

            #button to go two record front
            self.twoSortRecButton = tk.Button(self.mainWindow, text = ">>", width = 2, height =2, command = lambda: self.jumpSortedData(2))
            self.twoSortRecButton.place(x= 790, y= 260)

            #button show the last record
            self.endSortRecButton = tk.Button(self.mainWindow, text = ">|", width = 2, height =2, command = lambda: self.jumpSortedData(len(self.auditionDb.sortedRec)-1))
            self.endSortRecButton.place(x= 850, y= 260)

            #button to show the names in order from highest score to lowest score
            self.showSortNames = tk.Button(self.mainWindow, text = "Auditionee in order", command= lambda: self.displaySortedName())
            self.showSortNames.place(x= 550, y= 340)

            #label to show answers for the sorted data
            self.showSortLabel = tk.Label(self.mainWindow, text = " ")
            self.showSortLabel.place(x=550, y =310)

            self.mainWindow.mainloop()
