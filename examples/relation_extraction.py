# -*- coding: utf-8 -*-
import requests

# This is an example of how to use our API for communicating with
# our Relation Extraction model.

# First, please setup the endpoint URL provided for communicating with
# the Relation Extraction model.
# You can also copy the endpoint URL from the box "Request URL" after trying
# examples on our API documentation.
endpoint_url = "http://prm-ezcatdb.cbrc.jp/api/relation_extraction"

# Then, prepare your input data.
# Currently, we require your email address to know who is using our service.
# Please check out the input data structure `Doc` in our documentation for more details.
email = "example@domain.com"
document_text = (
    "BACKGROUND: Fibroblastic foci are characteristic features in "
    "lung parenchyma of patients with idiopathic pulmonary fibrosis (IPF)."
)

# Then, send a request with your input data to the endpoint URL.
response = requests.post(
    url=endpoint_url, params={"email": email}, json={"text": document_text}
)

# We then convert the returned data into JSON format.
response = response.json()

# The code below is to show all returned information.
# Please check out the output data structure `RelationExtractionData` in
# our documentation for more details.

# Print out the document text.
print("Document Text: ", response["text"], "\n")

# Print out all predicted relations.
print("Predicted relations:\n")

entities = {entity["id"]: entity for entity in response["entities"]}

for relation in response["relations"]:
    # Get entity object using its ID.
    left_arg_entity = entities[relation["left_arg_id"]]
    right_arg_entity = entities[relation["right_arg_id"]]

    print(f'Relation ID: {relation["id"]}')
    print(f'Relation Type: {relation["type"]}')
    print(f"Left entity: {left_arg_entity}")
    print(f"Right entity: {right_arg_entity}")
    print("===\n")
