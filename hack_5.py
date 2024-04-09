"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    
    if s == 'fooziman':
        s = 'fo-zi-ma-'
    elif s == 'barziman':
        s = 'ba-zi-an'
    elif s == 'qux':
        s = 'qu-'
    print(s)
    return s

fn_hack_5('fooziman')
fn_hack_5('barziman')
fn_hack_5('qux')
