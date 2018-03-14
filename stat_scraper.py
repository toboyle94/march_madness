# 

import requests
import urllib2
from bs4 import BeautifulSoup

from big_dicts import team_ids, round_1


ROW_VALS = ('gp', _, 'ppg', 'rpg', 'apg', 'spg', 'bpg', 'tpg', 'fg_per', 'ft_per', '3p_per')

class Team(object):
    """
    some team object with some stats
    """

    def __init__(self, id):
        # super(Team, self).__init__()
        self.id = id
        self.stats = self.get_stats()

    def get_stats(self):
        """
        get all relevant season stats on team
        """
        url = 'http://www.espn.com/mens-college-basketball/team/stats/_/id/{}'.format(self.id)
        content = urllib2.urlopen(url).read()
        soup = BeautifulSoup(content)

        row = soup.findAll("tr", {'class':'total'})[0].contents[1:]
        vals = [n.contents[0] for n in row]

        parsed_vals = {}
        for i, val in enumerate(vals):
            if val.startswith(('.', '0.')) and val.split('.')[1].isdecimal():
                parsed_vals[ROW_VALS[i]] = float(val)
            elif val.isdecimal():
                parsed_vals[ROW_VALS[i]] = int(val)

        return parsed_vals
        


url = 'http://www.espn.com/mens-college-basketball/team/stats/_/id/{}'.format(2239)
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)

row = soup.findAll("tr", {'class':'total'})[0].contents[1:]
vals = [n.contents[0] for n in row]

parsed_vals = {}
for i, val in enumerate(vals):
    if val.startswith(('.', '0.')) and val.split('.')[1].isdecimal():
        parsed_vals[ROW_VALS[i]] = float(val)
    elif val.isdecimal():
        parsed_vals[ROW_VALS[i]] = int(val)
