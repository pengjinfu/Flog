from jinja2 import Markup
from .md import md
from flask import request
from datetime import datetime
from slugify import slugify
from . import app
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin


@app.template_filter()
def date(s, format='%Y-%m-%d'):
    return s.strftime(format)


@app.context_processor
def get_current_time():
    return {'current_time': datetime.now()}


@app.context_processor
def blog_objects():
    url = request.url
    title = request.url_rule.endpoint if request.url_rule else ''
    rv = {'url': url, 'title': title}
    return {'page': rv, 'urljoin': urljoin}


@app.template_filter('slugify')
def make_slugify(s):
    return slugify(s)


@app.template_filter('render')
def render_markdown(s):
    return Markup(md(s))