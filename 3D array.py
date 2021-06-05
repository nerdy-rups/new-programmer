vacancy=0
rooms = [[[False for r in range(4)] for f in range(2)] for t in range(3)]
rooms[0][0][0] = True
rooms[0][1][3] = True
rooms[1][1][2] = True
rooms[1][0][2] = True
rooms[2][1][1] = True
rooms[2][0][3] = True
for i in rooms:
    print(i,end="\n")
for roomNumber in range(4):
    for floorNumber in range(2):
        for buildingNumber in range(3):
            if not rooms[buildingNumber][floorNumber][roomNumber]:
                vacancy+=1
print("vacancy:",vacancy)