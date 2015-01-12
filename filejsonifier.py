#!/usr/bin/python

import json
import glob
import sys
import os
import fileinput
import re

class FileJsonifier:
  """JSONifies given pdf or csv"""

  def __init__(self, file_path, ofp, index_type, index_count):
    if file_path.lower().endswith('.csv'):
      self.file_type = 'csv'
    else:
      #TODO: Make sure this doesn't always assume it's a pdf
      self.file_type = 'pdf'

    self.file_name = os.path.basename(file_path)
    self.ifp = open(file_path)
    self.ofp = ofp
    self.index_type = index_type
    self.index_count = index_count


  def jsonify(self):
    if self.file_type == "csv":
      self.__jsonify_csv()
    elif self.file_type =="pdf":
      self.__jsonify_pdf()
    else:
      raise "Jsonification is not supported for this filetype."

  def __jsonify_pdf(self):
    for line in self.ifp:
      date = re.search('^[0-9]{2}\/[0-9]{2}\s+', line).group(0).rstrip()
      date = self.file_name[:4] + '-' + date.replace("/", "-")
      subject = re.search('(?![0-9]*\/)(?![0-9])(?!\s+).*\s(?=\$?[0-9,]+\.[0-9]{2})', line)
      subject = subject.group(0)
      subject = subject.rstrip()
      value = re.search('[0-9,]+\.[0-9]{2}', line).group(0).replace(",","")

      json.dump({"index":{"_index": "transactions","_type": self.index_type, "_id": self.index_count}}, self.ofp)
      self.ofp.write('\n')
      json.dump({"date": date, "subject": subject, "value": value}, self.ofp)
      self.ofp.write('\n')

      self.index_count += 1

    print self.file_name, "complete."
    self.ifp.close()

  def __jsonify_csv(self):
    print "good stuff"
