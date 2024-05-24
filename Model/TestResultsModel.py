import sqlite3

class TestResultsModel:
    @staticmethod
    def GetTestResultsByPatientId(patient_id):
        conn = sqlite3.connect('Database/Database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM TestResults WHERE PatientID = ?', (patient_id,))
        results = cursor.fetchall()
        conn.close()
        return results
