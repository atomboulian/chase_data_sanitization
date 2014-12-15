chase_data_sanitization
=======================

This code converts chase statement pdf documents to text, and then to JSON to import to ElasticSearch, and to visually analyze with Kibana.

## Get Started
Download all your pdfs from Chase, and save them off into a single folder with the following date format: "YYYYMMdd.pdf". Navigate to that folder.

```
$ ls -n
total 1568
-rw-r--r--@  1 501  20  50554 Jul 15 20:13 20130926.pdf
-rw-r--r--@  1 501  20  55001 Jul 15 20:14 20131025.pdf
-rw-r--r--@  1 501  20  48080 Jul 15 20:14 20131127.pdf
-rw-r--r--@  1 501  20  54095 Jul 15 20:16 20131226.pdf
-rw-r--r--@  1 501  20  44491 Jul 15 20:16 20140128.pdf
-rw-r--r--@  1 501  20  56649 Jul 15 20:17 20140227.pdf
-rw-r--r--@  1 501  20  51758 Jul 15 20:17 20140326.pdf
-rw-r--r--@  1 501  20  56703 Jul 15 20:19 20140424.pdf
-rw-r--r--@  1 501  20  54687 Jul 15 20:19 20140527.pdf
-rw-r--r--@  1 501  20  45692 Jul 15 20:20 20140625.pdf
-rw-r--r--@  1 501  20  45043 Jul 28 19:53 20140725.pdf
-rw-r--r--@  1 501  20  57495 Sep  3 20:17 20140826.pdf
-rw-r-----@  1 501  20  52242 Dec 12 17:53 20140925.pdf
-rw-r-----@  1 501  20  47670 Dec 12 17:47 20141027.pdf
-rw-r-----@  1 501  20  44604 Dec 12 17:48 20141128.pdf
```

Run parse_pdf.sh. This takes all of the pdfs and puts them into text versions, without the unnecessary text about your address, page numbers, account number, etc. These text versions reside in "./textified/".

```
$ ls -n textified
total 392
-rw-r--r--  1 501  20    937 Dec 12 20:20 20130926.pdf_deposits
-rw-r--r--  1 501  20  10637 Dec 12 20:20 20130926.pdf_withdrawals
-rw-r--r--  1 501  20    400 Dec 12 20:20 20131025.pdf_deposits
-rw-r--r--  1 501  20  10085 Dec 12 20:20 20131025.pdf_withdrawals
-rw-r--r--  1 501  20    384 Dec 12 20:20 20131127.pdf_deposits
-rw-r--r--  1 501  20      0 Dec 12 20:20 20131127.pdf_withdrawals
-rw-r--r--  1 501  20    253 Dec 12 20:20 20131226.pdf_deposits
-rw-r--r--  1 501  20      0 Dec 12 20:20 20131226.pdf_withdrawals
-rw-r--r--  1 501  20    819 Dec 12 20:20 20140128.pdf_deposits
-rw-r--r--  1 501  20   8970 Dec 12 20:20 20140128.pdf_withdrawals
-rw-r--r--  1 501  20    821 Dec 12 20:20 20140227.pdf_deposits
-rw-r--r--  1 501  20   9712 Dec 12 20:20 20140227.pdf_withdrawals
-rw-r--r--  1 501  20    533 Dec 12 20:20 20140326.pdf_deposits
-rw-r--r--  1 501  20  11673 Dec 12 20:20 20140326.pdf_withdrawals
-rw-r--r--  1 501  20    266 Dec 12 20:20 20140424.pdf_deposits
-rw-r--r--  1 501  20  12987 Dec 12 20:20 20140424.pdf_withdrawals
-rw-r--r--  1 501  20    265 Dec 12 20:20 20140527.pdf_deposits
-rw-r--r--  1 501  20  13066 Dec 12 20:20 20140527.pdf_withdrawals
-rw-r--r--  1 501  20    265 Dec 12 20:20 20140625.pdf_deposits
-rw-r--r--  1 501  20   9970 Dec 12 20:20 20140625.pdf_withdrawals
-rw-r--r--  1 501  20    530 Dec 12 20:20 20140725.pdf_deposits
-rw-r--r--  1 501  20   9102 Dec 12 20:20 20140725.pdf_withdrawals
-rw-r--r--  1 501  20    256 Dec 12 20:20 20140826.pdf_deposits
-rw-r--r--  1 501  20  10029 Dec 12 20:20 20140826.pdf_withdrawals
-rw-r--r--  1 501  20    959 Dec 12 20:20 20140925.pdf_deposits
-rw-r--r--  1 501  20      0 Dec 12 20:20 20140925.pdf_withdrawals
-rw-r--r--  1 501  20    572 Dec 12 20:20 20141027.pdf_deposits
-rw-r--r--  1 501  20      0 Dec 12 20:20 20141027.pdf_withdrawals
-rw-r--r--  1 501  20    399 Dec 12 20:20 20141128.pdf_deposits
-rw-r--r--  1 501  20   8086 Dec 12 20:20 20141128.pdf_withdrawals
```

