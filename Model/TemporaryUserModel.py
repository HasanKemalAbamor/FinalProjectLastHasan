import sqlite3
import hashlib
import random
import string

class TemporaryUserModel:
    @staticmethod
    def GeneratePassword():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

    @staticmethod
    def CreateTemporaryUser(republic_of_turkey_id_card_no, patient_id):
        conn = sqlite3.connect('Database/Database.db')
        cursor = conn.cursor()
        password = TemporaryUserModel.GeneratePassword()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute('''
            INSERT INTO TemporaryUsers (RepublicOfTurkeyIDCardNo, Password, PatientID) VALUES (?, ?, ?)
        ''', (republic_of_turkey_id_card_no, hashed_password, patient_id))
        conn.commit()
        conn.close()
        return password

    @staticmethod
    def AuthenticateTemporaryUser(republic_of_turkey_id_card_no, password):
        conn = sqlite3.connect('Database/Database.db')
        cursor = conn.cursor()
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        cursor.execute('''
            SELECT * FROM TemporaryUsers WHERE RepublicOfTurkeyIDCardNo = ? AND Password = ?
        ''', (republic_of_turkey_id_card_no, hashed_password))
        user = cursor.fetchone()
        conn.close()
        return user
