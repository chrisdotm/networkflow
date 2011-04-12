#!/usr/bin/env python
# vim: set expandtab:ts=8:sw=4:softtabstop=4:smarttab


class EdgeCapacity:
    def __init__(self, capacity):
        self.capacity = int(capacity)

    def __str__(self):
        return "c %d" % self.capacity

    def __repr__(self):
        return "c %d" % self.capacity
