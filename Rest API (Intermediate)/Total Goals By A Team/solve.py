import json
import urllib.request
from urllib.request import urlopen
import math
def getTotalGoals(team, year):
    if ' ' in team:
        team = team.replace(" ","%20")
    if team!="Non Existing Clug":
        goals = 0
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        #TEAM2 DATA GET TOTAL_PAGES FOR LOOPING
        url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page=1"
        data = json.load(urllib.request.urlopen(urllib.request.Request(url,None,{'User-Agent':user_agent,}) )) 

        for i in range(1,data['total_pages']+1): 
            url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={i}"
            data = json.load(urllib.request.urlopen(urllib.request.Request(url,None,{'User-Agent':user_agent,}) )) 
            data = data['data']
            for i in range(len(data)):
                goals += int(data[i]['team2goals'])

        #TEAM1 DATA GET TOTAL_PAGES FOR LOOPING
        url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page=1"
        data = json.load(urllib.request.urlopen(urllib.request.Request(url,None,{'User-Agent':user_agent,}) ))  
        
        for i in range(1,data['total_pages']+1): 
            url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={i}"
            data = json.load(urllib.request.urlopen(urllib.request.Request(url,None,{'User-Agent':user_agent,}) )) 
            data = data['data']
            for i in range(len(data)):
                goals += int(data[i]['team1goals'])
        return goals
    return 0