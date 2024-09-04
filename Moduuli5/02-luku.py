numbers = []  # Alustetaan tyhjä lista numeroille

while True:
    user_input = input("Anna luku (tai paina Enter lopettaaksesi): ")
    if user_input == "":  
        break
    else:
        number = float(user_input)  
        numbers.append(number)  
    

# Lajitellaan lista suurimmasta pienimpään
numbers.sort(reverse=True)

# Tulostetaan viisi suurinta lukua
print("Viisi suurinta lukua suuruusjärjestyksessä:")
for number in numbers[:5]:  # Käydään läpi vain viisi ensimmäistä (suurinta) lukua
    print(number)
