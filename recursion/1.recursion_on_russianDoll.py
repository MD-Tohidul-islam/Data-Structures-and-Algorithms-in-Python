def opneRussianDoll(doll):
    if doll == 1:
        print('All dolls are opened')
    else:
        opneRussianDoll(doll-1)
print(opneRussianDoll(5))