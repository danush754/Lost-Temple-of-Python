def take_magic_damage(health, resist, amp, spell_power):
    damage_by_magic = amp * spell_power
    new_health = health - (damage_by_magic - resist)
    
    return new_health

print(take_magic_damage(2500, 3, 2, 2))
print(take_magic_damage(1, 1, 1, 1))
print(take_magic_damage(100, 2, 3, 1))
print(take_magic_damage(200, 10, 1, 25))