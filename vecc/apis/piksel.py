#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import urllib

from .webapi import WebAPI



class PikselAPI(WebAPI):

    def __init__(self):
        self._results = {}

    def check(self, video_id):
        self._results = {}
        try:
            resp = urllib.urlopen('http://player.piksel.com/' + video_id)
            if 200 == resp.getcode():
                self._results["status"] = True
                return True
            else:
                return False
        except:
            return False

    @property
    def video_data(self):
        if not self._results:
            self._results["status"] = False
        return self._results
