"""
Junhui Park
IST
10 May 2024 
Database for Master Project
Period 1
"""

import mysql
import mysql.connector

class AuditionDb:
    def __init__(self):
        #connection flag
        self.connected = False
        self.records = []

        #lists for insert, update, sorted records, and the names
        self.insertRec = [" ", 0, 0, 0, 0, 0]
        self.updateRec = [0, " ", 0, 0, 0, 0, 0]
        self.sortedRec = []
        self.sortedName = []

    def connect(self):
        try:
            #mySQL connector
            self.sqlConnection = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Jjun0525?!",
                database = "audition_program",
                auth_plugin = "mysql_native_password"
            )
            #mySQL cursor
            self.cursor = self.sqlConnection.cursor(buffered = True)
            self.cursor.execute("SELECT * from audition")
            return ("Successfully Connected")

        except mysql.connector.Error as error:
            return("Failed to connect: ", error)
        
    def disconnect(self):
        #disconnect from mySQL
        if(self.sqlConnection):
            self.sqlConnection.disconnect()
            return ("Connection Closed")
    
    def load(self):
        try:
            #select all data in my database
            self.cursor.execute("SELECT * from audition")

            #insert records into self.records list
            self.records = self.cursor.fetchall()
            return ""
        except mysql.connector.Error as error:
            return("Error loading: ", error)
        
    def insert(self):
        try:
            #insert values that were put in the textboxes
            query = "INSERT INTO audition (studentName, instrument, etudeScore, sightReadingScore, totalScore) VALUES (%s, %s, %s, %s, %s);"
            
            #execute query
            self.cursor.execute(query, self.insertRec)
            self.sqlConnection.commit()

            #reload my datas
            self.load()
            return("Inserted Auditionee")
        except mysql.connector.Error as error:
            return("Error Inserting Score: ", error)

    def delete(self, deleteNumber):
        try:
            #delete data that corresponds to the id
            query = ("DELETE FROM audition WHERE Id = %s;")
            self.cursor.execute(query, (deleteNumber, ))
            self.sqlConnection.commit()

            #reload data
            self.load()
            return ("Deleted Auditionee")
        except mysql.connector.Error as error:
            return("Error deleting auditionee: ", error) 
        
    def updateCurrentRec(self):
        try:
            #update data based on the text input in textboxes
            query = ("UPDATE audition SET studentName ='" + self.updateRec[1] + "', instrument = '" + self.updateRec[2] + "', etudeScore = '" + str(self.updateRec[3]) + "', sightReadingScore = '" + str(self.updateRec[4])+ "', totalScore = '" + str(self.updateRec[5]) + "' WHERE ID = '" + str(self.updateRec[0]) + "';")
            
            #execute query
            self.cursor.execute(query)
            self.sqlConnection.commit()
            return("Updated Auditionee")
        except mysql.connector.Error as error:
            return("Error updating auditionee: ", error) 

    def getSortedList(self, instrument):
        try:
            #sort data based on the dropdown selection
            query = ("SELECT * FROM audition WHERE instrument = '" + instrument + "' ORDER BY totalScore DESC;")
            print(query)
            
            #execute query
            self.cursor.execute(query)

            #insert in my sortedRec list
            self.sortedRec = self.cursor.fetchall()
            return ("Sort Successful")
        except mysql.connector.Error as error:
            return("Error fetching sorted auditionee: ", error) 

    def getSortedStudentNames(self, instrument):
        try:
            #select the names of student that plays the instrument selected on the dropdown
            query = ("SELECT studentname FROM audition WHERE instrument = '" + instrument + "' ORDER BY totalScore DESC;")
            print(query)

            #execute query
            self.cursor.execute(query)

            #insert in my sortedName list
            self.sortedName = self.cursor.fetchall()
            print(self.sortedName)
            return str(self.sortedName)
        except mysql.connector.Error as error:
            return ("Error fetching sorted auditionee names: ", error)


        