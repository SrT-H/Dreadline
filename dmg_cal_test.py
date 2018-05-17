while True:
    hp = int(input("HP: "))
    atk = int(input("ATK: "))
    armor = int(input("ARMOR: "))
    #effective HP = base HP × (1 + 0.05 × armor)
    #dmg_reduc = (0.05 * armor) / (1 + 0.05 * armor)
    
    if armor > 5:
        x = 1/5*2
    elif armor > 6.67:
        x = 1/4*2
    elif armor > 10:
        x = 1/3*2
    elif armor > 20:
        x = 1/2*2
    elif armor > 40:
        x = 2/3*2
    elif armor > 60:
        x = 3/4*2
        
    #eff_hp = hp * (1 + 0.05 * armor)
    dmg = atk-(armor*0.05)
    
    #print("EFF_HP:", eff_hp)
    #print("DMG:", dmg_reduc)
    print("DMG:", dmg)
    print('-------------\n')
