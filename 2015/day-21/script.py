#!/usr/bin/env python

def win_battle(character):
    # a loadout is a tuple ('damage', 'armor')
    boss         = (8, 2)
    character_hp = 100
    boss_hp      = 100

    character_atk = max(character[0] - boss[1], 1)  
    boss_atk      = max(boss[0] - character[1], 1)

    boss_turn = False
    while boss_hp > 0 and character_hp > 0:
        if boss_turn:
            character_hp -= boss_atk
        else:
            boss_hp -= character_atk

        boss_turn = not boss_turn

    return character_hp > 0

def optimal_loadout_cost(weapons, armors, rings):
    min_cost, max_cost = 0, 0

    for loadout in loadouts(weapons, armors, rings):
        cost = loadout[0]

        if win_battle(loadout[1:3]):
            if not min_cost or cost < min_cost:
                min_cost = cost

        else:
            if not max_cost or cost > max_cost:
                max_cost = cost

    return (min_cost, max_cost)

def loadouts(weapons, armors, rings):
    for weapon in weapons:
        yield from with_rings(weapon, rings)

        for armor in armors:
            with_armor = combine(weapon, armor)
            yield from with_rings(with_armor, rings)

def with_rings(loadout_with_no_rings, rings):
    yield loadout_with_no_rings

    for i in range(len(rings)):
        with_one_ring = combine(loadout_with_no_rings, rings[i])
        yield with_one_ring

        for j in range(i + 1, len(rings)):
            yield combine(with_one_ring, rings[j])

def combine(loadout1, loadout2):
    return tuple( x + y for x, y in zip(loadout1, loadout2) )

if __name__ == '__main__':
    # each equipment is a tuple ('cost', 'damage', 'armor')
    weapons = [ ( 8, 4, 0), (10, 5, 0), ( 25, 6, 0), (40, 7, 0), ( 74, 8, 0) ]
    armors  = [ (13, 0, 1), (31, 0, 2), ( 53, 0, 3), (75, 0, 4), (102, 0, 5) ]
    rings   = [ (25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), ( 40, 0, 2), (80, 0, 3) ]

    min_cost, max_cost = optimal_loadout_cost(weapons, armors, rings)
    print('[Part 1] Minimum cost to win is:',  min_cost)
    print('[Part 2] Maximum cost to lose is:', max_cost)
