import urllib
import pprint

#raw_input is the basic way of taking input from user
input = raw_input('Enter website to be crawled: ');
htmlText = urllib.urlopen(input).read();
print htmlText;
