# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for UpdateGateway
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-api-gateway


# [START apigateway_generated_apigateway_v1_ApiGatewayService_UpdateGateway_sync]
from google.cloud import apigateway_v1


def sample_update_gateway():
    # Create a client
    client = apigateway_v1.ApiGatewayServiceClient()

    # Initialize request argument(s)
    gateway = apigateway_v1.Gateway()
    gateway.api_config = "api_config_value"

    request = apigateway_v1.UpdateGatewayRequest(
        gateway=gateway,
    )

    # Make the request
    operation = client.update_gateway(request=request)

    print("Waiting for operation to complete...")

    response = operation.result()
    print(response)

# [END apigateway_generated_apigateway_v1_ApiGatewayService_UpdateGateway_sync]
