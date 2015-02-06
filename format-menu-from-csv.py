#!/usr/bin/python
import sys, csv, re
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
            if cols[0][:1]=='#':
                print "\nHeader line found. Skipping this line: \n", cols
                continue
 
            if 'column' in cols[0]:  
              print "Adding class for row ", val0
              row = cols[0] + " " + "{\"url\":\"" + cols[1] + "\", \"options\":{\"attributes\":{\"class\":[\"" + 'iit-gh-menu-grid-4' + "\"]}}}\n"
            else:
              row = cols[0] + " " + "{\"url\":\"" + cols[1] + "\"}\n"

            row = re.sub('/', '\/', row)
            output.write(row)
            
    output.close()
    print "\nFinished processing data from", inFile, "to", outFile