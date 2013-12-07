#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""EditorL"""
from __future__ import print_function
import sys
import os
import shutil


class TargetFile(object):
    def __init__(self, filename):
        self.filename = filename
        self.loadFile()

    def loadFile(self):
        with open(self.filename, "rt") as fp:
            self.lines = fp.readlines()
        self.currentPosition = 0
        self.p1 = 10  # TODO: need a clear name.
        self.showCurrentNode()

    def showNode(self):
        if self.p1 == 0:
            self.showCurrentNode()
        else:
            if self.p1 > 0:
                self.showNextPage()
            else:
                self.showLastPage()

    def showCurrentNode(self):
        print(self.lines[self.currentPosition])

    def showNextPage(self):
        print("showNextPage")
        p = self.currentPosition
        n = 0
        while not n > self.p1:
            self.currentPosition = p
            print(self.lines[self.currentPosition])
            p = p + 1
            n = n + 1

    def showLastPage(self):
        pass

    def save(self):
        dot = os.path.extsep
        dotPos = self.filename.rfind(dot)
        if dotPos == -1:
            backupFilename = dot.join([self.filename, 'bak'])
        else:
            backupFilename = dot.join([self.filename[:dotPos], 'bak'])
        if os.path.exists(backupFilename):
            os.remove(backupFilename)
        shutil.copy(self.filename, backupFilename)
        with open(self.filename, "wt") as fp:
            fp.writelines(self.lines)


def showHelp():
    # TODO: need implement
    pass


def parse(cmdline):
    # TODO: need implement.
    return cmdline[0].upper()


def main(arg):
    showHelp()
    print("\nEditor file: ", end='')
    filename = raw_input()
    if not os.path.exists(filename):
        print("  New file")
        fp = open(filename, "wt")
        fp.close()
    tf = TargetFile(filename)
    while True:
        print(">", end='')
        cmdline = raw_input()
        cmd = parse(cmdline)
        if cmd == 'E':
            break

    tf.save()

if __name__ == "__main__":
    main(sys.argv[1:])
