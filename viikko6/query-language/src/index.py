from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, All, Or

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    not_test = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )

    fewerthan_test = And(
        HasFewerThan(2, "goals"),
        PlaysIn("NYR")
    )

    or_test = Or(
        HasAtLeast(45, "goals"),
        HasAtLeast(70, "assists")
    )

    or_test_2 = And(
        HasAtLeast(70, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("FLA"),
            PlaysIn("BOS")
        )
    )
    for matcher in [not_test, fewerthan_test, or_test, or_test_2]:
        for player in stats.matches(matcher):
            print(player)
        print("\n")

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))

if __name__ == "__main__":
    main()
