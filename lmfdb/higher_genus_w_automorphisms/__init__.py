# -*- coding: utf-8 -*-
from lmfdb.base import app
from lmfdb.utils import make_logger
from flask import Blueprint

higher_genus_w_automorphisms_page = Blueprint("higher_genus_w_automorphisms", __name__, template_folder='templates', static_folder="static")
logger = make_logger(higher_genus_w_automorphisms_page)


@higher_genus_w_automorphisms_page.context_processor
def body_class():
    return {'body_class': 'higher_genus_w_automorphisms'}

import main

app.register_blueprint(higher_genus_w_automorphisms_page, url_prefix="/HigherGenus/C/aut")
