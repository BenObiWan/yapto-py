#!/usr/bin/env python3.5

import os

global prog, finished

prog='prog'
finished='finished'

#recursively list directories to scan
def listDir(stack, path):
  for entry in os.scandir(path):
    if entry.is_dir() and not (entry.name == prog or entry.name == finished):
      stack.append(entry.path)
      listDir(stack, entry.path)

#scan files in a directory
def scanDir(path):
  
  #treat each file
  for entry in os.scandir(path):
    if entry.is_file():
      scanFile(entry)

#def scanFile(path):
  #do stuff 

path='/mnt/mfs/images/photos/'
stack=[]

listDir(stack, path)

while stack:
  print(stack.pop())

