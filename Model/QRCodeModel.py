import sqlite3

class QRCodeModel:
    @staticmethod
    def save_qr_data(patient_id, qr_data):
        conn = sqlite3.connect('Database/Database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO QRCodes (PatientID, QrData) VALUES (?, ?)", (patient_id, qr_data))
        conn.commit()
        conn.close()

    @staticmethod
    def get_qr_data(patient_id):
        conn = sqlite3.connect('Database/Database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT QrData FROM QRCodes WHERE PatientID = ?", (patient_id,))
        qr_data = cursor.fetchone()
        conn.close()
        return qr_data
