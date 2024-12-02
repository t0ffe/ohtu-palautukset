class TennisGame:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]
    ALL_SCORE_NAMES = ["Love-All", "Fifteen-All", "Thirty-All", "Deuce"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self._get_even_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self._get_advantage_or_win_score()
        else:
            return self._get_running_score()

    def _get_even_score(self):
        if self.player1_score < 3:
            return self.ALL_SCORE_NAMES[self.player1_score]
        return "Deuce"

    def _get_advantage_or_win_score(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def _get_running_score(self):
        return f"{self.SCORE_NAMES[self.player1_score]}-{self.SCORE_NAMES[self.player2_score]}"
