import os
from google.cloud import *
from google.cloud.vision import *


#the JSON file you downloaded in step 5 above
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'our-signal-331319-c2f3d33ae558.json'

def classify():
    # Instantiates a client
    client = ImageAnnotatorClient()

    #set this thumbnail as the url
    image = Image()
    with open('the_image.png', 'rb') as f:
        image.content = f.read()
    # image.source.image_uri = 'https://static01.nyt.com/images/2021/09/14/science/07CAT-STRIPES/07CAT-STRIPES-superJumbo.jpg?quality=75&auto=webp'

    #### LABEL DETECTION ######

    response_label = client.label_detection(image=image)

    temp = response_label.label_annotations[0].description
    prob = float(response_label.label_annotations[0].score)
    if(prob >= 0.5):
        return "I think the result is: " + temp
    else:
        return "I'm not sure what's in this picture. Try another one!"
