from clarifai import rest
from clarifai.rest import ClarifaiApp

app = ClarifaiApp(api_key='1f2c93de75074a088597cd7791491b5a')
model = app.public_models.general_model
response = model.predict_by_url('https://samples.clarifai.com/metro-north.jpg')

# print(response['outputs'][0]['data']['concepts'])

name_map = []
for dict_item in response['outputs'][0]['data']['concepts']:
	name_map.append([dict_item['name'], dict_item['value']])
for item in name_map:
	print(item)
