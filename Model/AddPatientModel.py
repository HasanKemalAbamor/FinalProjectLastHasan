import sqlite3

class AddPatientModel:
    @staticmethod
    def add_patient(republic_of_turkey_id_card_no, name, age, condition, sex, email):
        conn = sqlite3.connect('Database/Database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Patients (RepublicOfTurkeyIDCardNo, Name, Age, Condition, Sex, Email) 
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (republic_of_turkey_id_card_no, name, age, condition, sex, email))
        conn.commit()
        conn.close()
