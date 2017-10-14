#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# blog 信息
AUTHOR = 'Holbrook'
SITENAME = u'心内求法'
SITESUBTITLE = u'制心一境，住心观性，澄心外照，摄心内证'
SITEURL = 'http://holbrook.github.io'
MENUITEMS = [
  (u'订阅','/feeds/all.atom.xml'),
  (u'关于','/pages/about.html'),
]

# 编译信息
PLUGIN_PATHS = ['../pelican-plugins','./plugins.custom']
PLUGINS = [
    'tag_cloud',
    'pelican-ipynb.markup',
    'pelican-toc',
    'relate_posts',

#    "i18n_subsites",
    "better_codeblock_line_numbering",
#    "plantuml",
#    "youku",
#    "youtube",
    'tipue_search',
    'neighbors',
    'series',
    'bootstrapify',
    'twitter_bootstrap_rst_directives',
    "render_math",
    'extract_toc',
    'tag_cloud',
    'sitemap',
    'summary',
    'render_math'
]


PATH = 'content'
MARKUP = ('md', 'ipynb')
IGNORE_FILES = ['.ipynb_checkpoints']

FILES_TO_COPY = (
    ("extra/robots.txt", "robots.txt"),
)


DEFAULT_LANG = 'zh'
TIMEZONE = 'Asia/Shanghai'
DATE_FORMATS = {
    'en': ('en_US','%a, %d %b %Y'),
    'cn': ('zh_CN','%Y-%m-%d'),
}
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


I18N_UNTRANSLATED_ARTICLES = "remove"

MD_EXTENSIONS = ['admonition',
                 'toc',
                 'codehilite(css_class=highlight,linenums=False)',
                 'extra']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.tables':{},
    }
}

JINJA_ENVIRONMENT = {'trim_blocks': True, 'lstrip_blocks': True}

# relate_posts 插件
RELATED_POSTS_MAX = 10

# pelican-toc 插件
TOC = {
    'TOC_HEADERS' : '^h[1-6]',  # What headers should be included in the generated toc
                                # Expected format is a regular expression
    'TOC_RUN'     : 'true'      # Default value for toc generation, if it does not evaluate
                                # to 'true' no toc will be generated
}


#使用目录名作为文章的分类名
#USE_FOLDER_AS_CATEGORY = True

#使用文件名作为文章或页面的slug（url）
FILENAME_METADATA = '(?P<slug>.*)'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

TAG_URL = ('tag/{slug}.html')     #The URL to use for a tag.
TAG_SAVE_AS = ('tag/{slug}.html')  #The location to save the tag page.

#THEME = 'themes/pelican-blueidea'
THEME = 'themes/my-foundation'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('//TODO:', '#'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
FOUNDATION_FRONT_PAGE_FULL_ARTICLES = False
FOUNDATION_ALTERNATE_FONTS = False
FOUNDATION_TAGS_IN_MOBILE_SIDEBAR = False
FOUNDATION_NEW_ANALYTICS = False
FOUNDATION_ANALYTICS_DOMAIN = ''
FOUNDATION_FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a> and <a href="http://foundation.zurb.com/">Zurb Foundation</a>. Theme by <a href="http://hamaluik.com">Kenton Hamaluik</a>.'
# FOUNDATION_PYGMENT_THEME = 'monokai'

FOUNDATION_PYGMENT_THEME = 'friendly'

