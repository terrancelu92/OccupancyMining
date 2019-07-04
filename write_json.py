# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 09:38:28 2019

@author: Xing Lu
"""
import json

# Enter your keys/secrets as strings in the following fields
credentials = {}  
credentials['CONSUMER_KEY'] = 'QDXHXHWlSEAK4ppzKF8KFjx2H'
credentials['CONSUMER_SECRET'] = '65qvxDHGexHPwM1OihSzB1BvzWFUAtOGOAyVu2esB9MrcJ5ZNK'
credentials['ACCESS_TOKEN'] = '865051271874703360-SPJoymFo01UVKssI5t7RJWbpcLAWi4L'
credentials['ACCESS_SECRET'] = 'dppOvmVmuMd3J8dhLqz5EqGqi16FnwisyfmkCtOT9oe93'

# Save the credentials object to file
with open("twitter_credentials.json", "w") as file:  
    json.dump(credentials, file)