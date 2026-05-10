import json
from jsonschema  import  validate


def Validate_schema(response_json,schema_path): # creating a validator for Schema
    with open(schema_path) as file:             # Opening Schema file
            schema = json.load(file)            # loading it as json(now we have the json file formate how out reponse should look like)


    validate(instance=response_json, schema=schema)  # validating the reponse we get and how it should look like with schema above from schema