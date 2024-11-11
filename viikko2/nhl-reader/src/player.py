import requests
class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.team = dict['team']
        self.nationality = dict['nationality']
        self.goals = dict['goals']
        self.assists = dict['assists']
    
    def __str__(self):
        return f"{self.name:20} {self.team}  {self.goals} + {self.assists} = {self.goals + self.assists}"

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self, season):
        url = f"{self.url}/{season}/players"
        response = requests.get(url).json()
        players = [Player(player_dict) for player_dict in response]
        return players
    
    def get_nationalities(self, season):
        players = self.get_players(season)
        nationalities = sorted(set([player.nationality for player in players]), key=lambda n: n.lower())
        return nationalities

class PlayerStats:
    def __init__(self, reader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality, season):
        players = self.reader.get_players(season)
        filtered_players = filter(lambda p: p.nationality == nationality, players)
        sorted_players = sorted(filtered_players, key=lambda p: p.goals + p.assists, reverse=True)
        return sorted_players