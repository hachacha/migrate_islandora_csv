#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#clearfiles.py
from const import Const
from os import remove
# just clears csvs that were just created
c = Const()
remove('../data/manifests/'+c.collection+'/manifests.csv')
remove('../data/migrations/'+c.collection+'/book_nodes.csv')
remove('../data/migrations/'+c.collection+'/page_files.csv')
remove('../data/migrations/'+c.collection+'/page_nodes.csv')