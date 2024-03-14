def display_fuzzy_set(set_name, fuzzy_set):
    print("Fuzzy Set", set_name + ":")
    for key, value in fuzzy_set.items():
        print(key + ":", value)
    print()

def fuzzy_union(set1, set2):
    union = set1.copy()  # Initialize the union with set1
    for key in set2.keys():
        if key in union:
            union[key] = max(set1[key], set2[key])  # Take the maximum membership value
        else:
            union[key] = set2[key]  # Add elements from set2 not present in set1
    return union

def fuzzy_intersection(set1, set2):
    intersection = {}
    for key in set1.keys():
        if key in set2:
            intersection[key] = min(set1[key], set2[key])
    return intersection

# Example usage
set1 = {'A': 0.6, 'B': 0.8, 'C': 0.4}
set2 = {'B': 0.7, 'C': 0.5, 'D': 0.9}

# Display sets
display_fuzzy_set("1", set1)
display_fuzzy_set("2", set2)

# Union
union_set = fuzzy_union(set1, set2)
print("Union:")
display_fuzzy_set("Union", union_set)

# Intersection
intersection_set = fuzzy_intersection(set1, set2)
print("Intersection:")
display_fuzzy_set("Intersection", intersection_set)
