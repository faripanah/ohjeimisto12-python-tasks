def litroksi(gallona):
    litra = gallona * 3.785
    return litra



gallonmaara = float(input("Syötä gallonmäärä: "))
while gallonmaara > 0 :
    x = litroksi(gallonmaara)
    print(f"{gallonmaara} gallonaa bensiini on {x:.2f} litraa.")
    gallonmaara = float(input("Syötä gallonmäärä: "))
print("Negativiinen määrää!!!")






