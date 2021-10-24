import random

ugani = {"Slovenije": "Ljubljana", "Italije": "Rim", "BIH": "Sarajevo", "Brazilije": "Brasilia", "Zelenortskih otokov": "Praia", "Kanade": "Ottawa",
         "Kitajske": "Peking", "Češke": "Praga", "Kolumbije": "Bogota", "Severne Koreje": "Pjongjang", "Južne Koreje": "Seul", "Hrvaške": "Zagreb",
         "Kube": "Havana", "Egipt": "Kairo", "Združenih arabskih emiratov": "Abu Dabi", "Finske": "Helsinki", "Francije": "Pariz", "Estonija": "Talin",
         "Nemčija": "Berlin", "Japonske": "Tokio"}

print("Dobrodošli v kvizu geografije. Preizkušali bomo koliko glavnih mest poznate.")
ime = input("Vpiši svoje ime:")
count = 0
for x in range(5):
    country, capital = random.choice(list(ugani.items()))
    mesto = input(f"Napiši glavno mesto {country}:")
    if mesto == capital:
        print(f"Odlično {ime}, odgovor je pravilen :)")
        count +=1
    else:
        print(f"Odgovor je žal napačen. Pravilen odgovor je {capital}.")

print(f"Pravilno si odgovoril na {count} vprašanj.")