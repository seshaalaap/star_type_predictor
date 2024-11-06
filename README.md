# Predicting Star Types with Machine Learning 🔭⭐🛸

This web application (https://mlstartypepredictor.streamlit.app/) allows the user to do the following:
1. Choose whether they want to generate type of a single star or multiple stars 
2. Tweak the values of various star attributes like temperature, radius, luminosity etc. for single type or upload a csv file (example provided) for bulk prediction
3. The program then uses Artificial Intelligence (specifically, logistic regression) to predict the star types using the entered values of the stars.

# Installation

This project is a Streamlit application for generating and predicting star data using a FastAPI backend.

## Prerequisites

Make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. **Clone the Repository**:

   Open your terminal and clone the repository:

   ```bash
   git clone https://github.com/yourusername/star-data-prediction-app.git
   cd star-data-prediction-app

2. **Install dependencies**:
   Create a virtual environment (optional but recommended) and install the required packages:

    For windows

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
    For linux or Mac
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   
   For windows
   ```bash
   venv\Scripts\activate
   ```
   For linux or Mac
   ```bash
   source venv/bin/activate
   ```
   
5. Install the requirements:
   
   For windows
   ```bash
   python -m pip install -r requirements.txt
   ```
   For linux or Mac
   ```bash
   pip install -r requirements.txt
   ```
   
7. Run the backend powered by FastAPI using Uvicorn:
   ```bash
   uvicorn backend:app
   ```

8. Run the frontend powered by Streamlit:
   ```bash
   streamlit run frontend.py
   ```



# Tools Used In This Project:
1. FastAPI - To build the API endpoints
2. Streamlit - To build and host the frontend of the web application
3. Render - To host the backend API built using FastAPI
4. NumPy - To create the synthetic dataset for training, validation, testing, and the web application
5. Matplotlib - To visualize the cost vs iterations and in the web application to visualize the regression line
6. Pandas - To read CSV files, create the dataframe, and save dataframes back to CSV
7. scikit-learn (sklearn) - To implement machine learning models and algorithms for training, evaluating, and making predictions in the web application. It provides tools for regression, classification, clustering, dimensionality reduction, and model evaluation, and is used to train models on the synthetic dataset and make predictions based on user inputs.




# Acknowledgements
Special thanks to the authors of the libraries used in this project! 

# Contact
For questions or support, please reach out to aalaapsesh@gmail.com



   



