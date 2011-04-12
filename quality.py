#!/usr/bin/env python
# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab

class Quality:

    def __init__(self, quality):
        self.quality = quality

    def __str__(self):
        return "\"quality\" %s" % self.quality

    def __repr__(self):
        return "\"quality\" %s" % self.quality
