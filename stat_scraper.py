#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import random

import yaml
import requests
import urllib2
from bs4 import BeautifulSoup

round_1 = yaml.load(open('round1.yaml'))
team_ids = yaml.load(open('team_codes.yaml'))

ROW_VALS = ('gp', 'min', 'ppg', 'rpg', 'apg', 'spg', 'bpg', 'tpg', 'fg_per', 'ft_per', '3p_per')


def build_bpi():
    """
    get bpi ranking numbers
    """
    bpi_dct = {}
    url = "http://www.espn.com/mens-college-basketball/bpi/_/view/bpi/page/{}/"
    # for i in range(1, 7):
    i = 1
    while (bpi_dct.keys() != team_ids.keys()) and i < 15: # circuit breaker
        content = urllib2.urlopen(url.format(i)).read()
        i += 1
        soup = BeautifulSoup(content, "html.parser")
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


class Team(object):
    """
    some team object with some stats
    """

    def __init__(self, team_name):
        self.team_name = team_name
        self.id = team_ids[team_name]
        self.stats = self.get_game_stats()
        self.wins = BPI_DICT[team_name][0]
        self.losses = BPI_DICT[team_name][1]
        self.bpi = BPI_DICT[team_name][2:]

    def get_game_stats(self):
        """
        get all relevant season stats on team
        """
        url = 'http://www.espn.com/mens-college-basketball/team/stats/_/id/{}'.format(self.id)
        content = urllib2.urlopen(url).read()
        soup = BeautifulSoup(content, "html.parser")

        row = soup.findAll("tr", {'class':'total'})[0].contents[1:]
        vals = [n.contents[0] for n in row]

        parsed_vals = {}
        for i, val in enumerate(vals):
            if val.startswith(('.', '0.')) and val.split('.')[1].isdecimal():
                parsed_vals[ROW_VALS[i]] = float(val)
            elif val.isdecimal():
                parsed_vals[ROW_VALS[i]] = int(val)

        return parsed_vals


def make_dumb_prediction(team1, team2):
    """
    take two teams and determine a winner
    """
    team1_off = (team1.bpi[0] - team2.bpi[1])
    team1_off = team1_off if team1_off > 1 else 1
    team1_off *= sum([team1.stats['ppg'], team1.stats['apg'] * .25, team1.stats['rpg'] * .5,])
    
    team2_off = (team2.bpi[0] - team1.bpi[1])
    team2_off = team2_off if team2_off > 1 else 1
    team2_off *= sum([team2.stats['ppg'], team2.stats['apg'] * .25, team2.stats['rpg'] * .5,])

    team1_xfact = sum([team1.stats['3p_per'] * 1.3, team1.stats['fg_per'], team1.stats['spg']]) - sum([team1.stats['tpg'], team2.stats['spg']]) * .01
    team2_xfact = sum([team2.stats['3p_per'] * 1.3, team2.stats['fg_per'], team1.stats['spg']]) - sum([team2.stats['tpg'], team1.stats['spg']]) * .01


    team1_ovr = team1_off * team1_xfact
    team2_ovr = team2_off * team2_xfact
    tot = team1_ovr / (team1_ovr + team2_ovr)

    return team1 if random.random() < tot else team2


def main():
    """
    the main stage
    """
    print "Beginning bracket simulation"
    print
    print "building teams..."
    all_teams = [(Team(t1), Team(t2)) for t1, t2 in round_1]
    while len(all_teams) > 1:
        all_teams = [make_dumb_prediction(*n) for n in all_teams]
        print "Winners for round of {}:".format(len(all_teams) * 2)
        print [n.team_name for n in all_teams]
        print
        all_teams = zip(*(iter(all_teams),) * 2)

    overall_winner = make_dumb_prediction(*all_teams[0])
    print "The NCAA 2018 champion is {}".format(overall_winner.team_name)
    print
    print

if __name__ == '__main__':
    main()

