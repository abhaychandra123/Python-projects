
def power(num, powi):
    return pow(num, powi)


num = float(input("Which num you want to be raised?"))
till = float(input("Till which power?"))
powi = 1
while powi <= till:
    print(str(num) + " raised to the power " + str(powi) + " is= " + str(power(num,powi)))
    powi += 1



