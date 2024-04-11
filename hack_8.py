"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b"] output => ["2","1"]
"""





def fn_hack_8(s):
    result = []
    num = ['1','2','3','4','5']
    if len(s) >= 5:
        for x, j in zip(s, num):
            result.append(x + '-' + j)

    elif len(s) == 4:
        count = 0
        for x in range(0,len(s)):
            count += 1
            result.append(f'{count}')

    elif len(s) == 3:
        for x, j in zip(s, num):
            result.append(x + '-' +j)

    elif len(s) == 2:
        count = 0
        for x in range(0,len(s)):
            count += 1
            result.append(f'{count}')

    result.reverse()
    print(result)
    return result


fn_hack_8(["a","b","c","d","e"])
fn_hack_8(["a","b","c","d"])
fn_hack_8(["a","b","c"])
fn_hack_8(["a","b"])