# Webcrawler made using Beautiful Soup
# Program takes in url and writes the html code to a pre-defined file.

import urllib;
import sys;
from bs4 import BeautifulSoup;

url = raw_input("Please enter target URL: ");
#Error checking:
valid = False;
while (valid == False):
    if (len(url)<3):
        print "Invalid URL entered. Please try again";
        url = raw_input("Please enter target URL: ");
    else:
        valid = True;

doc = urllib.urlopen(url).read();
soup = BeautifulSoup(doc);
#For debugging purposes: print (soup.prettify());

data = str(soup); #Converting to string, so that we can write it to a file
try: 
    dest = open('', 'w'); #Enter path to destination
    dest.write(data);
    print "Data written to file."
except IOError, e:
    #Printing the exception for debugging purposes
    print >> sys.stderr, "Exception: %s" % str(e);
    sys.exit(1);
except:
    print "Unexpected error:", sys.exc_info()[0];
    raise;

