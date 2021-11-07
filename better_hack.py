import os
from google.cloud import *
from google.cloud.vision import *


#the JSON file you downloaded in step 5 above
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'our-signal-331319-c2f3d33ae558.json'

# Instantiates a client
client = ImageAnnotatorClient()

#set this thumbnail as the url
with open('the_image.png', 'rb') as f:
    image = Image(f.read())
# image.source.image_uri = 'http://127.0.0.1:5000/static/the_image.png'

#### LABEL DETECTION ######

response_label = client.label_detection(image=image)

temp = response_label.label_annotations.values()#["label"]
print(temp)






#byebye
for label in response_label.label_annotations:
    print({'label': label.description, 'score': label.score})


#### FACE DETECTION ######

response_face = client.face_detection(image=image)

face_data = []

for face_detection in response_face.face_annotations:
    d = {
        'confidence': face_detection.detection_confidence,
        'joy': face_detection.joy_likelihood,
        'sorrow': face_detection.sorrow_likelihood,
        'surprise': face_detection.surprise_likelihood,
        'anger': face_detection.anger_likelihood
    }
    print(d)
    

#### IMAGE PROPERTIES ######

response_image = client.image_properties(image=image)

image_data = []

for c in response_image.image_properties_annotation.dominant_colors.colors[:3]:
    d = {
        'color': c.color,
        'score': c.score,
        'pixel_fraction': c.pixel_fraction
    }
    print(d)


#### TEXT DETECTION ######

response_text = client.text_detection(image=image)

for r in response_text.text_annotations:
    d = {
        'text': r.description
    }
    print(d)
