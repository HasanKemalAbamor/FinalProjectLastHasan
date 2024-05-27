import joblib
import pandas as pd
import numpy as np
from PIL import Image
import io
import matplotlib.pyplot as plt

class GraphController:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def upload_graph(self, patient_id, graph_data):
        return True, "Graph uploaded successfully."

    def process_graph(self, graph_image):
        image = Image.open(io.BytesIO(graph_image))

        # Debug: Check if image is opened correctly
        print(f"Image format: {image.format}, size: {image.size}, mode: {image.mode}")

        # Convert image to numpy array
        graph_array = np.array(image)

        # Extract data from graph (assuming line graph with absorbance data)
        # This is a placeholder. Actual implementation will depend on the graph format
        extracted_data = self.extract_data_from_graph(graph_array)

        if extracted_data is None:
            print("Graph not readable")
            return None

        try:
            preprocessed_data = self.preprocess_data(extracted_data)
            prediction = self.model.predict(preprocessed_data)
            return prediction
        except ValueError as e:
            print(f"Error in preprocessing data: {e}")
            return None

    def extract_data_from_graph(self, graph_array):
        # Placeholder for graph data extraction
        # Implement the actual logic to extract numeric data from the graph
        numeric_values = self.dummy_graph_data()
        return numeric_values

    def preprocess_data(self, data):
        numeric_values = [float(val) for val in data.split(',')]

        if len(numeric_values) != 172:
            raise ValueError(f"Expected 172 features, but got {len(numeric_values)}")

        data_dict = {f'absorbance_{i+1}': val for i, val in enumerate(numeric_values)}
        df = pd.DataFrame([data_dict])

        required_columns = [f'absorbance_{i+1}' for i in range(172)]
        df = df[required_columns]

        return df.values

    def dummy_graph_data(self):
        # Return dummy data matching the format expected by the model
        return ','.join([str(np.random.random()) for _ in range(172)])
