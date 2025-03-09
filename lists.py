# 3) lists
groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]
print(groceries)
while True:
    item = input("enter an item to remove (or 'stop' to end): ")
    if item == "stop":
        break
    if item in groceries:
        groceries.remove(item)
    print("updated list:", groceries)

