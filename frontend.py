import streamlit as st
import requests
import pandas as pd
from io import StringIO

# API endpoints for single and bulk predictions
single_predict_url = "https://star-type-predictor.onrender.com/predict/"
bulk_predict_url = "https://star-type-predictor.onrender.com/bulk_predict/"


# Set up the Streamlit app configuration
st.set_page_config(
    page_title="Star Type Predictor",
    page_icon="https://wallpapers.com/images/high/purple-shooting-star-emoji-bn1vl8bevshzxif4.png",  # Icon for the app
)

# Custom CSS for the app's background and styling
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/5eae36e3-278f-4731-be00-1440d36eca76/d30idy4-9a4a96ed-33be-4941-99c1-8b77adb23288.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwic3ViIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsImF1ZCI6WyJ1cm46c2VydmljZTpmaWxlLmRvd25sb2FkIl0sIm9iaiI6W1t7InBhdGgiOiIvZi81ZWFlMzZlMy0yNzhmLTQ3MzEtYmUwMC0xNDQwZDM2ZWNhNzYvZDMwaWR5NC05YTRhOTZlZC0zM2JlLTQ5NDEtOTljMS04Yjc3YWRiMjMyODguanBnIn1dXX0.urB7x7zyDCCRhro0z1HDVMWXZ9HJi9NgdXurlCon43Q");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

