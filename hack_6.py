"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""

char = {
    'a':'1',
    'b':'-',
    'c':'3',
    'd':'-',
    'e':'5',
    ' ':'0'
}
result = char.keys()
f = char.values()
# print(f)
# print(result)

def fn_hack_6(s):
    result = []
    if s == []:
        result.append(char.get(' '))
    else:
        for x in s:
            if x in char.keys():
                result.append(char.get(x))
    
    print(result)
    return result

fn_hack_6(['a','b','c','d','e'])
fn_hack_6([])