#!/usr/bin/python

import json
import glob
import sys
import os
import getopt
import fileinput
import re
from filejsonifier import FileJsonifier

def clean_jsonified_dir():
  if not os.path.exists('jsonified'):
    os.makedirs('jsonified')
  elif os.path.exists('./jsonified/transactions.json'):
    print "Removing ./jsonified/transactions.json"
    os.remove('./jsonified/transactions.json')

def jsonify_from_inputdir(inputdir,ofp):
  if not os.path.exists(inputdir):
    print 'Directory "',inputdir,'" does not exist. Exiting.'

  print "Processing text entries into JSON format."
  index_count = 0
  for bank_statement in os.listdir(inputdir):
    if bank_statement.endswith('deposits'):
      index_type = "deposits"
    elif bank_statement.endswith('withdrawals'):
      index_type = "withdrawals"
    elif bank_statement.endswith('e_withdrawals'):
      index_type = "e_withdrawals"

    fj = FileJsonifier(inputdir + bank_statement, ofp, index_type, index_count)
    fj.jsonify()

    index_count = fj.index_count
    ofp = fj.ofp
    del fj

  ofp.close()

def usage():
    print "json_maker -d <directory>"
    print "OR"
    print "json_maker -f <csvinputfile>"

def main(argv):

  inputdir = '' #'./textified/'
  inputfile = '' #'./JMPC.csv'
  try:
    opts, args = getopt.getopt(argv,"hd:o:f:",["idir=","ifile="])
  except getopt.GetoptError as err:
    # print something like "option -a not recognized"
    print str(err)
    usage()
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      usage()
      sys.exit()
    elif opt in ("-d", "--idir"):
      inputdir = arg
    elif opt in ("-f", "--ifile"):
      inputfile = arg
    else:
      assert False, "unhandled option"

  if inputdir:
    print "Input directory is {}".format(inputdir)
  elif inputfile:
    print "Input file is {}".format(inputfile)

  clean_jsonified_dir()
  output_filename = './jsonified/transactions.json'
  ofp = open(output_filename, 'w')

  jsonify_from_inputdir(inputdir,ofp)

  if os.path.exists(output_filename):
    print output_filename, "successfully created."

if __name__ == "__main__":
  main(sys.argv[1:])



