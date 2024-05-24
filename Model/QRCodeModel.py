import sqlite3

class QrCodeModel:
    @staticmethod
    def SaveQrCodeData(patient_id, qr_data):
        conn = sqlite3.connect('Database/Database.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO QrCodes (PatientID, QrData) VALUES (?, ?)
        ''', (patient_id, qr_data))
        conn.commit()
        conn.close()
