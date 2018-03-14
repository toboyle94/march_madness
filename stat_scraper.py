#!/usr/bin/env python
# -*- coding: UTF-8 -*-

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
        self.id = id
        self.game_stats = self.get_stats()

    def get_game_stats(self):
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


def build_bpi():
    """
    get bpi ranking numbers
    """
    bpi_dct = {}
    url = "http://www.espn.com/mens-college-basketball/bpi/_/view/bpi/page/{}/"
    # for i in range(1, 7):
    i = 1
    while (bpi_dct.keys() != team_ids.keys()) and i < 20:
        content = urllib2.urlopen(url.format(i)).read()
        i += 1
        soup = BeautifulSoup(content)
        tbl = soup.findAll("table", {'class':'bpi__table'})
        all_rows = soup.find_all('tr')
        for team in all_rows:
            team_name = team.find('abbr')
            # if we find a team abbr, can assume this is a valid row
            if team_name and team_name.contents[0] in team_ids:
                team_name = team_name.contents[0]
                raw_vals = [n.contents[0] for n in team.contents[3:7]]
                win, loss = [int(n) for n in raw_vals[0].split('-')]
                bpi_off = float(raw_vals[1])
                bpi_def = float(raw_vals[2])
                bpi = float(raw_vals[3])

                bpi_dct[team_name] = [win, loss, bpi_off, bpi_def, bpi]

    return bpi_dct

BPI_DICT = build_bpi()


