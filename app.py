import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

# Initialize FastAPI application
app = FastAPI(title="Iris Species Prediction API")

# Enable CORS for browser access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your pre-trained SVC model
try:
    model = joblib.load("svc.pkl")
    print("Model loaded successfully!")
except FileNotFoundError:
    raise RuntimeError("Model file 'svc.pkl' not found. Please run your training script first.")

# Define species mappings
SPECIES_MAPPING = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}

# Define the input schema
class FlowerMeasurements(BaseModel):
    sepal_length: float = Field(..., description="Sepal length in cm", example=5.1)
    sepal_width: float = Field(..., description="Sepal width in cm", example=3.5)
    petal_length: float = Field(..., description="Petal length in cm", example=1.4)
    petal_width: float = Field(..., description="Petal width in cm", example=0.2)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Prediction API!"}

# Prediction endpoint
@app.post("/predict")
def predict_species(data: FlowerMeasurements):
    # Convert input payload into a 2D array matching the model's training shape
    input_features = np.array([[
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]])
    
    try:
        # Generate numeric prediction
        prediction_id = int(model.predict(input_features)[0]) # Added index [0] safely
        
        # Map the numeric outcome to the actual flower string label
        species_name = SPECIES_MAPPING.get(prediction_id, "unknown")
        
        return {
            "prediction_id": prediction_id,
            "predicted_species": species_name
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")
