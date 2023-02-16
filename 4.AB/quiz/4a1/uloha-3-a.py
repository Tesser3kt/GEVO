rok_narozeni = input("Zadejte rok narození: ")
rok_narozeni = int(rok_narozeni)

if rok_narozeni < 1903 or rok_narozeni > 2017:
    print("Nevěřím.")

if 1953 <= rok_narozeni <= 1954:
    print("Nevěřím.")
