
min_number = None
max_number = None
user_input = input("Anna luku (tai tyhjä merkkijono lopettaaksesi): ")
while user_input != "":
    luku = float(user_input)
    if min_number is None or luku < min_number:
            min_number = luku
    if max_number is None or luku > max_number:
            max_number = luku
    user_input = input("Anna luku (tai tyhjä merkkijono lopettaaksesi): ")      
print(f"Pienin luku: {min_number}")
print(f"Suurin luku: {max_number}")



