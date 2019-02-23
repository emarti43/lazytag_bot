
from clarifai import rest
from clarifai.rest import ClarifaiApp

import sys

app = ClarifaiApp(api_key='1f2c93de75074a088597cd7791491b5a')
model = app.public_models.general_model

if (len(sys.argv) < 2):
    print ("Use random image.")
    response = model.predict_by_url('https://www.galleschevy.com/assets/misc/6132/646066.jpg')
else:
    response = model.predict_by_url(sys.argv[1])

#response = model.predict_by_url('https://i.redd.it/640h9vc5gjf21.jpg')
#response = model.predict_by_filename('~/yay')

name_map = []
for dict_item in response['outputs'][0]['data']['concepts']:
	name_map.append([dict_item['name'], dict_item['value']])
for item in name_map:
	print(item)
