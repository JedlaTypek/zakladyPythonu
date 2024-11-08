jmeno = input("Zadej jmeno:")
vaha = input("Zadej svou váhu v kg:")
vyska = input("Zadej svou vysku v cm:")
bmi = round(int(vaha) / (int(vyska) / 100)**2, 2)   #výpočet BMI
print('{jmeno} měří {vyska}, váží {vaha} a má hodnotu BMI: {bmi}.'.format(jmeno=jmeno, vyska=vyska, vaha=vaha, bmi=bmi))
if bmi < 18.5:
    print(jmeno + " málo papá.")
elif bmi > 18.5 and bmi < 24.9:
    print(jmeno + " papá tak akorát.")
elif bmi > 25 and bmi < 29.9:
    print(jmeno + " papá trochu víc.")
else:
    print(jmeno + " se přímo nacpává.")
