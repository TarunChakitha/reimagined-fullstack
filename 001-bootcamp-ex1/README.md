# Exercises

The file `solutions.py` has empty functions that you need to fill in
with code for the problems mentioned below. Remove the `pass`
statement and fill in code for the functions below and then run the
tests file using


## Problem 1
Write a function called `biggest` which will take a list of numbers as
input and return the largest number in the list

     l = [5,6,9,3,2]
     print (biggest(l))

will print `9`.

## Problem 2
Write a function called `average` which will take a list of numbers as
input and return the average of the list of numbers.


     l = [5,6,9,3,1]
     print (average(l))
     
will print `4.8`

## Problem 3
Write a function called `longest` which will take a list of strings as
input and return the longest string in the list.

     l = ["python", "perl" "php"]
     print (longest(l))
     
will print `python`.

## Problem 4
Write a function called `first_space` which will take a list of
strings as input and return the first string in the list which has a
space in it.

    l = ["perl", "ruby", "python programming", "C hacking"]
    print(first_space(l))

will print `python programming`. 

*Hint:* You can use `in` to check if a string has a certain
substring. e.g. 
    
        "p" in "python"
        
will return `True` but

        "q" in "python"
        
will return `False`

## Problem 5
Write a function called `freq` which will take a string `s` as input
and then return a dictionary which will contain how many times each
character occurs in the string. 

         s = "she sells sea shells on the sea shore"
         print(freq(s))
         
will print


          {'s': 8, 'h': 4, 'e': 7, ' ': 7, 'l': 4, 'a': 2, 'o': 2, 'n': 1, 't': 1, 'r': 1}


## Problem 6
A sentence will all letters of the alphabet is called a panagram
(e.g. "the quick brown fox jumps over the lazy dog"). Write a function
called `panagram` that will take a string `s` as input and return
`True` if `s` is a panagram and `False` if not. 


         panagram("the quick brown fox jumps over the lazy dog")
         
will return `True`

         panagram("the quick brown fox jumped over the lazy dog")
         
will return `False` (I've changed *jumps* to *jumped* so there's no *s*).

## Problem 7
Write a function called `abbreviate` which will take a string `s` (of
multiple words) as input and return an abbreviation of the string. It
will create an abbreviation by taking the first letter of all the
words which start with a capital letter.

       s = "Indian Institute of Management"
       print (abbreviate(s))
       
will print `IIM`.

*Hint:* You can check whether a string has the first letter capital
using the `.istitle` method

       >>> l = "First"
       >>> l.istitle()
       True
       >>> l = "first"
       >>> l.istitle()
       False

## Problem 8
Write a function called `split` which will take an amount of money `a` and a
list of currency denominations `d` and then return how to split `a`
into units of `d`. It should return a dictionary with keys as
denominations and number of notes as values.

         solutions.split(2246, [1000, 500, 100, 50, 20, 10, 5, 1])


will return 

           {1000: 2, 100: 2, 20: 2, 5: 1, 1: 1}

This means that 2246 consists of 2 1000, 2 100, 2 20, 1 5 and 1 1
notes. 50, 10 etc. are not there since we're not using them



      

        



