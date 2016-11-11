
import requests
from yaml import load
from basesetup import basedefault

class Testdeleteissue(basedefault):
	
		def setUp(self):
			super(Testdeleteissue, self).setUp()
			self.url = self.base_url + '/issue/'

		def test_delete_issue(self):
			issue_id = self.newissue()

			r = requests.delete(self.url + issue_id, cookies=self.cookies )
			self.assertEquals(r.status_code, 200)

			r = requests.get(self.url + issue_id, cookies=self.cookies)
			self.assertEquals(r.status_code, 404)

