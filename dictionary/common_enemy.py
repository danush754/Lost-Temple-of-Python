enemies_dict = {"jackal": 4, "kobold": 3, "soldier": 10, "gremlin": 5}
max_so_far = float("-inf")
max_enemy_name = None
for name in enemies_dict:
    enemy_count = enemies_dict[name]
    if enemy_count > max_so_far:
        max_so_far = enemy_count
        max_enemy_name = name

print(max_enemy_name)


    


