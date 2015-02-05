#!/usr/bin/python
import sys, csv, re
print '''
   Simple file parser to impurt menu items into Drupal.\n   Expecting comma-delimited file with two columns.\n   Define a header row with a leading '#'
     Column 1: menu name (with dashes for sub menus)
     Column 2: path
'''
checkColumn = "menu-column" #this will appear in the URL column for a column header
className = "iit-gh-menu-grid-4" # this is the class name IITWeb uses to space out columns
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
            val0=cols[0]
            if val0[:1]=='#':
                print "\nHeader line found. Skipping this line: \n", cols
                continue

            val1=cols[1]  
            if checkColumn in val1:  
                print "Adding class for row ", val0
                row = val0 + " " + "{\"url\":\"" + val1 + "\", \"options\":{\"attributes\":{\"class\":[\"" + className + "\"]}}}\n"
            else:
                row = val0 + " " + "{\"url\":\"" + val1 + "\"}\n"
            row = re.sub('/', '\/', row)
            output.write(row)
            
    output.close()
    print "\nFinished processing data from", inFile, "to", outFile