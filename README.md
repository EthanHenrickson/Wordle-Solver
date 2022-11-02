# Wordle Solver
 A script that opens a wordle type website and solves the wordle.
 
 I say as best as it can because its possible it doesn't solve it in the 6 tries you get. This is because of how similar some words are, you have to just try every signle possible word that match the current criteria. This could be slightly improved by checking the words that are more popular first. From what I've found wordle doesn't pick super obscure words, because my program uses almost every 5 letter word all these super obscure words are still a part of my program. By filtering these out and using the more popular word out of the words left, it could possibly made more effective. The effectiveness could also possibly be improved by first trying words that don't have duplicate letters (EX. Bloom, Hobby, etc.) this also should slightly increase the effectiveness.


NOTE -  

You must have selenium installed for python. This can be installed with PIP    (pip3 install selenium)
This program also uses Firefox for its web interaction. You must have both Firefox and the Firefox web driver installed. https://github.com/mozilla/geckodriver

Also, because this program uses almost every 5 letter word sometimes the words it inputs into the wordle site that the site doesn't think is a word. The program already acounts for this, if it happens it will delete the current word and try another. I put this here so you don't think its not working correctly when you see those red boxes.


Have fun!
