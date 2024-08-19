def jump_game(jump_list):
    farthest = 0

    for i in range(len(jump_list)):
        print(jump_list[i])
        if i > farthest:
            return False
        farthest = max(farthest, i + jump_list[i]) 
    return True

print(jump_game([3, 2, 1, 1, 4]))
# print(jump_game([3, 2, 1, 0, 4]))