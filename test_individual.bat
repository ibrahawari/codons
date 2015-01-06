@echo off
C:\Python27\Python.exe hw2.py insulin.fa 60 > insulin_out
C:\Python27\Python.exe hw2.py hemoglobinB.fa 51 > hemoglobinB_out
C:\Python27\Python.exe hw2.py rhodopsin.fa 96 > rhodopsin_out
C:\Python27\Python.exe hw2.py collagen1.fa 127 > collagen1_out
C:\Python27\Python.exe hw2.py insulin.fa 60 hemoglobinB.fa 51 rhodopsin.fa 96 collagen1.fa 127 > all_out
pause