import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

breed_list = ['chihuahua','japanese_spaniel','maltese_dog','pekinese','shih-tzu','blenheim_spaniel','papillon','toy_terrier',
    'rhodesian_ridgeback','afghan_hound','basset','beagle','bloodhound','bluetick','black-and-tan_coonhound','walker_hound',
    'english_foxhound','redbone','borzoi','irish_wolfhound','italian_greyhound','whippet','ibizan_hound','norwegian_elkhound',
    'otterhound','saluki','scottish_deerhound','weimaraner','staffordshire_bullterrier','american_staffordshire_terrier',
    'bedlington_terrier','border_terrier','kerry_blue_terrier','irish_terrier','norfolk_terrier','norwich_terrier','yorkshire_terrier',
    'wire-haired_fox_terrier','lakeland_terrier','sealyham_terrier','airedale','cairn','australian_terrier','dandie_dinmont',
    'boston_bull','miniature_schnauzer','giant_schnauzer','standard_schnauzer','scotch_terrier','tibetan_terrier','silky_terrier',
    'soft-coated_wheaten_terrier','west_highland_white_terrier','lhasa','flat-coated_retriever','curly-coated_retriever','golden_retriever',
    'labrador_retriever','chesapeake_bay_retriever','german_short-haired_pointer','vizsla','english_setter','irish_setter','gordon_setter',
    'brittany_spaniel','clumber','english_springer','welsh_springer_spaniel','cocker_spaniel','sussex_spaniel','irish_water_spaniel',
    'kuvasz','schipperke','groenendael','malinois','briard','kelpie','komondor','old_english_sheepdog','shetland_sheepdog',
    'collie','border_collie','bouvier_des_flandres','rottweiler','german_shepherd','doberman','miniature_pinscher','greater_swiss_mountain_dog',
    'bernese_mountain_dog','appenzeller','entlebucher','boxer','bull_mastiff','tibetan_mastiff','french_bulldog','great_dane',
    'saint_bernard','eskimo_dog','malamute','siberian_husky','affenpinscher','basenji','pug','leonberg','newfoundland','great_pyrenees',
    'samoyed','pomeranian','chow','keeshond','brabancon_griffon','pembroke','cardigan','toy_poodle','miniature_poodle','standard_poodle',
    'mexican_hairless','dingo','dhole','african_hunting_dog']

model = load_model('my_inception_model.h5')

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
int_class = int(predicted_class)
class_name = breed_list[int_class]
string = "\nPredicted Class: " + class_name
print(string)
print("Prediction Confidence: ", confidence_score)
