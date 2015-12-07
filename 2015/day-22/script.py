#!/usr/bin/env python

MAX_MANA_VALUE = 1000000000

def spent_mana(hp, mana, boss_hp, boss_dmg, part_2 = False,
    shield_timer = 0, poison_timer = 0, recharge_timer = 0,
    turn = True, depth = 20):

    if part_2 and turn:
        hp -= 1

    if boss_hp <= 0:
        return 0

    hp = min(hp, 50)

    if depth == 0 or hp <= 0:
        return MAX_MANA_VALUE

    new_shield_timer   = max(0, shield_timer - 1)
    new_poison_timer   = max(0, poison_timer - 1)
    new_recharge_timer = max(0, recharge_timer - 1)

    if not turn:
        if poison_timer > 0:
            boss_hp -= 3

        if recharge_timer > 0:
            mana += 101

        if boss_hp <= 0:
            return 0

        armor = 0 if shield_timer == 0 else 7
        hp -= max( 1, boss_dmg - armor )

        return spent_mana(hp, mana, boss_hp, boss_dmg, part_2,
            new_shield_timer, new_poison_timer, new_recharge_timer,
            not turn, depth - 1)

    # This is the player's turn.
    if poison_timer > 0:
        boss_hp -= 3

    if boss_hp <= 0:
        return 0

    if recharge_timer > 0:
        mana += 101

    mi = MAX_MANA_VALUE

    if mana < 53:
        return MAX_MANA_VALUE

    if mana >= 53:
        new_mi = spent_mana(hp, mana - 53, boss_hp - 4, boss_dmg, part_2,
            new_shield_timer, new_poison_timer, new_recharge_timer,
            not turn, depth - 1)

        mi = min(mi, 53 + new_mi)

    if mana >= 73:
        new_mi = spent_mana(hp + 2, mana - 73, boss_hp - 2, boss_dmg, part_2,
            new_shield_timer, new_poison_timer, new_recharge_timer,
            not turn, depth - 1)

        mi = min(mi, 73 + new_mi)

    if mana >= 113 and new_shield_timer == 0:
        new_mi = spent_mana(hp, mana - 113, boss_hp, boss_dmg, part_2,
            6, new_poison_timer, new_recharge_timer, not turn, depth - 1)

        mi = min(mi, 113 + new_mi)

    if mana >= 173 and new_poison_timer == 0:
        new_mi = spent_mana(hp, mana - 173, boss_hp, boss_dmg, part_2,
            new_shield_timer, 6, new_recharge_timer, not turn, depth - 1)
            
        mi = min(mi, 173 + new_mi)

    if mana >= 229 and new_recharge_timer == 0:
        new_mi = spent_mana(hp, mana - 229, boss_hp, boss_dmg, part_2,
            new_shield_timer, new_poison_timer, 5, not turn, depth - 1)
            
        mi = min(mi, 229 + new_mi)

    return mi

if __name__ == '__main__':
    spent = spent_mana(50, 500, 51, 9)
    print('[Part 1] Minimum spent mana:', spent)
    
    spent = spent_mana(50, 500, 51, 9, part_2 = True)
    print('[Part 2] Minimum spent mana:', spent)
