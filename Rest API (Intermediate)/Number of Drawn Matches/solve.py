import json
import urllib.request
from urllib.request import urlopen
def getNumDraws(year):
        draws = 0
        for i in range(0,10):
            user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
            url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1goals={i}&team2goals={i}&page=1"
            data = json.load(urllib.request.urlopen(urllib.request.Request(url,None,{'User-Agent':user_agent,}) )) 
            total = data['total']
            draws+= total
        return draws