'''
distribution.py
Author: Jack Meehan
Credit: https://stackoverflow.com/questions/2932511/letter-count-on-a-string
https://stackoverflow.com/questions/4659524/how-to-sort-by-length-of-string-followed-by-alphabetical-order
Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r


Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
'''

L = input('Please enter a string of text (the bigger the better): ')
alphabet = "abcdefghijklmnopqrstuvwxyz"
print('The distribution of characters in "'+L+'" is: ')
L = L.lower()
counts = []
for i in alphabet:
    thiscount = L.count(i)
    if thiscount>1:
        counts.append((L.count(i))*(i))
    elif thiscount > 0:
        counts.append(i)
l = counts
for d in sorted(l, key=len, reverse=True):
     print(d)

