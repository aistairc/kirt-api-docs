# -*- coding: utf-8 -*-
import requests

# This is an example of how to use our API for communicating with
# our Disease Network.

# First, please setup the corresponding endpoint URLs for Entity Linking,
# Event Extraction, Disease Network models.
# In the Disease Network, we require both outputs from the Entity Linking
# and Event Extraction models to be able to generate the graph data.

# You can also copy the endpoint URLs from the box "Request URL" after trying
# examples on our API documentation.
event_extraction_endpoint = "http://prm-ezcatdb.cbrc.jp/api/event_extraction"
entity_linking_endpoint = "http://prm-ezcatdb.cbrc.jp/api/entity_linking"
disease_network_endpoint = "http://prm-ezcatdb.cbrc.jp/api/disease_network"

# Then, prepare your input data.
# Currently, we require your email address to know who is using our service.
# Please check out the input data structure `DiseaseNetworkDoc` in our documentation
# for more details.
email = "example@domain.com"

# In the Disease Network, we usually want to generate the graph data for
# multiple documents. So we prepare a list of 3 documents for example.
document_text_1 = (
    "METHODS: A549 cells were examined for evidence of EMT "
    "after treatment with TGF-beta1."
)
document_text_2 = (
    "OBJECTIVES: Matrix metalloproteinase-8 (MMP-8) promotes "
    "lung fibrotic responses to bleomycin in mice."
)
document_text_3 = "Active MMP-8 is the main form elevated in IPF lungs."

documents = [document_text_1, document_text_2, document_text_3]

# First, we need to obtain the outputs from the Entity Linking and
# Event Extraction models
disease_network_inputs = []

for document in documents:
    event_extraction_response = requests.post(
        url=event_extraction_endpoint, params={"email": email}, json={"text": document}
    ).json()

    entity_linking_response = requests.post(
        url=entity_linking_endpoint, params={"email": email}, json={"text": document}
    ).json()

    # Then, prepare input data for the Disease Network
    disease_network_inputs.append(
        {
            "entities": event_extraction_response["entities"],
            "events": event_extraction_response["events"],
            "linked_entities": entity_linking_response["entities"],
        }
    )

# After that, we send a request with the prepared input data
# to the endpoint URL of the Disease Network.
disease_network_response = requests.post(
    url=disease_network_endpoint, params={"email": email}, json=disease_network_inputs
)

# We then convert the returned data into JSON format.
disease_network_response = disease_network_response.json()

# The code below is to show all returned information.
# Please check out the output data structure `DiseaseNetworkData` in
# our documentation for more details.

# Print the graph data generated for the Disease Network
print("Graph Data: ", disease_network_response["graph_data"])

# We also provide 2 web applications for visualize the graph data in 2D and 3D
# So please write it down as an HTML file and open it on a web browser
with open("2d_visualization.html", mode="w", encoding="UTF-8") as f:
    f.write(disease_network_response["visualization_2d"])

with open("3d_visualization.html", mode="w", encoding="UTF-8") as f:
    f.write(disease_network_response["visualization_3d"])
