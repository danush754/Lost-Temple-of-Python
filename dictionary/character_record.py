def get_character_record(name, server, level, rank):
    
    player = {"name": name,"server":server,"level":level,"rank":rank,"Id":name + "#"+server}
    return player
    


print(get_character_record("dhan", "server1", 10 , 3))
