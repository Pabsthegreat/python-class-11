from boltiot import Bolt
api_key = "192bd761-87ff-4499-83c7-bdc17ec0dcba"
device_id  = "BOLT13166887"
mybolt = Bolt(api_key, device_id)
response = mybolt.isOnline()
print (response)