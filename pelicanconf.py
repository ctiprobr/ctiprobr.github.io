#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# AUTHOR = "A Diretoria"
SITENAME = "CTI"
SITETITLE = "Profissionais da Ciência e Tecnologia da Informação"
SITESUBTITLE = "Espaço organizado de maneira independente com o objetivo de fomentar o debate sobre temas que orbitam a categoria profissional."

PORT = 8080
HTTPS = True
SITEURL = "https://cti.pro.br"
DOMAIN = SITEURL
FEED_DOMAIN = SITEURL
LINKS = ()

TIMEZONE = "America/Sao_Paulo"
DEFAULT_LANG = "pt-BR"
DEFAULT_CATEGORY = ""
USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True

DEFAULT_PAGINATION = 10
SUMMARY_MAX_LENGTH = 100
SUMMARY_MAX_PARAGRAPHS = 1
RELATIVE_URLS = True

THEME = "theme"
PATH = "conteudo"
PAGE_PATHS = ["Paginas"]
STATIC_PATHS = ["static"]
ARTICLE_URL = "{date:%Y}-{date:%m}-{date:%d}_{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}-{date:%m}-{date:%d}_{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
