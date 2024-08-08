def table(arr):
    
    print("")
    new_arr = []
    for s, section in enumerate(arr):
        new_arr.append([section[0]])
        new_arr[s].extend([[] for i in range(len(section) - 1)])
        section = section[1:]
        for r in range(len(section[0])):
            max_chars = find_max_char([i[r] for i in section])
            for g, group in enumerate(section):
                new_arr[s][g + 1].append(group[r] + " " * (max_chars-len(group[r])))
    
    for section in new_arr:
        for group in new_arr:
            print(f"[\'{group[0][0]} {len(group) - 1}\']")
            for elem in group[1:]:
                print("  ".join(elem))
            print("\n")
        break


def find_max_char(arr):
    
    chars = [len(i) for i in arr]
    
    return max(chars)