from Model.TestResultsModel import TestResultsModel

class ShowTestResultsController:
    @staticmethod
    def GetTestResults(patient_id):
        results = TestResultsModel.GetTestResultsByPatientId(patient_id)
        return results
