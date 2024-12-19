def teken_bord(bord):
    for i in range(3):
        print(' | '.join(bord[i*3:(i+1)*3]))
        if i < 2:
            print('-' * 9)

def check_win(bord, speler):
    for i in range(3):
        if all(bord[i*3+j] == speler for j in range(3)):
            return True
        if all(bord[i+j*3] == speler for j in range(3)):
            return True
    if all(bord[i*4] == speler for i in range(3)):
        return True
    if all(bord[2+i*2] == speler for i in range(3)):
        return True
    return False

bord = [" " for _ in range(9)]
speler = "X"

while True:
    teken_bord(bord)
    rij = int(input(f"Speler {speler}, voer de rij in (1-3): ")) - 1
    kolom = int(input(f"Speler {speler}, voer de kolom in (1-3): ")) - 1
    index = rij * 3 + kolom

    if 0 <= rij <= 2 and 0 <= kolom <= 2 and bord[index] == " ":
        bord[index] = speler
        if check_win(bord, speler):
            print(f"Speler {speler} heeft gewonnen!")
            break
        speler = "O" if speler == "X" else "X"
    else:
        print("Probeer opnieuw.")

    if " " not in bord:
        print("Gelijkspel!")
        break