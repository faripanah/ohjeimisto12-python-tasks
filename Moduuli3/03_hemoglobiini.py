sukupuoli = input("Anna sukupuoli (Nainen/Mies).").lower()
hemoglobiini_arvo = int(input("Anna sinun hemoglobiiniarvo(g/l): "))
if sukupuoli == "nainen" and hemoglobiini_arvo > 175:
    print("Sinun hemoglobiiniarvo on korkea.")
elif sukupuoli == "nainen" and hemoglobiini_arvo < 117:
    print("Sinun hemoglobiiniarvo on alhainen.")
elif sukupuoli == "nainen" and 117<= hemoglobiini_arvo <=175:
    print("Sinun hemoglobiiniarvo on normaali.")
elif sukupuoli == "mies" and hemoglobiini_arvo < 134:
    print("Sinun hemoglobiiniarvo on alhainen.")
elif sukupuoli == "mies" and hemoglobiini_arvo > 195:
     print("Sinun hemoglobiiniarvo on korkea.")
elif sukupuoli == "mies" and 134<=hemoglobiini_arvo<=195:
    print("Sinun hemoglobiiniarvo on normaali.")
else:
    print("Anna oiken tiedot!!!")

