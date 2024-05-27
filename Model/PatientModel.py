import sqlite3

class PatientModel:
    @staticmethod
    def get_all_patients():
        conn = sqlite3.connect('Database/Database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT RepublicOfTurkeyIDCardNo, PatientID, Condition, Age, Name, Sex FROM Patients')
        patients = cursor.fetchall()
        conn.close()
        return patients
