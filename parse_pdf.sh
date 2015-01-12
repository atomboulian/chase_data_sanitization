#!/bin/bash

idir=$(pwd)
while getopts "i:o:" opt; do
  case $opt in
    i)
      idir=$OPTARG
      echo "Input directory of pdfs is $idir"
      ;;
    o)
      odir=$OPTARG
      echo "Output directory of textified pdfs is $odir"
      ;;
    \?)
      echo "Invalid operion -$OPTARG" >&2
      exit 1
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
  esac
done

echo "====================="

# Test for the presence of the command xpdf-pdftotext to continue
$(xpdf-pdftotext -h > /dev/null 2>&1)
if [[ $? -ne 99 ]]; then
  echo "install xpdf-pdftotext to continue"
  exit 1
fi

# Make output directory if it doesn't exist
if [[ ! -d $odir ]]; then
  mkdir $odir
fi

pdflist=$(ls $idir*.pdf)

# For each pdf in the input directory
for pdfname in $pdflist
do

  echo "converting ${pdfname} from pdf format to text format"
  xpdf-pdftotext -table -nopgbrk $pdfname textified_pdf > /dev/null 2>&1

  echo "getting deposits and additions for ${pdfname}"
  LC_ALL=C sed -n '/^DEPOSITS AND ADDITIONS$/,/^Total Deposits and Additions.*$/p' textified_pdf \
    | sed '/^\s*$/d' | egrep "^[0-9]" > ./textified/$(basename $pdfname)_deposits

  echo "getting ATM and Debit Card withdrawals for ${pdfname}"
  LC_ALL=C sed -n '/^ATM    & DEBIT CARD WITHDRAWALS/,/Total ATM & Debit Card Withdrawals.*$/p' textified_pdf \
    | sed '/^\s*$/d' | egrep "^[0-9]" > ./textified/$(basename $pdfname)_withdrawals

  echo "getting Online purchases for ${pdfname}"
  LC_ALL=C sed -n '/^ELECTRONIC WITHDRAWALS/,/Total Electronic Withdrawals.*$/p' textified_pdf \
    | sed '/^\s*$/d' | egrep "^[0-9]" > ./textified/$(basename $pdfname)_ewithdrawals

  echo "cleaning up textified pdf temporary file"
  rm -f ./textified_pdf
  echo "====================="
done
