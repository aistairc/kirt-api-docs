# -*- coding: utf-8 -*-
import requests

# This is an example of how to use our API for checking the server status.

# Sometimes, our server is very busy processing other requests in the queue
# so it may take you a long time to get the response. In this case, you don't
# know whether our service is down or still working. So we provide this API to
# give you more information about our current server health.

# First, please setup the endpoint URL provided for checking API server status.
# You can also copy the endpoint URL from the box "Request URL" after trying
# examples on our API documentation.
endpoint_url = "http://prm-ezcatdb.cbrc.jp/api/status"

# We will send a request to the endpoint.
response = requests.get(url=endpoint_url)

# Then, convert the returned data into JSON format.
response = response.json()

# Show the server status.
# If the server is still working normally, the received status should be "Running".
print(response)
