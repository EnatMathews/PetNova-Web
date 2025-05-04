import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


# import tensorflow as tf
# load_model = tf.keras.models.load_model
# image = tf.keras.preprocessing.image

print("///////////////////////")

def predicts(img_path):
    # Load the trained model
    model_path = 'dog_skin_disease_prediction_model_vgg16_updated.h5'

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")

    # Load the model, ensuring no custom objects are included
    try:
        model = load_model(model_path, compile=False)  # Setting compile=False to avoid loading optimizer
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

    print("////////////////////////")

    # Define the image file you want to predict
    image_file = img_path

    if not os.path.exists(image_file):
        raise FileNotFoundError(f"Image file not found at {image_file}")

    # Load and preprocess the image
    img = image.load_img(image_file, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0

    # Perform prediction
    predictions = model.predict(img_array)

    # Get the predicted class label
    predicted_class = np.argmax(predictions)

    # Class labels dictionary
    class_labels = {
        0: 'bacterial', 
        1: 'flea_allergy', 
        2: 'fleas', 
        3: 'fungus', 
        4: 'healthy', 
        5: 'hotspot', 
        6: 'hypersensitivity', 
        7: 'mange', 
        8: 'ringworm'
    }
    predicted_label = class_labels.get(predicted_class, "Unknown class")

    print("Predicted class:", predicted_label)
    
    return predicted_label

# Example usage
# print(predicts("path_to_your_image.jpg"))
