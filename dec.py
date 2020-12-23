def deco(funcn):
    def inner():
        print('coming from inner')
        funcn()
        print('after funcn execution')
    return inner

def funcn_to_be_used():
    print('inside funcn')


funcn_to_be_used=deco(funcn_to_be_used)
funcn_to_be_used()