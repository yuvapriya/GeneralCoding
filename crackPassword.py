# -*- coding: utf-8 -*-
def Test(candidate): # return True if it is the password.

subst = { ‘a’: [‘a’, ‘A’, ‘@’], ‘b’: []...}

def crack(seed_word, subst):
    if len(seed_word) == 0:
        return None
return testSubs(seed_word, 0 , subst)    


def testSubs(subs_word, index, subst):
    if index == len(subs_word):
        if (Test(subsWord)):
            return subsWord
    else:
        for subsChar in subst[subs_word[index]]:
            newSubsWord= subs_word[:index-1] + subsChar + subs_word[index+1:]
            result = testSubs(newSubsWord, index+1 , subst)
            if (result is not None):
                return result 
    return None



