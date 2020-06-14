from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

import samplebot.config

# sample_transport = RequestsHTTPTransport(
#     url=samplebot.config.GRAPHQL_ENDPOINT,
#     verify=False,
#     retries=3,
# )

# client = Client(
#     transport=sample_transport,
#     fetch_schema_from_transport=True,
# )


# def load_something():
#     query = gql("")
#     return client.execute(query)
