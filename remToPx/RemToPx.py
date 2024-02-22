#Python Rem to px converter 

choice = int(input("Rem or pixels [0 or 1]: "))
if choice == 0:
    rem = float(input('REM: '))
    pixels = rem * 16
    print(f"{rem} REM = {pixels} pixels")
else:
    pixels = float(input('Pixels: '))
    rem = pixels / 16
    print(f"{pixels} pixels = {rem} REM")