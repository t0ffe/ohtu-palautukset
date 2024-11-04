import unittest

from player import Player
from statistics_service import SortBy, StatisticsService


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Player1", "TeamA", 10, 11),
            Player("Player2", "TeamA", 20, 22),
            Player("Player3", "TeamB", 30, 33),
            Player("Player4", "TeamB", 40, 44),
            Player("Player5", "TeamC", 50, 55),
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_player_found(self):
        player = self.stats.search("Player1")
        assert player is not None
        assert player.name == "Player1"

    def test_search_player_not_found(self):
        player = self.stats.search("NonExistentPlayer")
        assert player is None

    def test_team_players_found(self):
        team_players = self.stats.team("TeamA")
        assert len(team_players) == 2
        assert team_players[0].team == "TeamA"
        assert team_players[1].team == "TeamA"

    def test_team_players_not_found(self):
        team_players = self.stats.team("NonExistentTeam")
        assert len(team_players) == 0

    def test_top_players(self):
        top_players = self.stats.top(2)
        assert len(top_players) == 3
        assert top_players[0].points >= top_players[1].points
        assert top_players[1].points >= top_players[2].points

    def test_top_players_by_goals(self):
        top_players = self.stats.top(2, SortBy.GOALS)
        assert len(top_players) == 3
        assert top_players[0].goals >= top_players[1].goals
        assert top_players[1].goals >= top_players[2].goals

    def test_top_players_by_assists(self):
        top_players = self.stats.top(2, SortBy.ASSISTS)
        assert len(top_players) == 3
        assert top_players[0].assists >= top_players[1].assists
        assert top_players[1].assists >= top_players[2].assists

    def test_top_players_by_points(self):
        top_players = self.stats.top(2, SortBy.POINTS)
        assert len(top_players) == 3
        assert top_players[0].points >= top_players[1].points
        assert top_players[1].points >= top_players[2].points
