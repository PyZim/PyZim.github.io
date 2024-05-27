AUTHOR = 'Ronald'
SITENAME = 'PyCon Zimbabwe'

SITEURL = ""

INDEX_SAVE_AS = "blog_index.html"

THEME = "theme"

PATH = "content"

TIMEZONE = 'Africa/Harare'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
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
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
#
STATIC_PATHS = ["content/pages"]

TEMPLATE_PAGES = {
        "pages/index.html": "index.html",
        "pages/sponsors.html": "sponsors.html"
        }


# Conference related settings
#
CONFERENCE_NAME = "PyCon Zimbabwe 2024"

MENU_ITEMS = [
        ("talks", "Talks"),
        ("sponsors", "Sponsors")
        ]
