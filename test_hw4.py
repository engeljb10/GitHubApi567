import unittest
import hw4
from unittest import mock


class testGithub(unittest.TestCase):

	@mock.patch("hw4.getGithubInfo")
	def test_Github(self, mock_github):
		engeljrepos = hw4.getGithubInfo("engeljb10")
		mock_github.return_value = ["repo1", "repo2","repo3", "repo4"]
		assert "repo1" in repos
		assert "repo2" in repos


if __name__ == '__main__':
	unittest.main()