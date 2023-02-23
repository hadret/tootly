# Tootly

Super simple app that gathers latest post via RSS from
[my blog](https://chabik.com), shortens URL using my
[other super simple app](https://github.com/hadret/shorty) and posts it
altogether to my [Mastodon account](https://fosstodon.org/@hadret). It leverages
SQLite for keeping track of what was published and
[mastodon-py](https://mastodonpy.readthedocs.io/en/stable/) for posting to Mastodon.
