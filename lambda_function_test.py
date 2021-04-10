import json
from unittest import TestCase
import unittest
from lambda_function import lambda_handler, requestUri

originRequestJson = 'cloudfront-origin-request.json'

class CloudfrontIndexRedirect(TestCase):
	def load_test_json(self, filename):
		with open('test/' + filename, 'r') as json_file:
			return json.loads(json_file.read())

	def test_origin_request(self):
		event = self.load_test_json(originRequestJson)
		self.assertTrue(len(event['Records']) > 0)
		self.assertTrue(event['Records'][0]['cf']['request'][requestUri])
		response = lambda_handler(event, None)
		expected = '/test/index.html'
		self.assertEqual(expected, response[requestUri])

	def test_origin_request_root(self):
		event = self.load_test_json(originRequestJson)
		event['Records'][0]['cf']['request'][requestUri] = '/'
		response = lambda_handler(event, None)
		expected = '/index.html'
		self.assertEqual(expected, response[requestUri])

	def test_origin_request_trailing_slash(self):
		event = self.load_test_json(originRequestJson)
		event['Records'][0]['cf']['request'][requestUri] = '/test/'
		response = lambda_handler(event, None)
		expected = '/test/index.html'
		self.assertEqual(expected, response[requestUri])

	def test_origin_request_index(self):
		event = self.load_test_json(originRequestJson)
		event['Records'][0]['cf']['request'][requestUri] = '/index.html'
		response = lambda_handler(event, None)
		expected = '/index.html'
		self.assertEqual(expected, response[requestUri])


	def test_origin_request_index_no_ext(self):
		event = self.load_test_json(originRequestJson)
		event['Records'][0]['cf']['request'][requestUri] = '/index'
		response = lambda_handler(event, None)
		expected = '/index.html'
		self.assertEqual(expected, response[requestUri])

if __name__ == '__main__':
	unittest.main()
