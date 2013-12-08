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

    def checkEmpty(fn):
        def f(self):
            if len(self.lines):
                fn(self)
        return f

    @checkEmpty
    def showCurrentNode(self):
        print(self.lines[self.currentPosition])

    @checkEmpty
    def showNextPage(self):
        print("showNextPage")
        p = self.currentPosition
        n = 0
        while not n > self.p1:
            self.currentPosition = p
            print(self.lines[self.currentPosition])
            p = p + 1
            n = n + 1

    @checkEmpty
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
    print("""
Help Menu
<CommandLine>::=<Prompt><Command>[,<Parameter>]
<Prompt>::=]
<Command>::=A|B|C|D|E|H|I|L|N|O|S|T
           |Abort| Bottom| Change
           |Delete| End| Head
           |Insert| Last| Next
           |OnHelp| Show| Top
<Parameter>::=-32767..32767
    """)


def abortEdit(tf):
    sys.exit(1)


def initializeCommands():
    cmds = {}
    cmds['A'] = abortEdit
    return cmds


def parse(cmdline):
    if cmdline:
        cmd = cmdline[0].upper()
        commaPos = cmdline.find(',')
        try:
            p1 = int(cmdline[commaPos+1])
        except:
            p1 = 0
        return (cmd, p1)
    else:
        return ('E', 0)


def main(arg):
    showHelp()
    print("\nEditor file: ", end='')
    cmds = initializeCommands()
    filename = raw_input()
    if not filename:
        print("filename is empty.")
        sys.exit(-1)
    if not os.path.exists(filename):
        print("  New file")
        fp = open(filename, "wt")
        fp.close()
    tf = TargetFile(filename)
    while True:
        print(">", end='')
        cmdline = raw_input()
        cmd, p1 = parse(cmdline)
        if cmd == 'E':
            break
        else:
            if cmd in cmds:
                tf.p1 = p1
                cmds[cmd](tf)
            else:
                print("Wrong command.")

    tf.save()

if __name__ == "__main__":
    main(sys.argv[1:])
