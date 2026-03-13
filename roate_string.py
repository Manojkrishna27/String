def rotate_string(s,goal):
    # first check it has same length
    if len(s)!=len(goal):
        return False

    return goal in (s+s)  # uf it has same length check goal is there in s+s i mean abcdabcd see goal is there
s="abcd"
goal="cdab"
print(rotate_string(s,goal))