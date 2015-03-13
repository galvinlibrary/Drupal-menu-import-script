#!/usr/bin/python
import sys, csv, re
print '''
   Simple file parser to impurt menu items into Drupal.\n   Expecting comma-delimited file with two columns.\n   Define a header row with a leading '#'
     Column 1: menu name (with dashes for sub menus)
     Column 2: path
'''

inFile = raw_input("\nEnter input filename to continue or <enter> to quit:\n")
propFlag=0
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
          i=0;
          for cols in line:
            if cols[0][:1]=='#':
                print "\nHeader line found. Skipping this line: \n", cols
                continue
            if cols[0][:1]=='':
                print "\nSkipping blank line: \n"
                continue
                
            # add options only if one or more property flags are found
            propFlag=0
            
            if cols[2]!="":
                propFlag=1
            if cols[3]!="":
                propFlag=1
            if cols[4]!= "":
                propFlag=1                

            row = "%s {\"url\":\"%s\"" % (cols[0], cols[1])
            if propFlag==1:
                row = row + ",\"options\":{\"attributes\":{"
                if cols[2]!="":
                    row = row + "\"title\":\"" + cols[2] + "\","
                if cols[3]!="":
                    row = row + "\"id\":\"" + cols[3] + "\","
                if cols[4]!="":
                    row = row + "\"class\":[\"" + cols[4] + "\"],"
                row = row[:-1]
                row = row + "}}}\n"
            else:
                row = row + "}\n"

            row = re.sub('/', '\/', row)
            output.write(row)
            

            
    output.close()
    print "\nFinished processing data from", inFile, "to", outFile