#!/usr/bin/env python3

from os import path
from re import search

requestUri = 'uri'
 
def lambda_handler(event, context):
    """
    https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-query-string-examples
    """
    request = event['Records'][0]['cf']['request']
    uri = request[requestUri]
    root, ext = path.splitext(uri)
    if ext:
        """
        no-op on explicit url lookups for robots.txt, sitemap.xml, or index.html itself
        """
        return request
    elif search('index$', uri):
        request[requestUri] = uri  + '.html'
    else:
        request[requestUri] = path.join(uri, 'index.html')
    return request
