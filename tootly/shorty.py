import requests
from config import get_settings

shorty_url = get_settings().shorty_url


def get_short_link(link: str):
    """Get short link from the shorty endpoint"""
    shorty = requests.post(shorty_url, json={"target_url": link})

    if shorty:
        short_link = shorty.json()["url"]
        admin_link = shorty.json()["admin_url"]
        return short_link, admin_link
    else:
        print(shorty)
        raise SystemExit("Couldn't reach the URL shortener")
