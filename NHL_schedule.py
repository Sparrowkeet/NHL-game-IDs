import requests

#Enter date on next line
date = "now" # e.g., "2024-03-01" or "now"

def game_schedule():
    url = f"https://api-web.nhle.com/v1/schedule/{date}"
    return requests.get(url).json()

def main():
    game_data = game_schedule()
    for level_1 in (game_data["gameWeek"]):
        for game in (level_1["games"]):
            print(level_1["date"])
            print(f"Game ID: {game['id']}")
            print(game["awayTeam"]["placeName"]["default"], end=" at ")
            print(game["homeTeam"]["placeName"]["default"])

if __name__ == "__main__":
    main()
