import sqlite3

class DoctorLoginModel:
    @staticmethod
    def get_hashed_password(republic_of_turkey_id_card_no):
        conn = sqlite3.connect('Database/Database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT Password FROM Doctors WHERE RepublicOfTurkeyIDCardNo = ?', (republic_of_turkey_id_card_no,))
        result = cursor.fetchone()
        conn.close()
        if result:
            password = result[0].strip()
            print(f"Fetched password from DB: {password} (length: {len(password)})")
            return password
        else:
            print("No password found in DB for the given ID.")
            return None
