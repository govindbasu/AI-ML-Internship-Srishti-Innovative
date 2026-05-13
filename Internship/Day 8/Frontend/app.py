import streamlit as st
import tensorflow as tf
import numpy as np

from PIL import Image

# Load CNN Model

model = tf.keras.models.load_model(
    "brain_tumor_cnn_model.h5"
)

# Class Labels

class_names = [
    "Glioma",
    "Meningioma",
    "No Tumor",
    "Pituitary"
]

# Streamlit Frontend

st.title("Brain Tumor Detection System")

st.write(
    "Upload a Brain MRI image for prediction"
)

# Upload Image

uploaded_file = st.file_uploader(
    "Choose an MRI Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    # Display Uploaded Image

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded MRI Scan",
        use_container_width=True
    )

    # Resize Image

    image = image.resize((128,128))

    # Convert to Array

    image_array = np.array(image)

    # Normalize Image

    image_array = image_array / 255.0

    # Expand Dimensions

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    # Prediction

    prediction = model.predict(image_array)

    predicted_class = np.argmax(prediction)

    confidence = np.max(prediction)

    # Display Prediction

    st.subheader("Prediction Result")

    st.success(
        f"Predicted Tumor Type: {class_names[predicted_class]}"
    )

    st.info(
        f"Confidence Score: {confidence:.2f}"
    )