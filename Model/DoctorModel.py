import sqlite3
import hashlib

class DoctorModel:
    @staticmethod
    def authenticate(id_card_no, password):
        conn = sqlite3.connect('Database/Database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT Password FROM Doctors WHERE RepublicOfTurkeyIDCardNo = ?", (id_card_no,))
        result = cursor.fetchone()
        conn.close()
        if result:
            stored_password = result[0]
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            return stored_password == hashed_password
        return False
