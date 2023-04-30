import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

def predict(image_path):
    # Load saved model
    model = load_model('my_inception_model.h5') # Replace with path to your saved model

    # Preprocess image
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    # Make prediction
    predictions = model.predict(x)
    predicted_class_index = np.argmax(predictions)
    predicted_class = str(predicted_class_index)
    confidence_score = str(predictions[0][predicted_class_index])

    return [predicted_class, confidence_score]

model = load_model('my_inception_model.h5') # Replace with path to your saved model

# Preprocess image
img = image.load_img("image.jpg", target_size=(224, 224))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = x / 255.0

# Make prediction
predictions = model.predict(x)
predicted_class_index = np.argmax(predictions)
predicted_class = str(predicted_class_index)
confidence_score = str(predictions[0][predicted_class_index])
class_pred = int(predicted_class)
string = "Predicted Class: " + predicted_class + "\t\tPrediction Confidence Score: " + confidence_score
with open('output.txt', 'w') as f:
    string_to_write = string
    f.write(string_to_write)