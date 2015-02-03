#!/usr/bin/python
import sys, csv
print '''
   Simple file parser to impurt menu items into Drupal.\n   Expecting comma-delimited file with two columns.\n   Define a header row with a leading '#'
     Column 1: menu name (with dashes for sub menus)
     Column 2: path
'''
inFile = raw_input("\nEnter input filename to continue or <enter> to quit:\n")
if len(inFile) < 1:
    print '\nProgram stopped'
else: 
    outFile = raw_input("\nEnter output filename to continue or <enter> to quit:\n") 
    if len(outFile) < 1:
        print "\nProgram stopped"
    else:
      output = open(outFile,'w')
      with open(inFile) as input:
          line = csv.reader(input, delimiter=",")
          for cols in line:
              val1=cols[0]
              if val1[:1]=='#':
                print "\nHeader line found. Skipping this line: \n", cols
                continue
              else: 
                val2=cols[1]
                row = val1 + " " + "{\"url\":\"" + val2 + "\"}\n"
                output.write(row)
    output.close()
    print "\nFinished processing data from", inFile, "to", outFile