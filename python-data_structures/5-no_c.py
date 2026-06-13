#!/usr/bin/python3
def no_c(my_string):
     new_string = ""
     for charecter in my_string:
         if charecter != "c" and charecter != "C":
             new_string += charecter 
     return new_string

