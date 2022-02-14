# -*- coding: utf-8 -*-
import requests

# This is an example of how to use our API for communicating with
# our Event Extraction model.

# First, please setup the endpoint URL provided for communicating with
# the Event Extraction model.
# You can also copy the endpoint URL from the box "Request URL" after trying
# examples on our API documentation.
endpoint_url = "http://prm-ezcatdb.cbrc.jp/api/event_extraction"

# Then, prepare your input data.
# Currently, we require your email address to know who is using our service.
# Please check out the input data structure `Doc` in our documentation for more details.
email = "example@domain.com"
document_text = (
    "While most sources agree that IPF does not result from a "
    "primary immunopathogenic mechanism, evidence gleaned from "
    "animal modeling and human studies suggests that innate and "
    "adaptive immune processes can orchestrate existing fibrotic responses."
)

# Then, send a request with your input data to the endpoint URL.
response = requests.post(
    url=endpoint_url, params={"email": email}, json={"text": document_text}
)

# We then convert the returned data into JSON format.
response = response.json()

# The code below is to show all returned information.
# Please check out the output data structure `EventExtractionData` in
# our documentation for more details.

# Print out the document text.
print("Document Text: ", response["text"], "\n")

# Print out all predicted events.
print("Predicted events:\n")

entities = {entity["id"]: entity for entity in response["entities"]}

for event in response["events"]:
    print(f'Event ID: {event["id"]}')
    print(f'Event Trigger ID: {event["trigger_id"]}')

    # Print all event's arguments.
    for argument in event["args"]:
        print(f'Argument ID (could be an event or entity ID): {argument["arg_id"]}')
        print(f'Argument role: {argument["arg_role"]}')

    # Print all event's modalities.
    for modality in event["modalities"]:
        print(f'Modality ID: {modality["id"]}')
        print(f'Modality Type: {modality["type"]}')

    print("===\n")
