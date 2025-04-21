print("Willkommen beim L-Bank Förderrechner!")

# Benutzereingaben
einkommen = float(input("Geben Sie Ihr Jahreseinkommen ein (in €): "))
projekt = input("Welcher Projekttyp? (digitalisierung/energie/startup): ").lower()

if einkommen < 40000 and projekt == "digitalisierung":
    print("Förderung möglich: bis zu 5.000 €")
elif einkommen < 60000:
    print("Förderung möglich: bis zu 2.500 €")
else:
    print("Keine Förderung möglich.")

print("Vielen Dank für die Nutzung des Rechners!")