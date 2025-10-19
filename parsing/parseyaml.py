# Fill in this file with the code from parsing YAML exercise
import json
import yaml
with open('myfile.yaml','r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)
print(ouryaml)
print(f"The access token is {ouryaml['access_token']}")
print(f"The token expires in {ouryaml['expires_in']} seconds.")
print("\n\n")
print(json.dumps(ouryaml, indent=4))
