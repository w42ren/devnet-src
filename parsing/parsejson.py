# Fill in this file with the code from parsing JSON exercise
import json
import yaml
# Use the Python with statement to open myfile.json and set it to the variable name json_file. Then use the json.
# load method to load the JSON file into a string set to the variable name ourjson.
with open('myfile.json','r') as json_file:
    ourjson = json.load(json_file)
# Add a print statement for ourjson to see that it is now a Python dictionary
print(ourjson)
# Add print statements that display the token value 
# and how many seconds until the token expires
print(f"The access token is: {ourjson['access_token']}")
print(f"The token expires in {ourjson['expires_in']} seconds.")
# print ourjson as YAML data by using the dump() method of the yaml library. 
print("\n\n---")
print(yaml.dump(ourjson))


