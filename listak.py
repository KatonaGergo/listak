import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

gyumolcsok = []


def vizsgalat(gyumolcs):
    if gyumolcs in gyumolcsok:
        print("A beiírt gyümölcs már szerepel a listában!")
        return
    else:
        gyumolcsok.append(gyumolcs)


def kiiratas():
    print("A gyümölcsök fordított sorrendben:", list(reversed(gyumolcsok)))


programfut = True
while programfut:
    gyumolcs = input(str("Írd be a gyümölcsöket!"))
    if gyumolcs == "Vége":
        print("Kiléptél a programból!")
        programfut = False
    else:
        vizsgalat(gyumolcs)

kiiratas()
    

