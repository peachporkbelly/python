"""
정의하고 호출하기
"""
def do_nothing():
    pass

do_nothing()


"""
위치 인수 분해하기/모으기: *args
"""
def print_a_lot(nessesary, *args):
    print(nessesary)
    print("others: ", args) #튜플

print_a_lot("very important", "apple", "banana")

