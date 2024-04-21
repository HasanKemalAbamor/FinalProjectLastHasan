import sqlite3

class AddPatientModel:


    @staticmethod
    def AddPatient(RepublicOfTurkeyIDCardNo):

            conn = sqlite3.connect('Database/Database.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO Patients (RepublicOfTurkeyIDCardNo) VALUES (?)
            ''', (RepublicOfTurkeyIDCardNo,))

            conn.commit()
            conn.close()


