from player import PlayerReader, PlayerStats
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    console = Console()
    seasons = ["2018-19", "2019-20", "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]

    console.print("\nNHL Statistics by nationality", style="italic")
    
    season = Prompt.ask(f"\nSelect season [cyan][{ '/'.join(seasons)}][/]").strip()

    while season not in seasons:
        season = Prompt.ask(f"\nInvalid season {season}. Please select one of the following: [cyan][{ '/'.join(seasons)}][/]").strip()
    
    while True:
        nationalities = reader.get_nationalities(season)
        nationality = Prompt.ask(f"\nSelect nationality [cyan][{ '/'.join(nationalities)}][/]").strip().upper()
        
        while nationality not in nationalities:
            nationality = Prompt.ask(f"\nInvalid nationality {nationality}. Please select one of the following: [cyan][{ '/'.join(nationalities)}][/]").strip().upper()
            continue

        players = stats.top_scorers_by_nationality(nationality, season)

        table = Table(title=f"Top Scorers from {nationality} in {season}")

        table.add_column("Name", justify="left", style="cyan", no_wrap=True)
        table.add_column("Team", justify="left", style="magenta")
        table.add_column("Goals", justify="right", style="green")
        table.add_column("Assists", justify="right", style="green")
        table.add_column("Total Points", justify="right", style="bold")

        for player in players:
            table.add_row(player.name, player.team, str(player.goals), str(player.assists), str(player.goals + player.assists))


        console.print(table)

if __name__ == "__main__":
    main()