[data-testid="stAppViewContainer"] > .main {
    backdrop-filter: blur(5px);  # Apply a blur effect to the main container
}
</style>
'''

# Inject the custom CSS for background
st.markdown(page_bg_img, unsafe_allow_html=True)

# Title of the application
st.markdown("<h1 style='color:cyan;'>🌌 Star Type Predictor 🌠</h1>", unsafe_allow_html=True)

# Dropdown for page selection
page = st.selectbox("Choose a page:", ["Introduction", "Single Prediction Mode", "Bulk Prediction Mode"])

# Introduction section with styled background
if page == "Introduction":
    with st.container():
        st.markdown("""
        <div style='background-color: rgba(200, 230, 255, 0.8); padding: 20px; border-radius: 10px;'>
            <h3 style='color: teal;'>Introduction to Project</h3>
            <p style='color:black;'><b>This web application is designed to help you predict the type of stars based on their physical parameters. Using machine learning models, we analyze key attributes of stars, such as <u>temperature</u>, <u>luminosity</u>, <u>radius</u>, and <u>absolute magnitude</u>, to classify them into different types.</b></p>
        </div>
        """, unsafe_allow_html=True)



    st.text(" ")  # Add spacing

    # Importance section with information on usage
    with st.container():
        st.markdown("""
        <div style='background-color: rgba(230, 230, 250, 0.8); padding: 20px; border-radius: 10px;'>
            <h3 style='color: darkblue;'>How to Use This Web Application?</h3>
            <ul style='font-size: 16px; color:black;'>
                <li>
                    <strong>Kindly select either Single Prediction Mode or Bulk Prediction Mode from the dropdown given above.
                <li>
                    <strong>Single Prediction will predict the type of a single star based on listed properties.
                </li>
                <li>
                    <strong>Bulk Prediction will predict the type of multiple stars based on properties provided in CSV file
                </li>
                <li>
                    <strong>Respective page shall guide you more about how to use it.
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.text(" ")  # Add spacing

    # Call to action to start using the app
    with st.container():
        st.markdown("""
        <div style='background-color: rgba(220, 255, 220, 0.8); padding: 20px; border-radius: 10px;'>
            <h3 style='color: purple;'>Get Started...</h3>
            <p style='color:black;'><b>Select either the Single or Bulk Prediction mode from the menu to begin exploring the stars!</b></p>
        </div>
        """, unsafe_allow_html=True)

# Single Prediction Page content
elif page == "Single Prediction Mode":

    # Information section about single prediction
    with st.container():
        st.markdown(
            """
            <div style='background-color: rgba(255, 205, 255, 0.8); padding: 20px; border-radius: 10px;'>
                <h3 style='color: maroon;'>Single Star Type Predictor Mode:</h3>
                <ul style='font-size: 16px; color: black;'>
                    <li>
                        <strong>Provide properties of the star to predict its type!
                    </li>
                    <li>
                        <strong>The default values are for our Solar System's Sun. You can modify these to analyze other stars.
                    </li>
                    <li>
                        <strong>Click the 'Predict' button to get the predicted star type.
                    </li>
                    <li>
                        <strong>Green (strong), Yellow (average), and Red (poor) status shows the confidence level of the model.
                    </li>
                </ul>
            </div>
            """, 
            unsafe_allow_html=True
        )

    st.text(" ")  # Add spacing

    # Input fields for user to enter star parameters
    temperature = st.number_input("Temperature (K):-", min_value=0, step=1, value=5770)
    luminosity = st.number_input("Luminosity wrt Sun (L/Lo):-", min_value=0.0, step=0.01, value=1.0)
    radius = st.number_input("Radius wrt Sun (R/Ro):-", min_value=0.0, step=0.01, value=1.0)
    magnitude = st.number_input("Absolute magnitude (Mv):-", step=0.01, value=4.83)

    # Button to trigger the prediction
    if st.button("Predict"):
        # Prepare the payload for the API request with input parameters
        payload = {
            "Temperature (K)": temperature,
            "Luminosity(L/Lo)": luminosity,
            "Radius(R/Ro)": radius,
            "Absolute magnitude(Mv)": magnitude
        }

        # Send a POST request to the prediction API
        try:
            response = requests.post(single_predict_url, json=payload)

            # Check if the API request was successful
            if response.status_code == 200:
                result = response.json()  # Parse the JSON response
                predicted_type = result.get("predicted_type")  # Get predicted star type
                probability = result.get("predicted_probability")  # Get predicted probability

                # Create a dynamic container for displaying prediction results
                with st.container():
                    if probability >= 0.47:
                        background_color = "rgba(76, 175, 80, 0.8)"  # Green for strong predictions
                        text_color = "white"
                        message = "Predicted Star Type: " + predicted_type
                    elif 0.27 <= probability < 0.47:
                        background_color = "rgba(255, 235, 59, 0.8)"  # Yellow for average predictions
                        text_color = "black"
                        message = "Predicted Star Type: " + predicted_type
                    else:
                        background_color = "rgba(244, 67, 54, 0.8)"  # Red for low confidence poor predictions
                        text_color = "white"
                        message = "Predicted Star Type: " + predicted_type

                    # Display the prediction result with appropriate styling
                    st.markdown(
                        f"""
                        <div style='background-color: {background_color}; padding: 10px 0px 1px 10px; border-radius: 10px;'>
                            <p style='color: {text_color};'>{message}</p>
                        </div>
                        """, 
                        unsafe_allow_html=True
                    )
                
            else:
                # Display error message if prediction fails
                st.error(f"Error: Unable to get prediction. Status code {response.status_code}")
        except Exception as e:
            # Handle exceptions and display an error message
            st.error(f"An error occurred: {str(e)}")

# Bulk Prediction Page content
elif page == "Bulk Prediction Mode":
    
    # Container with instructions for bulk prediction
    with st.container():
        st.markdown(
            """
            <div style='background-color: rgba(200, 170, 220, 0.8); padding: 20px; border-radius: 10px; color:black;'>
                <h3 style='color: purple;'>Multiple Star Type Predictor Mode</h3>
                <p style='color: black;'><b>Upload a CSV file with the following features:</b></p> 
                    <li>
                        <strong>Temperature (K)</strong>
                    </li>
                    <li> 
                        <strong>Luminosity (L/Lo)</strong>
                    </li>
                    <li>
                        <strong>Radius (R/Ro)</strong>
                    </li>
                    <li>
                        <strong>Absolute Magnitude (Mv)</strong>
                    </li>
                <p> </p>
                <p><b>The system will analyze and return a CSV file with predicted star types for each entry.</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.text(" ")  # Add spacing

    # Container for downloading example dataset
    with st.container():
        st.markdown(
            """
            <div style='background-color: rgba(255, 230, 153, 0.8); padding: 20px; border-radius: 10px; color:black;'>
                <h4 style='color: darkred;'>Sample Dataset</h4>
                <p style='color: black;'><b>If you don't have a dataset, you can download the given sample dataset and try this service.</b></p>
                <a href="https://drive.google.com/uc?id=1-q0J3TAJdz5n1mth6Ihtmpc3jez_FT4I" download>
                    <button style='background-color: black; color: white; border: none; padding: 10px; border-radius: 5px;'>Download Dataset</button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.text(" ")  # Add spacing

    # File uploader for users to upload their CSV file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    # Automatically trigger bulk prediction when a file is uploaded
    if uploaded_file is not None:
        try:
            # Send the CSV file to the FastAPI bulk_predict endpoint
            response = requests.post(
                bulk_predict_url,
                files={"file": uploaded_file.getvalue()}  # Get the file content for the POST request
            )

            # Check if the request was successful
            if response.status_code == 200:
                # Convert response to a DataFrame and display results
                output_df = pd.read_csv(StringIO(response.content.decode('utf-8')))
                st.markdown("<h4 style='color:red;'>Predicted Results:-</h4>", unsafe_allow_html=True)
                st.dataframe(output_df)  # Display the resulting predictions as a DataFrame
            else:
                # Display error message if bulk prediction fails
                st.error(f"Error: Unable to get predictions. Status code {response.status_code}")
        except Exception as e:
            # Handle exceptions and display an error message
            st.error(f"An error occurred: {str(e)}")

# Add a container for the note about cold start problem
with st.container():
    st.markdown(
        """
        <div style='background-color: rgba(255, 255, 224, 0.8); padding: 20px; border-radius: 10px;'>
            <p style='color: black;'><strong>Note:</strong> If the app is idle for >15 minutes, it may take time to generate values. This is known as the <a href='https://en.wikipedia.org/wiki/Cold_start_(computing)' target='_blank' style='color: blue;'>cold start problem</a>.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Footer at the bottom of the app
footer = """
<div style='position: fixed; left: 0; bottom: 0; width: 100%; background-color: white; text-align: center; padding: 10px;'>
    <p style='color: black; margin: 0;'>This project is developed by <b>Aalaap Seshanand</b> as part of the <b>ML for Astronomy</b> Training Program at <b>Spartificial</b>.</p>
</div>
"""

# Inject the footer using markdown
st.markdown(footer, unsafe_allow_html=True)
