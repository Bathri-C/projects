row1 = ['⬜️', '⬜️', '⬜️']
row2 = ['⬜️', '⬜️', '⬜️']
row3 = ['⬜️', '⬜️', '⬜️']

Map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input('Where do want to put the treasure : '.title())

row = int(position[0])
column = int(position[1])
Map[row - 1][column - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
