def sort_by_value(input_map):
    sorted_map = dict(sorted(input_map.items(), key=lambda item: item[1]))
    return sorted_map

n = int(input("Enter the number of entries in the map: "))

input_map = {}

for _ in range(n):
    key = int(input("Enter the key (e.g., 101, 102): "))
    value = input("Enter the value (e.g., John Doe, Jane Smith): ")
    input_map[key] = value

sorted_map = sort_by_value(input_map)

print("Sorted Map:", sorted_map)
