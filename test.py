"""
Matthew Dawson
11/23/20
AgileUnoModule8
"""
#acheive score of 7.5 or higher in pylint

#import pdb


# 1
# import my_module and pprint
import pprint
import my_module
from my_module import my_json_data as my_data #see item #5

#add breakpoint to test your data
breakpoint()
#view the data in your variables to ensure they are correct


# 2
# use the greeting method from my_module to print out your name
print(my_module.greeting('Matt'))
#add breakpoint to test your data
breakpoint()
#view the data in your variables to ensure they are correct


# 3
# use the letter_text module to print out a string
print(my_module.letter_text(name="Matt",amount="$100",denomination="USD"))
#add breakpoint to test your data
breakpoint()
#view the data in your variables to ensure they are correct


# 4
# use the my_module.my_json_data and print it out
print(my_module.my_json_data)
#add breakpoint to test your data
breakpoint()
#view the data in your variables to ensure they are correct


# 5
# import the my_json_data as my_data and print out the my_json_data using pprint
pprint.pprint(my_data)
#add breakpoint to test your data
breakpoint()
#view the data in your variables to ensure they are correct
