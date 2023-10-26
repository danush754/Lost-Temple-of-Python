def level_up(level, xp_to_add):
    org_xp = level * 100
    xp_increase = org_xp + xp_to_add
    level_incresed = xp_increase // 100
    return level_incresed