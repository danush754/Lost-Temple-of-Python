def calculate_damage(sword, arrow, spear, dagger, fire):
    total_damage = sword+arrow+spear+dagger+fire
    average_damage = (sword+arrow+spear+dagger+fire) / 5
    return total_damage, average_damage

print(calculate_damage(1, 2, 3, 4, 5))
print(calculate_damage(0, 0, 0, 0, 10))
