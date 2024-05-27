from Model.TestResultsModel import TestResultsModel

class ShowTestResultsController:
    @staticmethod
    def get_test_results(patient_id):
        results = TestResultsModel.get_test_results_by_patient_id(patient_id)
        return results
