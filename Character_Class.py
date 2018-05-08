
def cal_percentage(percent, whole):
    if whole is 0:
        return 0
    else:
        return (percent * whole) / 100


#class Human:
    #HP = 0
    #DP = 0
    #AP = 0
    #human_name = ''
    #race = human


#class Elf:
    #HP = 0
    #DP = 0
    #AP = 0
    #elf_name = ''
    #race = elf


#class Demon:
    #HP = 0
    #DP = 0
    #AP = 0
    #demon_name = ''
    #race = demon


class Elentriana:  # red hair girl.
    def ___intit___(self):
        self.max_HP = 65
        self.max_DP = 50
        self.max_AP = 15
        self.name = 'Elentriana'
        self.race = 'Human'
        self.skill_activate = False

    def skill_blade_of_chaos(self):
        """+ATK 30%"""
        self.skill_activate = True
        percent_damage = cal_percentage(30, max_AP)
        self.max_AP += percent_damage

    def skill_demon_blood_thirster(self):
        """If the enemy is Demon, + ATK 60%(stack with above skill), heal herself 5 ponits"""
        percent_damage = cal_percentage(60, max_ap)
        if race == 'Demon':
            self.skill_activate = True
            self.max_AP += percent_damage
            if self.HP < self.max_HP:  # if current HP < max HP heal 5 HP
                self.HP += 5


class Zalana:
    def ___intit___(self):
        self.max_HP = 100
        self.max_DP = 100
        self.max_AP = 7
        self.name = 'Zalana'
        self.race = 'Human'
        self.skill_activate = False

    def skill_heal(self):
        """Heal herself 10 points"""
        skill_cooldown = 4  # 4 turns
        self.skill_activate = True
        self.HP += 10

    def skill_shield_of_protection(self):
        """reduce damage taking 20%"""
        self.skill_activate = True
        percent_reduce = cal_percentage(20, damage_taken)
        max_DP -= percent_reduce
        max_HP -= percent_reduce


class Shaca:
    def ___intit___(self):
        self.max_HP = 75
        self.max_DP = 35
        self.max_AP = 20
        self.name = 'Shaca'
        self.race = 'Elf'
        self.skill_activate = False

    def skill_piercing_shot(self):
        """attack all enemies"""
        skill_cooldown = 3
        self.skill_activate = True
        percent_reduce = cal_percentage(30, self.max_AP)

    def skill_trinity_arrow(self):
        """attack 3 times in 1 hit"""
        skill_cooldown = 2
        self.skill_activate = True
        percent_reduce = cal_percentage(50, self.max_AP)
        self.max_AP *= 3 - percent_reduce


class Kazuki:
    def ___intit___(self):
        self.max_HP = 60
        self.max_DP = 35
        self.max_AP = 25
        self.name = 'Kazuki'
        self.race = 'Human'
        self.skill_activate = False

    def skill_kage_no_sashi(self):
        """attack directly to enemy HP"""
        self.skill_activate = True
        skill_cooldown = 3

    def skill_chishi_kogeki(self):
        """0.01% chance of reduce an enemy HP to 1"""
        self.skill_activate = True
        percent_chance = cal_percentage(0.01, 1)


class Lucifer:
    def ___intit___(self):
        self.max_HP = 60
        self.max_DP = 25
        self.max_AP = 30
        self.name = 'Lucifer'
        self.race = 'Demon'
        self.skill_activate = False

    def skill_curse_suffer(self):
        """reduce an enemy attack 20% 2turns"""
        self.skill_activate = True
        reduce_percent = cal_percentage(20, 1)#enemy AP

    def skill_black_magic(self):
        """deal more 20% damage to enemy that is curse"""
        self.skill_activate = True


class Refaian:
    def ___intit___(self):
        self.max_HP = 100
        self.max_DP = 100
        self.max_AP = 7
        self.name = 'Refaian'
        self.race = 'Human'
        self.skill_activate = False

    def skill_intervention(self):
        """Immortality for 1 turn"""
        self.skill_activate = True
        skill_cooldown = 4

    def skill_oriharukon_armor(self):
        """Replenish DP by 2 every 2 turns"""
        self.skill_activate = True
        skill_cooldown = 2
        self.max_DP += 2
