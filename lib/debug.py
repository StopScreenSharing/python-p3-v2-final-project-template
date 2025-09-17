#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.gardener import Gardener
from models.plant import Plant

import ipdb

Gardener.create_table()
Plant.create_table()

ipdb.set_trace()
