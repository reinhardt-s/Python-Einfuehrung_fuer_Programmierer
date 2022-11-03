# Schreibe ein Programm welches die Spieler*in dazu auffordert deren Schatz du vergraben,
# in dem diese die Zeile und Spalte angibt.
# 🐒
# 🟫
row1 = ["🟫", "🟫", "🟫"]
row2 = ["🟫", "🟫", "🟫"]
row3 = ["🟫", "🟫", "🟫"]
treasure_map = [row1, row2, row3]
print(f"1 {row1}\n2 {row2}\n3 {row3}")
print("     1     2     3")
# Dein Code nach dieser Zeile

position = input("Wo soll die Affen-Statue vergraben werden(X,Y)?\n")
position_x = int(position[0]) - 1
position_y = int(position[1]) - 1
treasure_map[position_y][position_x] = "🐒"

# Dein Code über dieser Zeile
print(f"{row1}\n{row2}\n{row3}")
