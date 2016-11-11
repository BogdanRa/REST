import requests
import unittest
from yaml import load # method for read file and compl it in dictionary
from basesetup import basedefault


class TestCreateIssue(basedefault):
		
		def setUp(self):
			super(TestCreateIssue, self).setUp()
			self.url = self.base_url + '/issue/'

		def test_new_issue(self):
			
			params = {
				'project': 'API',
				'summary': 'test summary from robots',
				'description': 'Hail the robots'
			}

			r = requests.put(self.url, data=params,  cookies=self.cookies)
			issue_id = r.headers['location'].split('/')[-1]  # get issue ID

			self.assertEquals(r.status_code, 201)

			urlid = requests.get(self.url + issue_id, cookies=self.cookies)
			self.assertEquals(urlid.status_code, 200) # verification issue ID