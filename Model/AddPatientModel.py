import sqlite3

class AddPatientModel:
    @staticmethod
    def AddPatient(republic_of_turkey_id_card_no, name, age, condition, sex):
        conn = sqlite3.connect('Database/Database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Patients (RepublicOfTurkeyIDCardNo, Name, Age, Condition, Sex) VALUES (?, ?, ?, ?, ?)
        ''', (republic_of_turkey_id_card_no, name, age, condition, sex))
        patient_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return patient_id
