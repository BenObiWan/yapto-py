#!/usr/bin/env python3

import os

#global vars
global prog, finished
prog='progress'
finished='finished'

#non global vars
path='/mnt/mfs/images/photos/'
stack=[]

#recursively list directories to scan
def listDir(stack, path):
  for entry in os.scandir(path):
    if entry.is_dir() and not (entry.name == prog or entry.name == finished):
      stack.append(entry.path)
      listDir(stack, entry.path)

#scan files in a directory
def scanDir(path):
  #check if in progress directory exists or create it

  #treat each file
  for entry in os.scandir(path):
    if entry.is_file():
      scanFile(entry)

def scanFile(path):
  if not path.name.lower().endswith(('.png', '.jpg', '.jpeg', '.jpe', '.cr2', '.bmp', '.tga')):
    if not path.name.lower().endswith(('.m2ts', '.cont', '.tmb', '.cont', '.mov', '.sh', '.sh~', '.mp4', '.mts', '.m4v', '.pmpd', '.xmp', '.avi', '.thm', '.mod', '.moi', '.wmv', '.mpg')):
      print(path.path)

#main program
listDir(stack, path)

while stack:
  scanDir(stack.pop())

