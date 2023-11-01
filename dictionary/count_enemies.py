enemy_names = ["jackal",
            "kobold",
            "jackal",
            "kobold",
            "soldier",
            "kobold",
            "soldier",
            "soldier",
            "jackal",
            "jackal",
            "gremlin",
            "jackal",
            "jackal",]
count_enemies = {}
for names in enemy_names:
    if names in count_enemies:
        count_enemies[names] += 1
    else :
        count_enemies[names] = 1

print(count_enemies)


