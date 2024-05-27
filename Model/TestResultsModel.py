import sqlite3

class TestResultsModel:
    @staticmethod
    def get_test_results_by_patient_id(patient_id):
        conn = sqlite3.connect('Database/Database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM TestResults WHERE PatientID = ?', (patient_id,))
        results = cursor.fetchall()
        conn.close()
        results_dict = {}
        if results:
            result = results[0]
            results_dict['hdl_cholesterol_human'] = result[1]
            results_dict['hemoglobin_hgb_human'] = result[2]
            results_dict['cholesterol_ldl_human'] = result[3]
        return results_dict
