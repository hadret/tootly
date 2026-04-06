import httpx
from config import get_settings

shorty_url = get_settings().shorty_url
shorty_api_key = get_settings().shorty_api_key


def get_short_link(link: str):
    """Get short link from the shorty endpoint"""
    headers = {"X-API-Key": shorty_api_key}
    response = httpx.post(shorty_url, json={"target_url": link}, headers=headers, timeout=10.0)
    response.raise_for_status()

    short_link = response.json()["url"]
    admin_link = response.json()["admin_url"]
    return short_link, admin_link
