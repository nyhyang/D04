#!/usr/bin/env python
# HW04_ch08_ex04

# The following functions are all intended to check whether a string contains
# any lowercase letters, but at least some of them are wrong. For each
# function, describe (is the docstring) what the function actually does.
# You can assume that the parameter is a string.

# Do not merely paste the output as a counterexample into the documentation
# string, explain what is wrong.

###############################################################################
# Body


def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
    """
    #.islower will only return tru if ALL the character is in lower case but if
    #there is one, it will still return false, which is not the goal
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
    """
    #'c' is not equal to c, it's not refering to check the items in s, it's checkecking if 
    # if there is actual c inside s. It will return since c is in lowercase. 
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
    """ 
    # it only returns the last result of the word 
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    """
    # This returns the result of the boolean statement. 
    # In the all lowercase cases False or True will return True. Correct. 
    # The default False will remain False when the c is uppercases. 
    # When it encounters a lowercase it will become True or False, and return True.
    # Once flag has been reassigned, the characters behind the lowercase character will
    # not change the result. This is the correct function. 

    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag 


def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    """ 
    # This is checking if all the characters are lower cases. 
    # To make c.islower() True to return False, all the c should be lowercases.  
    for c in s:
        if not c.islower():
            return False
    return True




###############################################################################


def main():

    # Remove print("Hello World!") and for each function above that is wrong,
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")

    print(any_lowercase1('Hello'))
    print(any_lowercase2('Hello'))
    print(any_lowercase3('HellllllllllO'))
    print(any_lowercase4('HoEpe'))
    print(any_lowercase5('tesT'))

if __name__ == '__main__':
    main()
