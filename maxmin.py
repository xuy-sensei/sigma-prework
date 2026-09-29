# array1 = [2, 4, 1, 0, 2, -1]
# array2 = [20, 50, 12, 6, 14, 8]
# array3 = [100, -100]
new_array = []

while True:
    num = input("Give ONLY numbers, 'q' to finish: ")
    if num == "q":
        print("Exiting...")
        break
    new_array.append(int(num))

ordered = sorted(new_array)
max_and_min = [ordered[0], ordered[-1]]

print(max_and_min)
