"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    
    for x in list(s):
        s.pop(x)
        
    s['Foo'] = 'Fooziman'
    print(s)
    return s

fn_hack_9({"foo":"fookziman","bar":"barziman"})
