import time

PlayerX = 2
PlayerY = 2
Key = ""
Map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
for a in range(999999999):
    Map[PlayerY][PlayerX] = "P"
    print("----------")
    for i in range(0, 10):
        print(
            str(Map[i][0])
            + str(Map[i][1])
            + str(Map[i][2])
            + str(Map[i][3])
            + str(Map[i][4])
            + str(Map[i][5])
            + str(Map[i][6])
            + str(Map[i][7])
            + str(Map[i][8])
            + str(Map[i][9])
        )
    Key = input("Key: ")
    if Key == "Left":
        Map[PlayerY][PlayerX] = 0
        PlayerX = PlayerX - 1
        if Map[PlayerY][PlayerX] == 1:
            PlayerX = PlayerX + 1
    if Key == "Right":
        Map[PlayerY][PlayerX] = 0
        PlayerX = PlayerX + 1
        if Map[PlayerY][PlayerX] == 1:
            PlayerX = PlayerX - 1
    if Key == "Up":
        Map[PlayerY][PlayerX] = 0
        PlayerY = PlayerY - 1
        if Map[PlayerY][PlayerX] == 1:
            PlayerY = PlayerY + 1
    if Key == "Down":
        Map[PlayerY][PlayerX] = 0
        PlayerY = PlayerY + 1
        if Map[PlayerY][PlayerX] == 1:
            PlayerY = PlayerY - 1
