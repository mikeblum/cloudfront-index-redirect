#!/usr/bin/env python3

from os import path

requestUri = 'uri'
 
def lambda_handler(event, context):
    """
    https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-query-string-examples
    """
    request = event['Records'][0]['cf']['request']
    uri = request[requestUri]
    request[requestUri] = path.join(uri, 'index.html')
    return request
