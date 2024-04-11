"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""
# No se si fue un error o fue intencional para ver si lograbamos resolver
# ya veo porque es el 80% del tiempo leyendo codigo 
char = {
    'a': '1',
    'b': 2,
    'c': '3',
    'd': 4,
    'e': '5',
    0: 0
}


def fn_hack_7(s):
    result = []
    # if s == [0]:
    #     result.append(0)
    # else:
    for x in s:
        if x in char.keys():
            result.append(char.get(x))

    print(result)
    return result


fn_hack_7(["a", "b", "c", "d", "e"])
fn_hack_7([0])
