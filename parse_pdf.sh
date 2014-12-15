#!/bin/bash

pdflist=$(ls *.pdf)

for pdfname in $pdflist
do

  echo "converting ${pdfname} pdf to text"
  pdftotext -table -nopgbrk $pdfname textified_pdf

  echo "getting deposits and additions for ${pdfname}"
  LC_ALL=C sed -n '/^DEPOSITS AND ADDITIONS$/,/^Total Deposits and Additions.*$/p' textified_pdf \
    | sed '/^\s*$/d' | egrep "^[0-9]" > ./textified/${pdfname}_deposits

  echo "getting withdrawals for ${pdfname}"
  LC_ALL=C sed -n '/^ATM\s+& DEBIT CARD WITHDRAWALS/,/^Total Electronic Withdrawals.*$/p' textified_pdf \
    | sed '/^\s*$/d' | egrep "^[0-9]" > ./textified/${pdfname}_withdrawals

  echo "cleaning up textified pdf temporary file"
  rm -f ./textified_pdf
done
