import joblib
import pandas as pd
import numpy as np
from PIL import Image
import io

class GraphUploadController:
    def __init__(self):
        self.model = joblib.load('trained72')  # Load the trained machine learning model

    def upload_graph(self, graph_data):
        # Placeholder for saving graph data to database
        # GraphModel.save_graph_data(patient_id, graph_data)
        return True, "Graph uploaded successfully."

    def process_graph(self, graph_image):
        # Convert image bytes to a numpy array
        image = Image.open(io.BytesIO(graph_image))
        image_array = np.array(image)

        # Debug: Check image properties
        print(f"Image format: {image.format}, size: {image.size}, mode: {image.mode}")

        # Preprocess the image as needed by your model
        try:
            preprocessed_data = self.preprocess_image(image_array)
            prediction = self.model.predict(preprocessed_data)
            return prediction
        except ValueError as e:
            print(f"Error in preprocessing data: {e}")
            return None

    def preprocess_image(self, image_array):
        # Convert the image to grayscale
        image = Image.fromarray(image_array).convert('L')

        # Resize the image to 13x13 pixels using LANCZOS resampling
        image = image.resize((13, 13), Image.Resampling.LANCZOS)
        resized_image_array = np.array(image).flatten() / 255.0

        # Ensure the data matches the expected input shape of the model
        if len(resized_image_array) != 169:
            raise ValueError(f"Expected 169 features after resizing, but got {len(resized_image_array)}")

        # Create a data dictionary with feature names
        data_dict = {f'absorbance_{i+1}': val for i, val in enumerate(resized_image_array)}
        df = pd.DataFrame([data_dict])

        # Reorder columns to match the order used during model training
        required_columns = [f'absorbance_{i+1}' for i in range(172)]
        # Padding the DataFrame to have 172 features if necessary
        for col in required_columns:
            if col not in df:
                df[col] = 0.0

        return df[required_columns].values  # Ensure this is a 2D numpy array
