# -*- coding: utf-8 -*-
import requests

# This is an example of how to use our API for communicating with
# our Named Entity Recognition model.

# First, please setup the endpoint URL provided for communicating with
# the Named Entity Recognition model.
# You can also copy the endpoint URL from the box "Request URL" after trying
# examples on our API documentation.
endpoint_url = "http://prm-ezcatdb.cbrc.jp/api/named_entity_recognition"

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
# Please check out the output data structure `NamedEntityRecognitionData` in
# our documentation for more details.

# Print out the document text.
print("Document Text: ", response["text"], "\n")

# Print out all predicted entities.
print("Predicted entities:\n")

for entity in response["entities"]:
    print(f'Entity ID: {entity["id"]}')
    print(f'Entity Type: {entity["type"]}')
    print(f'Entity Span: {entity["span"]}')
    print(f'Entity Mention Text: {entity["text"]}')
    # Or you can also obtain the entity mention text using span information.
    entity_mention_text = response["text"][
        entity["span"]["start"] : entity["span"]["end"]
    ]
    print(f"Entity Mention Text (using span information): {entity_mention_text}")
    print("===\n")

# This code below is to show segmented sentences and tokens of the document text

print("Segmented sentences:")

sentences = [
    response["text"][span["start"] : span["end"]]
    for span in response["sentence_boundaries"]
]

for sentence in sentences:
    print(sentence)

print("\nTokens:")

tokens = [
    response["text"][span["start"] : span["end"]]
    for span in response["token_boundaries"]
]

print(tokens)
