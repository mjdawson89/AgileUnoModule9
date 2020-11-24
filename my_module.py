"""
Matthew Dawson
11/22/20
my_module
"""

#import json module
import json

#greeting function which returns "Hello Matt" if name is 'Matt'
def greeting(name):
    return(f"Hello {name}")

#the next function creates a letter
def letter_text(**kwargs):
    #if **kwargs has the correct parameters it returns the following
    if "name" and "amount" and "denomination" in kwargs.keys():
        return(f"Hello {kwargs['name']}, this letter is to inform you that you have won {kwargs['amount']} {kwargs['denomination']}.")
    #if not it notifies the user that the wrong parameters were used
    else:
        return("incorrect parameters supplied")

#initiate my_json_data dictionary
my_json_data = {}

#with the input.json file open, input the json data to the my_json_data dict
with open("input.json", "r") as input:
    my_json_data = json.load(input)