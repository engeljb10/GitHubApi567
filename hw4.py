import urllib.request
import json
import time


def getGithubInfo():
	with urllib.request.urlopen(repoLink) as url:
		count = 0 
		data = json.loads(url.read().decode())
		for item in data:
			repos.append(item.get("name"))
			commitsLink = "https://api.github.com/repos/"+username+"/"+item.get("name").strip('"') + "/commits"
			try:
				with urllib.request.urlopen(commitsLink) as commitUrl:
					commitsData = json.loads(commitUrl.read().decode())
					#print(len(commitsData))
					print("Repo: " + item.get("name").strip('"') + " Number of commits: " + str(len(commitsData)))
			except:
				time.sleep(5)


try:
	username = input("Github username: ")
	repoLink = "https://api.github.com/users/" + username + "/repos"
	repos = []
	getGithubInfo()
except:
	time.sleep(5)
	getGithubInfo()


