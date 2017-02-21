#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://localhost:8000'
RELATIVE_URLS = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""


# GALLERY_OUTPUT_PATH variables were not already defined (as implied in docs)
BASE_PATH = '/'
OUTPUT_PATH = 'output/'
GALLERY_FOLDER = 'images/gallery'

GALLERY_FOLDER = "galleries"
GALLERY_SRC_PATH = "%s%s" % (BASE_PATH, "gallery_src")
GALLERY_OUTPUT_PATH = "%s%s%s" % (BASE_PATH, OUTPUT_PATH, GALLERY_FOLDER)
GALLERY_REGENERATE_EXISTING = False
GALLERY_PRESETS = [
                    {"name": "thumb", "actions": [{"type": "fit", "height": 100, "width": 100, "from": (0.5, 0.5) }]},
                    {"name": "slider", "actions": [{"type": "fit", "height": 300, "width": 900, "from": (0.5, 0.5) }]},
                    {"name": "large", "actions": [{"type": "resize", "height": 640, "width": 850, "from": (0.5, 0.5) }]},
                    {"name": "thumb_greyscale",
                        "actions": [
                            {"type": "fit", "height": 100, "width": 100, "from": (0.5, 0.5) },
                            {"type": "greyscale"}
                        ]},
                  ]

# This setting is optional, used for thumbnails in bootstrap
THUMBNAIL_GALLERY_CLASS = "span2"
