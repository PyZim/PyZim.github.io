import os
import sys


sys.path.append(os.curdir)

from volunteers_conf import VOLUNTEERS
from speaker_conf import SPEAKERS
from schedule_conf import DAY1, DAY2, DAY3

AUTHOR = 'Humphrey'

SITENAME = 'PyCon-Zimbabwe'

SITEURL = ""

INDEX_SAVE_AS = "news.html"

THEME = "event-agency-theme"
# THEME = "notmyidea"

PATH = "content"

TIMEZONE = 'Africa/Harare'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("Facebook", "https://www.facebook.com/pyconzim/", "fab fa-facebook-f"),
    ("Twitter", "https://x.com/pycon_zim", "fab fa-twitter"),
    ("LinkedIn", "https://www.linkedin.com/company/pycon-zimbabwe", "fab fa-linkedin-in"),
    ("Mastodon", "https://fosstodon.org/@pyconzim", "fab fa-mastodon"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
#

#
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# STatic files
CSS_FILE = "styles.css"
# CSS_FILE = "lux.css"

# Menu
MENU_ITEMS = [
        # ("about", "About"),
        # ("venue", "Venue"),
        # ("tickets", "Tickets"),
        ("code-of-conduct.html", "Code-of-Conduct"),
        ("diversity.html", "Diversity"),
        # ("talks", "programme"),
        # ("sponsors", "Sponsoring"),
        ("schedule.html", "Schedule "),
        ("news.html", "News"),
        ("team.html", "Team"),
        ("safety-and-health.html", "Health-Policy"),
        ]

# TEMPLATE_PAGES = {
        # "pages/conduct.html": "conduct.html",
        # }

# Conference Details
#
CONFERENCE_NAME = "PyCon Zimbabwe"
CONFERENCE_DATES = "31 October-2 November"
CONFERENCE_YEAR = "2024"
CONFERENCE_VENUE = "Cresta Oasis Hotel"
CONFERENCE_LOGO = ""