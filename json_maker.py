#!/usr/bin/python

import json
import glob
import sys
import os
import getopt
import fileinput
import re

def clean_jsonified_dir():
  if not os.path.exists('jsonified'):
    os.makedirs('jsonified')
  elif os.path.exists('./jsonified/transactions.json'):
    print "Removing ./jsonified/transactions.json"
    os.remove('./jsonified/transactions.json')

def main(argv):

  inputdir = '' #'./textified/'
  try:
    opts, args = getopt.getopt(argv,"hi:o:",["idir="])
  except getopt.GetoptError:
    print "json_maker -i <directory>"
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print "json_maker -i <directory>"
      sys.exit()
    elif opt in ("-i", "--idir"):
      inputdir = arg

  print 'Input directory is "',inputdir,'"'
  clean_jsonified_dir()
  output_filename = './jsonified/transactions.json'
  fp = open(output_filename, 'w')

  if not os.path.exists(inputdir):
    print 'Directory "',inputdir,'" does not exist. Exiting.'

  print "Processing text entries into JSON format."
  index_count = 0
  for bank_statement in os.listdir(inputdir):
    inputfile = open(inputdir + bank_statement, 'r')
    if bank_statement.endswith('deposits'):
      index_type = "deposits"
    elif bank_statement.endswith('withdrawals'):
      index_type = "withdrawals"


    for line in inputfile:
      date = re.search('^[0-9]{2}\/[0-9]{2}\s+', line).group(0).rstrip()
      date = bank_statement[:4] + '-' + date.replace("/", "-")
      subject = re.search('(?![0-9]*\/)(?![0-9])(?!\s+).*\s(?=\$?[0-9,]+\.[0-9]{2})', line)
      subject = subject.group(0)
      subject = subject.rstrip()
      value = re.search('[0-9,]+\.[0-9]{2}', line).group(0).replace(",","")

      json.dump({"index":{"_index": "transactions","_type": index_type, "_id": index_count}}, fp)
      fp.write('\n')
      json.dump({"date": date, "subject": subject, "value": value}, fp)
      fp.write('\n')

      index_count += 1

    print bank_statement, "complete."
    inputfile.close()

  fp.close()

  if os.path.exists(output_filename):
    print output_filename, "successfully created!"
if __name__ == "__main__":
  main(sys.argv[1:])



