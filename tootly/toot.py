from config import get_settings
from mastodon import Mastodon

mastodon_url = get_settings().mastodon_url
mastodon_token = get_settings().mastodon_token


def create_toot(toot: str) -> None:
    """Create new toot with post title and short link"""
    mastodon = Mastodon(access_token=mastodon_token, api_base_url=mastodon_url)

    response = mastodon.toot(toot)
    print(response["url"])
