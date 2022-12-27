def hackerlandRadioTransmitters(x, k):
    x.sort()
    continuous = []
    discontinuous = []

    digit = ['0'] * len(str(x[0]))
    digit[0] = '1'
    digit = ''.join(digit)
    print(x[0] // int(digit))

    for i in range(len(x)):
        if i == x[i]:
            continuous



x = [21,22,23,25,29]
k = 1

hackerlandRadioTransmitters(x, k)