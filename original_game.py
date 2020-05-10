from random import randint
import time
##t = 0
##last_move = 0
num_rest = 30
p_name= input("what is your name? ")
print("type help for a list of actions")
print(p_name, "enters a dark cave, looking for adventure.")
command_list = ("explore, quit, help, rest, status, flee, attack, trade, talk, work")
normal_atk = randint(1,20)
p_inventory=["health_pot","health_pot","health_pot","health_pot","health_pot_super", "health_pot",
             "boost_pot_super","boost_pot_super", "boost_pot_super", "boost_pot_super", "boost_pot_super",
             "boost_pot_super", "boost_pot_super","health_pot_super","health_pot_super","health_pot_super","health_pot_super",
             "health_pot_super","health_pot_super","health_pot_super","health_pot_super","health_pot_super",
             "health_pot_super","health_pot_super","health_pot_super","health_pot_super","health_pot_super",]
y = 0
heal_num = -1
explore_num = 0
current_monster_num = 22
num_boss = 0
command_over = ("wander, trade, accept, decline, talk")
m_name = ['warrior', 'potato', 'ridley']
token_message=("You have now obtained a token! It grants passive enhancement of your character. To learn about specific types of tokens, type 'token_help'")
x = randint(0,2)
b = randint(0,2)
person_talk = "nobody"
magic_genie = False
world_message = False
Curse_on = False
Curse_time = 5
buff_health = False
b_health_count = 0
buff_strength = False
b_strength_count = 0
buff_regen = False
b_regen_count = 0
buff_luck = False
b_luck_count = 0
buff_mystery = False
b_mystery_count = 0
buff_boost = False
b_boost_count = 0
heal_t = False
strength_t = False
speed_t = False
boost_t = False
rej_t = False
god_t = False
mana_t = False
essence_t = False
stealth_t = False

class enemy:
    def __init__(enemy, name, hp, attack):
        enemy.name = name
        enemy.hp = hp
        enemy.attack = attack

class minion:
    def __init__(minion, name, hp, attack):
        minion.name = name
        minion.hp = hp
        minion.attack = attack

class NPC:
    def __init__(NPC,name, gold):
        NPC.name = name
        NPC.gold = gold





class player:
    def __init__(self, status, name, hp, hp_max, attack, luck, gold, inventory,
                 employ, bowman, a1, a2, a3, a1_use, a2_use, a3_use, boss_fight,
                 bow, bow_use, minion,overworld, underworld, explore_level):
        self.status = status
        self.name = name
        self.hp = hp
        self.hp_max = hp_max
        self.attack = attack
        self.luck = luck
        self.gold = gold
        self.inventory = inventory
        self.employ = employ
        self.bowman = bowman
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a1_use = a1_use
        self.a2_use = a2_use
        self.a3_use = a3_use
        self.boss_fight = boss_fight
        self.bow = bow
        self.bow_use = bow_use
        self.minion = minion
        self.overworld = overworld
        self.underworld = underworld
        self.explore_level = explore_level

        
    def die(self):
        print (self.name, "dies, GAME OVER")

    def help(self):
        global command_list
        global command_over
        if(p1.underworld == True):
            print (command_list)
        elif(p1.underworld == False):
            print(command_over)

    def explore(self):
        global enemy_
        global y
        global explore_num
        global num_boss
        global m_name
        global b
        global world_message
        global e21
        global b_health_count
        global buff_health
        global heal_t
        global strength_t
        global boost_t
##        global t
        if(p1.underworld == True):
            if (p1.status == 'normal'):
                if(buff_health == True):
                    b_health_count = b_health_count + 1
                if(heal_t == True):
                    p1.hp = p1.hp + 2
                
                p1.bow_use = p1.bow_use - 1
                explore_num = explore_num + 1
                if(num_boss >= 3) and (world_message == False):
                    print("You unlock the outside world! You can move here and start "
                          "visiting various areas by pressing the LETTERS 'one' ")
                    world_message = True
                    p1.overworld = True
                    x= randint(0,14)
                elif(p1.attack > 50) and (p1.hp > 50) and (explore_num >30):
                    x= randint(0,14)
                else:
                    x= randint(0,12)
                enemy = randint (0, 19)
    ##            if (t <= 30):
    ##                y = enemy_1[enemy]
    ##            elif (30<t<100):
    ##                y = enemy_2[enemy]
                y = enemy_ [enemy]
                if(x==0) or (x==1):
                    if(p1.gold >= 50):
                        ptaotepo=('A ',m_name[b], 'has appeared! He says he will fight for you for only 50 gold! Accept? y or n ')
                        minion = input(ptaotepo)
                        if(minion == 'y'):
                            p1.gold = p1.gold - 50
                            p1.minion = p1.minion +1
                            
                elif (x==2) or (x==3):
                    print("you enter into another dark cave with a goblin at its center."
                          "It seems to be guarding a pile of gold. Attack or Flee? ")
                    print("His attack is", y.attack,)
                    p1.status = 'combat'
                    if (boost_t == True):
                        p1. hp = p1.hp + 1
                        p1.attack = p1.attack + 1
                        p1.luck = p1.luck + 2

                elif (x==4) or (x==5):
                    print("You continue walking. Suddenly you spot a faint gleam from the distance.")
                    decision = input("Continue walking? y or n. ")
                    if (decision == 'y'):
                        gold = randint (1, 10)
                        if (gold <=8):
                            p1.gold = p1.gold+200
                            print(" You find a cache of gold!")
                        elif (gold > 8):
                            p1.hp = p1.hp - 1
                            p1.status = 'combat'
                            print ("you are attacked suddenly out of the darkness. attack?")
                            p1.hp = p1.hp + 1
                            p1.attack = p1.attack + 1
                            p1.luck = p1.luck + 2
                elif (x==6) or (x==7):
                    print("You see an underground village. trade or flee?")
                    p1.status = 'trade'
                elif (x==8) or (x==9):
                    y=input("You discover an underground mine. There are various "
                          "workers here. do you want to talk? y or n")
                    if (y=='y'):
                        p1.status = 'talk'
                        print("type talk!")
                    elif(y=='n'):
                        print("You leave the mine.")
                elif(x==10) or (x==11):
                    if (p1.hp>1):
                        p1.hp = p1.hp-1
                        print("an arrow strikes you in the back. You turn "
                              "and see a bowman looking at you. You can either try "
                              "to attack him or to flee.")
                        if(boost_t == True):
                            p1.hp = p1.hp + 1
                            p1.attack = p1.attack+1
                            p1.luck = p1.luck + 2
                        p1.bowman = True
                        p1.status = 'combat'

                elif(x==12):
                    if(p1.gold >= 200):
                        print("You are at a Brewery. Trade?")
                        p1.status = 'potion'
                elif (x==13) or (x==14):
                    print("A boss monster has appeared! It has immense power and hp!")
                    q=input ("Do you wish to fight? y or n ")
                    if (q == 'y'):
                        p1.boss_fight = True
                        print("Its attack is", e21.attack, )
                        if (boost_t == True):
                            p1.hp = p1.hp + 1
                            p1.attack = p1.attack + 1
                            p1.luck = p1.luck + 2
                        p1.status = 'combat'
                    elif (q == 'n'):
                        print("You leave the dungeon.")
                        p1.status = 'normal'
            elif (p1.status == 'combat'):
                print("you can't do that right now!")

        elif(p1.underworld == False):
            print("There's nothing to explore! You are in the OverWorld!")
    def quit(self):
        print("")
##        print("dont quit u")
##        if (p1.employ == True):
##            p1.employ = False
##            print("You quit the job")
    def status(self):
        if(p1.underworld == True):
            print(p1.hp, "health.", p1.attack, "attack.", p1.gold, "gold.", p1.luck,"luck.",p1.inventory,
                  "is your inventory")
        elif(p1.underworld == False):
            print(p1.gold, "gold", p1.inventory, "is your inventory")
        
    def rest(self):
        global num_rest
        if(p1.underworld == True):
            if (p1.status == 'normal'):
    ##            if (t != last_move):
                rest=randint(1,5)
                if (num_rest >= 0):

                    print("You used a rest! you only have left ", num_rest)
                    num_rest = num_rest - 1
        ##                last_move = t
                    if (rest==5) and (p1.hp>1) and (p1.hp < p1.hp_max-5):
                        p1.hp=p1.hp-1
                        print("you slept too long, -1 health.")
                    elif (p1.hp < p1.hp_max - 5):
                        p1.hp = p1.hp + 1 
                        print("you rest peacefully and gain 1 hp")
                    else:
                        print("You don't need this!")
                else:
                    print("no more rests!")
    ##        elif(t == last_move):
    ##            print("You already did this last move!")
        elif(p1.underworld == False):
            print("no need to rest! Its the OverWorld!")
                

        else:
            print("You can't do that right now!")
    def flee(self):
        if(p1.underworld == True):
            if (p1.status == 'combat') or (p1.status == 'trade'):
                if(p1.boss_fight == False):
                    x=randint (1,4)
                    if (x<= 3):
                        if(p1.a3 == False):
                            print("You flee successfully")
                            p1.status = 'normal'
                            p1.bowman = False
                        if(p1.a3 == True):
                            print("Passive gold!")
                            p1.status = 'normal'
                            p1.bowman = False
                            p1.gold = p1.gold + 5
                    elif (x==4):
                        print("You take 1 damage as you try to leave. You leave unsuccessfully")
                        p1.hp = p1.hp-1
                elif(p1.boss_fight == True):
                    x = randint(1,50)
                    if(x <3):
                        print("You managed to escape this time...")
                        p1.boss_fight = False
                    elif(x>=3):
                        print("The boss monster catches up to you and inflicts damage!"
                              "-10 hp!")
                        p1.hp = p1.hp - 10
        elif(p1.underworld == False):
            print("You are in the OverWorld! There's nothing to flee from!")

    def magic_genie(self):
        global magic_genie
        print("A magic potato genie appears! You have reached close to your death, and the potato is worried. The genie resores your health!"
              " He won't come again, so make sure you don't die again!")
        magic_genie = True
        p1.hp = p1.hp_max

    def attack_accept(self):
        global y
        global num_bow_use
        global num_boss
        if(p1.underworld == True):
            if (p1.status == 'combat') and (p1.boss_fight == False):
                if(p1.bowman == False):
                    if(p1.bow == False):
                        atk = randint (1, 5)
                        crit = randint(1,10)
                        if (atk >=2):
                            if(crit == 1):
                                y.hp = y.hp-p1.attack*2
                                print ("You strike a CRITICAL hit")
                            elif(crit >=2):
                                y.hp = y.hp - p1.attack
                                print("You strike a hit")
                            if (y.hp <= 0):
                                print("you defeat the enemy")
                                p1.gold = p1.gold + 100
                                print ("You get 100 gold!")
                                p1.status = 'normal'
                            else:
                                enemy_atk = randint (1, 10)
                                if (enemy_atk <= 9):
                                    p1.hp = p1.hp - y.attack
                                    print ("He scores a hit! Minus", y. attack, "hp. ")
                                else:
                                    print ("The enemy misses")
                        else:
                            print("You swing and miss.")
                            p1.hp = p1.hp - e1.attack
                            print ("he hits and scores")
                    elif("bow" in p1.inventory):
                        while (p1.bow == True):
                            bow = randint(1,15)
                            if(bow >= 2):
                                y.hp = y.hp - 2
                                print("You shoot a shot at the enemy.")
                                if (y.hp <= 0):
                                    print("You defeat the enemy! +100 gold")
                                    p1.gold = p1.gold+100
                                    p1.status = 'normal'
                                    p1.bow = False
                            elif(bow < 2):
                                print("The bow is overused, and cannot "
                                      "fire more arrows currently. Wait for it to"
                                      " recover")
                                p1.bow = False
                                p1.bow_use = num_bow_use
                                
                elif(p1.bowman == True):
                    if(p1.bow == False):
                        z= 10
                        x= randint (1,15)
                        chance = randint (1,10)
                        if (chance <= 8):
                            z=z-p1.attack
                            if(z<=0):
                                print("you defeat the bowman")
                                p1.status = 'normal'
                                p1.bowman = False
                            else:
                                print("You hit and strike")
                                print("The bowman hits u")
                                p1.hp = p1.hp - x
                                z= z-p1.attack
                        else:
                            print("You hit and miss")
                            print("bowman hits u")
                            p1.hp = p1.hp - x
                    elif(p1.bow == True):
                        z= 10
                        x= randint(1,15)
                        while (p1.bow == True):
                            bow = randint(1,15)
                            if(bow >= 2):
                                z = z - 2
                                print("You shoot a shot at the bowman.")
                                if (z <= 0):
                                    print("You defeat the bowman! +100 gold")
                                    p1.gold = p1.gold+100
                                    p1.status = 'normal'
                                    p1.bow = False
                                    p1.bowman = False
                            elif(bow < 2):
                                print("The bow is overused, and cannot "
                                      "fire more arrows currently. Wait for it to"
                                      " recover")
                                p1.bow = False
                                p1.bow_use = num_bow_use
                        
            elif (p1.boss_fight == True):
                b_atk = randint(1, 50)
                p_atk = randint(1, 9)
                if(b_atk > 3):
                    p1.hp = p1.hp - e21.attack
                    print("The ", e21.name, "attacks you")
                    if(p_atk > 3):
                        e21.hp = e21.hp - p1.attack
                        print("You hit the boss")
                        if(e21.hp <=0):
                            print("You beat the boss! +500 gold!")
                            p1.status = 'normal'
                            p1.boss_fight = False
                            p1.gold = p1.gold + 500
                            num_boss = num_boss+1
                    elif(p_atk <=3):
                        print("You miss the ", e21.name)
                elif(b_atk <= 3):
                    print("You dodge the ", e21.name, "'s attack")
                    e21.hp =e21.hp - p1.attack
                    print("You strike a hit on the boss.")
            else:
                print("theres no one to attack!")
        elif(p1.underworld == False):
            if(p1.status == 'choice_tavern'):
                p1.gold = p1.gold - 100
                x= randint(0,4)
                drinks = ['water','soda','beer','juice','milk']
                current_drink = drinks[x]
                p1.inventory.append(current_drink)
                print("You collect a cup of", current_drink)
                p1.status = 'normal'

        
            elif(p1.status == 'explore_shop'):
                p1.status = 'normal'
                print("You explore the Shop. There are various goods and foods to buy.")
                buy = input("There are three sections of the Shop! foods, tokens, and tech. Type one of the catagories to see them. Or you can exit by declining.")
                p1.status = 'explore_shop2'
                if(buy == 'foods'):
                    p1.foods()
                elif(buy == 'tokens'):
                    p1.tokens()
                elif(buy == 'tech'):
                    p1.tech()
    def attack(self):
        global y
        global num_bow_use
        global num_boss
        if(p1.underworld == True):
            if (p1.status == 'combat') and (p1.boss_fight == False):
                if(p1.bowman == False):
                    if(p1.bow == False):
                        atk = randint (1, 5)
                        crit = randint(1,10)
                        if (atk >=2):
                            if(crit == 1):
                                y.hp = y.hp-p1.attack*2
                                print ("You strike a CRITICAL hit")
                            elif(crit >=2):
                                y.hp = y.hp - p1.attack
                                print("You strike a hit")
                            if (y.hp <= 0):
                                print("you defeat the enemy")
                                p1.gold = p1.gold + 100
                                print ("You get 100 gold!")
                                p1.status = 'normal'
                            else:
                                enemy_atk = randint (1, 10)
                                if (enemy_atk <= 9):
                                    p1.hp = p1.hp - y.attack
                                    print ("He scores a hit! Minus", y. attack, "hp. ")
                                else:
                                    print ("The enemy misses")
                        else:
                            print("You swing and miss.")
                            p1.hp = p1.hp - e1.attack
                            print ("he hits and scores")
                    elif("bow" in p1.inventory):
                        while (p1.bow == True):
                            bow = randint(1,15)
                            if(bow >= 2):
                                y.hp = y.hp - 2
                                print("You shoot a shot at the enemy.")
                                if (y.hp <= 0):
                                    print("You defeat the enemy! +100 gold")
                                    p1.gold = p1.gold+100
                                    p1.status = 'normal'
                                    p1.bow = False
                            elif(bow < 2):
                                print("The bow is overused, and cannot "
                                      "fire more arrows currently. Wait for it to"
                                      " recover")
                                p1.bow = False
                                p1.bow_use = num_bow_use
                                
                elif(p1.bowman == True):
                    if(p1.bow == False):
                        z= 10
                        x= randint (1,15)
                        chance = randint (1,10)
                        if (chance <= 8):
                            z=z-p1.attack
                            if(z<=0):
                                print("you defeat the bowman")
                                p1.status = 'normal'
                                p1.bowman = False
                            else:
                                print("You hit and strike")
                                print("The bowman hits u")
                                p1.hp = p1.hp - x
                                z= z-p1.attack
                        else:
                            print("You hit and miss")
                            print("bowman hits u")
                            p1.hp = p1.hp - x
                    elif(p1.bow == True):
                        z= 10
                        x= randint(1,15)
                        while (p1.bow == True):
                            bow = randint(1,15)
                            if(bow >= 2):
                                z = z - 2
                                print("You shoot a shot at the bowman.")
                                if (z <= 0):
                                    print("You defeat the bowman! +100 gold")
                                    p1.gold = p1.gold+100
                                    p1.status = 'normal'
                                    p1.bow = False
                                    p1.bowman = False
                            elif(bow < 2):
                                print("The bow is overused, and cannot "
                                      "fire more arrows currently. Wait for it to"
                                      " recover")
                                p1.bow = False
                                p1.bow_use = num_bow_use
                        
            elif (p1.boss_fight == True):
                b_atk = randint(1, 50)
                p_atk = randint(1, 9)
                if(b_atk > 3):
                    p1.hp = p1.hp - e21.attack
                    print("The ", e21.name, "attacks you")
                    if(p_atk > 3):
                        e21.hp = e21.hp - p1.attack
                        print("You hit the boss")
                        if(e21.hp <=0):
                            print("You beat the boss! +500 gold!")
                            p1.status = 'normal'
                            p1.boss_fight = False
                            p1.gold = p1.gold + 500
                            num_boss = num_boss+1
                    elif(p_atk <=3):
                        print("You miss the ", e21.name)
                elif(b_atk <= 3):
                    print("You dodge the ", e21.name, "'s attack")
                    e21.hp =e21.hp - p1.attack
                    print("You strike a hit on the boss.")
            else:
                print("theres no one to attack!")
        elif(p1.underworld == False):
            print("You aren't in the UnderWorld right now! No need to attack!")

    def item_message(self):
        print("You have now obtained an item! To use it, "
                "type bread for bread, sword for sword, bow to activate bow in combat, and armor for armor. To"
                " look at your inventory, just type status.")
    def pot_message(self):
        print("You have gotten a potion! To use, just type the name of the potion. For info about different"
              " types of potions, type pot_help.")
    def pot_help(self):
        print("There are various types of potions: health, strength, hp-regen, luck, boost, and mystery.")
        print("Health potions give instant health toward the player. It doesn't add to the max health the player has. Stats: +[] health")
        print("Strength potions give instant attack - for three combat situations. It can be used in battle. Stats: +[] strength")
        print("Hp-regen potions give health over time. Over 10 combat situations it restores a set amount of health. Stats: +[] health per combat")
        print("Luck potions are potions that give a higher chance of fleeing successfully. This is permanent. Stats: +[%] chance")
        print("Boost potions give an extra boost for the player. There is a random chance of what exact stats you recieve. However you will have a total of 15 points "
              "in health, strength, and/or luck")
        print("Mystery potions have a very low chance of giving extreme upgrades in all areas. It also has a 1% chance of instant death. ")

        print("There are also potion UPGRADES. If you have 5 of the same potion in your inventory, they will automatically combine into a completely "
              "stronger and better potion. With two of the same 'super-potion', it will make a permanent buff on your character depending on the potion's origins.")
        print("In order to use super-potions, just type 'super_' and the potion type")
        
    def trade(self):
        global person_talk
        if(p1.underworld == True):
            if (p1.status == 'trade'):
                if (p1.gold >= 100):
                    print("the village accepts your offer to trade")
                    offer = input ("They offer 4 trades, bread for 200, sword for 400, armor for 100, and a bow for 600"
                                   " press b for bread, s for sword, and a for armor, and"
                                   " bow for a bow for 600 gold! ")
                    if (offer == 'b') and (p1.gold >= 200):
                        p1. gold = p1.gold - 200
                        p1.inventory.append("bread")
    #                    p1.inventory.append("p")
                        p1.status = 'normal'
                        p1.item_message()
                        
                    elif (offer == 's') and (p1.gold >= 400):
                        p1.gold = p1.gold - 400
                        p1.inventory.append("sword")
    #                    p1.inventory.append("p")
                        p1.status = 'normal'
                        p1.item_message()
                        
                    elif (offer == 'a') and (p1.gold >= 100):
                        p1.gold = p1.gold - 100
                        p1.inventory.append("armor")
                        p1.status = 'normal'
                        p1.item_message()
                    elif (offer == 'bow') and (p1.gold >= 600):
                        p1.gold = p1.gold - 600
                        p1.inventory.append("bow")
                        p1.status = 'normal'
                        p1.item_message()
                        p1.bow_use = num_bow_use
                        
                    
                    else:
                        print ("make sure you have enough gold and enter the right keys.")
                else:
                    print("You don't have enough gold! The villagers are angry but let you"
                          " leave peacefully.")
                    p1.status = 'normal'
            elif(p1.status == 'potion'):
                print("There are 3 potions for sale. They update everytime you enter this Brewery.")
                potions = ['health_pot', 'strength_pot', 'mystery_pot', 'hp-regen_pot', 'boost_pot', 'luck_pot']
                prices = [300,400,200,450,300, 350]
                x1=randint(0,4)
                x2=randint(0,4)
                x3=randint(0,4)
##                while (x1==x2) or (x2==x3) or (x3==x1):
##                    if(x1==x2):
##                        if(x1<=3):
##                            x1=x1+1
##                        elif(x1>=1):
##                            x1=x1-1
##                    if(x1==x3):
##                        if(x3<=3):
##                            x3=x3+1
##                        elif(x3>=1):
##                            x3=x3-1
##                    if(x2 == x3):
##                        if(x2<=3):
##                            x2=x2+1
##                        elif(x2>=1):
##                            x2=x2-1
                print("The potions for sale are: ",potions[x1]," ",potions[x2], " and ",potions[x3])
                print("The prices for each one is ", prices[x1], "", prices[x2], "", prices[x3],". To choose one of them, press a for the first, b for second, etc.")
                select_pot = input("a, b, c, or n for decline")
                if(select_pot == 'a') and (p1.gold >= prices[x1]):
                    p1.gold = p1.gold - prices[x1]
                    p1.inventory.append(potions[x1])
                    p1.status = 'normal'
                    print("You recieve the ",potions[x1],", and leave the Brewery")
                    p1.pot_message()
                elif(select_pot == 'b') and (p1.gold >= prices[x2]):
                    p1.gold = p1.gold - prices[x2]
                    p1.inventory.append(potions[x2])
                    p1.status = 'normal'
                    print("You recieve the ",potions[x2],", and leave the Brewery")

                elif(select_pot == 'c') and (p1.gold >= prices[x3]):
                    p1.gold = p1.gold - prices[x3]
                    p1.inventory.append(potions[x3])
                    p1.status = 'normal'
                    print("You recieve the ",potions[x3],", and leave the Brewery")

                elif(select_pot == 'n'):
                    print("you exit the Brewery!")
                    p1.status = 'normal'
            else:
                print ("You can't trade now!")
        elif(p1.underworld == False):
            #add something here - ideas: taverns, other villages, maybe some travelling merchants
            s = randint(1,10)
            if (s == 1) and (p1.gold >= 400):
                t = randint(0,4)
                offer = ["rice", "dumplings", "curry", "mashed potatoes", "cheese"]
                print("The ", person_talk, "offers a trade. 400 gold for "+offer[t]+". accept or decline? ")
                p1.status = 'trade_1'
            elif(s == 2):
                print("The",person_talk,"gives a free gift! You get a Curse!")
                
                
            elif(s==3):
                print("POTATO") 
            print("Test")

    def potion_combo(self):
        if(p1.inventory.count("health-pot") >= 5):
            for i in range(1,5):
                del p1.inventory["health-pot"]
                p1.inventory.append("super-health-pot")
                      
    def talk(self):
        if(p1.underworld == True):
            if (p1.status == 'talk'):
                if(p1.gold >=800):
                    power_opt = input("They offer information on how to battle better for only "
                          "800 gold. Accept? y or n")
                    power = randint(1,3)
                    if (power_opt == 'y'):
                        p1.gold = p1.gold - 800
                        if (power == 1) and (p1.a1 == False):
                            p1.a1 = True
                            print("You have a new power! It is the ability to Heal. You can use it with a cost of 50 gold. This skill"
                                  " gets better over time. Press 1 to use")
                        if (power == 2) and (p1.a2 == False):
                            p1.a2 = True
                            print("You now have the ability to fly! You can use it in combat, and is activated by pressing 2. It "
                                  "makes your damage taken during battle reduce.")
                        if (power == 3) and (p1.a3 == False):
                            p1.a3 = True
                            print("You have the ability to hide! This ability gives passive gold when choosing to flee.")
                        else:
                            p1.possible()       

                if(p1.gold >=200):
                    choice = input("They offer information on how to battle better for only "
                          "200 gold. Accept? y or n")
                    if (choice == 'y'):
                        p1.gold = p1.gold - 200
                        atk = randint (1, 3)
                        if (atk == 1):
                            print("You learn some martial arts! +5 atk")
                            p1.attack = p1.attack +5
                            p1.status = 'normal'
                        elif (atk == 2):
                            print("You learn how to defend yourself! +5 hp max")
                            p1.status = 'normal'
                            p1.hp_max = p1.hp_max + 5
                        elif (atk == 3):
                            print("You gain attack and defense! +3 atk, +3 hp max!")
                            p1.status = 'normal'
                            p1.attack = p1.attack + 3
                            p1.hp_max = p1.hp_max + 3
                    elif(choice == 'n'):
                        p1.status = 'normal'
                    elif (choice == 'y') and (p1.gold < 200):
                        print("You don't have enough gold. Dejected, you leave.")
                        p1.status = 'normal'
                    else:
                        print (p1.name, "doesn't understand.")
                elif (p1.employ == False):
                    print("They offer you a job at the mines, working is hard,"
                          " but it pays 50 gold per coal you clear out... just"
                          " be careful of the monsters!")
                    p1.status = 'option'
                    choice = input("if you want to work, press y, if not press n")
                    if (choice == 'y'):
                        player.work(p1)
                    elif(choice == 'n'):
                        p1.status = 'normal'
                        print("You decide not to work")
                    else:
                        print(p1.name, "doesn't understand")
                        print("type talk to continue")
                        p1.status = 'talk'
                else:
                    print("They say that there is a great monster underground, and"
                          " if you explore enough, you can find it.")
                    p1.status = 'normal'
            else:
                print("You can't talk right now!")
        elif(p1.underworld == False):
            if(p1.status == 't/t over'):
                x = randint(1,10)
                if(x==1):
                #hope to have at least 10 situations that you can talk about or sell or trade goods.
                    print("X+!@$!@$$#")
    def possible(self):
        if (p1.a1 == True) and (p1.a2 == True) and (p1.a3 == True):
            print("You have mastered all abilities!")
            p1.gold = p1.gold+800
        elif (p1.a1 == True) and (p1.a2 == True) and (p1.a3 == False):
            p1.a3 = True
            print("You have the ability to hide! This ability gives passive gold when choosing to flee.")

        elif (p1.a1 == True) and (p1.a2 == False) and (p1.a3 == True):
            p1.a2 = True
            print("You now have the ability to fly! You can use it in combat, and is activated by pressing 2. It "
                  "makes your damage taken during battle reduce.")
        elif (p1.a1 == False) and (p1.a2 == True) and (p1.a3 == True):
            p1.a1 = True
            print("You have a new power! It is the ability to Heal. You can use it with a cost of 50 gold. This skill"
                  " gets better over time. Press 1 to use")
        else:
            p1.possible_all()

    def possible_all(self):
        if (p1.gold >= 200):
            abl = input("They give a discount - two powers for 1000 gold. y or n? ")
            if (abl == 'y'):
                p1.a1 = True
                p1.a2 = True
                p1.a3 = True
                p1.gold = p1.gold - 200
                print("You now have mastered all abilities. Heal - 1, Fly - 2, Hide - passive skill")
            elif(abl == 'n'):
                print("You back out of a great deal")
                p1.status = 'normal'
            else:
                print(p1.name, " doesn't understand. He leaves the mine.")
                p1.status = 'normal'
        else:
            x= randint(1, 3)
            if (x==3):
                p1.possible_3()
            if (x==2):
                p1.possible_2()
            if (x==1):
                p1.possible_1()

    def possible_3(self):
        if(p1.a1 == False):
            p1.a1 = True
            print("You have a new power! It is the ability to Heal. You can use it with a cost of 50 gold. This skill"
                  " gets better over time. Press 1 to use")
            return
        
        elif(p1.a2 == False):
            p1.a2 = True
            print("You now have the ability to fly! You can use it in combat, and is activated by pressing 2. It "
                  "makes your damage taken during battle reduce.")
            return
        elif(p1.a3 == False):
            p1.a3 = True
            print("You have the ability to hide! This ability gives passive gold when choosing to flee.")
            return
    def possible_2(self):
        if(p1.a3 == False):
            p1.a3 = True
            print("You have the ability to hide! This ability gives passive gold when choosing to flee.")
            return
        elif(p1.a1 == False):
            p1.a1 = True
            print("You have a new power! It is the ability to Heal. You can use it with a cost of 50 gold. This skill"
                  " gets better over time. Press 1 to use")
            return
        elif(p1.a2 == False):
            p1.a2 = True
            print("You now have the ability to fly! You can use it in combat, and is activated by pressing 2. It "
                  "makes your damage taken during battle reduce.")
            return
    def possible_1(self):
        if(p1.a2 == False):
            p1.a2 = True
            print("You now have the ability to fly! You can use it in combat, and is activated by pressing 2. It "
                  "makes your damage taken during battle reduce.")
            return
        elif(p1.a3 == False):
            p1.a3 = True
            print("You have the ability to hide! This ability gives passive gold when choosing to flee.")
            return
        elif(p1.a1 == False):
            p1.a1 = True
            print("You have a new power! It is the ability to Heal. You can use it with a cost of 50 gold. This skill"
                  " gets better over time. Press 1 to use")
            return
                
    def bread(self):
        if ("bread" in p1.inventory):
            p1.inventory.remove("bread")
            p1.hp_max = p1.hp_max + 2
            p1.hp = p1.hp + 2
            print ("You ate your bread! It was yummy.")
            
    def sword(self):
        if ("sword" in p1.inventory):
            p1.inventory.remove("sword")
            p1.attack = p1.attack + 12
            print ("You used your sword and got extra attack!")

    def armor(self):
        if ("armor" in p1.inventory):
            p1.inventory.remove("armor")
            p1.hp = p1.hp + 5
            p1.hp = p1.hp - len(p1.inventory)
            print("You put on the armor!")

    def health_pot(self):
        if("health_pot" in p1.inventory):
            p1.inventory.remove("health_pot")
            p1.hp = p1.hp + 10

    def mystery_pot(self):
        if("mystery_pot" in p1.inventory):
            p1.inventory.remove("mystery_pot")
            c = randint(1,100)
            if(c==100):
                p1.hp = 0
            elif(c<=5):
                b = randint(1,3)
                if(b==3):
                    print("You get more luck!")
                    p1.luck = p1.luck + 20
                elif(b==2):
                    print("You get more strength!")
                    p1.attack = p1.attack + 20
                elif(b==1):
                    print("You get higher hp_max!")
                    p1.hp_max = p1.hp_max + 20
            else:
                print("nothing happened.")
        else:
            print("bro u trying to scam me - you dont have the potion dumbo")

    def strength_pot(self):
        if("strength_pot" in p1.inventory):
            p1.inventory.remove("strength_pot") 
            p1.attack = p1.attack + 10
    def luck_pot(self):
        if("luck_pot" in p1.inventory):
            p1.inventory.remove("luck_pot")
            p1.luck = p1.luck + 10
    def hp_regen_pot(self):
        if("hp-regen_pot" in p1.inventory):
            p1.inventory.remove("hp-regen_pot")
            p1.hp = p1.hp+10

    def boost_pot(self):
        if("boost_pot" in p1.inventory):
            p1.inventory.remove("boost_pot")
            lol = randint(1,3)
            c=randint(1,10)
            y=15-c
            x = randint(1,2)
            if(lol == 1):
                p1.attack = p1.attack + c
                print("Plus ", c, " attack.")
                if(x == 1):
                    p1.hp = p1.hp + y
                    print("Plus ",y," hp.")
                elif(x == 2):
                    p1.luck = p1.luck + y
                    print("Plus ",y," luck.")
            elif(lol == 2):
                p1.hp = p1.hp + c
                print("Plus ", c, " hp.")
                if(x == 1):
                    p1.attack = p1.attack + y
                    print("Plus ",y," attack.")
                elif(x == 2):
                    p1.luck = p1.luck + y
                    print("Plus ",y," luck.")
            elif(lol == 3):
                p1.luck = p1.luck + c
                print("Plus ", c, " luck.")
                if(x == 1):
                    p1.hp = p1.hp + y
                    print("Plus ",y," hp.")
                elif(x == 2):
                    p1.attack = p1.attack + y
                    print("Plus ",y," attack.")

    def super_pot(self):
        if("health_pot_super" in p1.inventory):
            x=input("Would you like to use the super health potion?")
            if(x == 'y'):
                p1.inventory.remove("health_pot_super")
                p1.hp_max = p1.hp_max + 30
                p1.hp = p1.hp + 50
                print("HP max increased by 30! HP increased by 50!")
        if("strength_pot_super" in p1.inventory):
            x=input("Would you like to use the super strength potion?")
            if(x=='y'):
                p1.inventory.remove("strength_pot_super")
                p1.attack = p1.attack + 70
        if("super_luck_pot_super" in p1.inventory):
            x=input("Would you like to use the super luck potion?")
            if(x=='y'):
                p1.inventory.remove("luck_potion_super")
                p1.luck = p1.luck + 60
        if("hp-regen_pot_super" in p1.inventory):
            x=input("Would you like to use the super hp-regen potion?")
            if(x=='y'):
                p1.inventory.remove("hp-regen_pot_super")
                p1.hp = p1.hp + 20
        if("boost_pot_super" in p1.inventory):
            x=input("Would you like to use the super boost pot?")
            if(x=='y'):
                p1.inventory.remove("boost_pot_super")
                a = randint(1,88)
                b = randint(1,90-a)
                c = 90 - (a+b)
                p1.hp = p1.hp + a
                p1.attack = p1.attack + b
                p1.luck = p1.luck + c
                print("hp +",a,". attack +",b,". luck +",c,".")
        if("mystery_pot_super" in p1.inventory):
            x=input("Would you like to use the super mystery pot?")
            if(x=='y'):
                p1.inventory.remove("mystery_pot_super")
                m = randint(1,10)
                if(m <= 7):
                    x = p1.hp/2
                    y = p1.attack/2
                    z = p1.luck/2
                    p1.hp = p1.hp + int(round(x))
                    p1.attack = p1.attack + int(round(y))
                    p1.luck = p1.luck + int(round(z))
                    print("hp, attack, and luck increased by",int(round(x)),int(round(y)),int(round(z)))
                else:
                    print("It didn't work...")
                                
    def work(self):
        if (p1.status == 'option'):
            print("You decide to work. Now you are employed and can work"
                  " with pressing w")
            p1.status = 'normal'
            p1.employ = True

    def working(self):
        global person_talk
        global y
        global enemy_
        global current_monster_num
        if(p1.underworld == True):
            if(p1.status == 'normal'):
                if(p1.employ == True):
                    monster = randint (1, 20)
                    if(monster<=9):
                        print("You work without delay, and gain your 50 gold")
                        p1.gold = p1.gold+50
                    elif(monster>9):
                        enemy = randint (0,19)
                        print("A monster appears!")
                        y = enemy_ [enemy]
                        p1.status = 'combat'
                elif(p1.employ == False):
                    print("You're unemployed! Poor you.")
            else:
                print("You can't work right now...")
        elif(p1.underworld == False):
            if(p1.explore_level == 1):
                print("You unlock the Village! Type 'Tavern', 'Shop', 'Farm'")
                p1.explore_level = p1.explore_level + 1
            elif(p1.explore_level == 10):
                print("You unlock the Forest! You can go there and wander around. Maybe you can find some stuff")
                p1.explore_level = p1.explore_level + 1
            else:
                p = [s5,s6,s7]
                x= randint(0,2)
                potato = p[x]
                print("You meet a ", potato.name, ".")
                p1.status = 't/t over'
                person_talk = potato.name

    def heal(self):
        global heal_num
        if(p1.a1 == True) and (p1.gold >= 50) and (p1.status != 'combat'):
            heal_num = heal_num+1
            if(heal_num <= 10):
                p1.hp = p1.hp + 2
                p1.gold = p1.gold - 50
                print ("You healed 2 hp!")
            elif(10<heal_num<=20):
                p1.hp = p1.hp + 5
                p1.gold = p1.gold - 50
                print("You healed 5 hp!")
            elif(20<heal_num<=49):
                p1.hp = p1.hp + 8
                p1.gold = p1.gold - 50
                print("You healed 8 hp!")
            elif(heal_num>=50):
                p1.hp = p1.hp + 20
                p1.gold = p1.gold - 50
                print("Using your Super-Ability Heal, you restored 20 hp.")
        elif(p1.a1 == True) and (p1.gold<50) and (p1.status != 'combat'):      
            print("You need 50 gold!")
        elif(p1.a1 == False):
            print("You don't have this skill!")
        elif(p1.status == 'combat'):
            print("You are in a fighting situation!")
            
    def fly(self):
        global y
        if(p1.a2 == True) and (p1.status == 'oombat'):
            y.attack = y.attack/2
            print("Your enemy's attack decreased by a lot!")
            p1.a2_use = True
        elif(p1.a2 == False):
            print("You don't have this ability!")
        elif(p1.status != 'combat'):
            print("You aren't fighting right now!")
            
    def bow(self):
        if (p1.status == 'combat') and (p1.bow_use <= 0) and ("bow" in p1.inventory):
            p1.bow = True
            print("Bow activated!")
        else:
            p1.bow = False
            print("Are you in combat? or is your bow still recovering?")

    def overworld(self):
        if (p1.overworld == True):
            print("You enter the overworld. The door back underground clangs shut"
                  " behind you. You can return to the underworld through pressing"
                  " the LETTERS 'zero'")
            print("Press help to get a list of actions in the Overworld.")
            p1.underworld = False

    def underworld(self):
        print("You return underground - and leave the overworld.")
        p1.underworld = True
        p1.status = 'normal'
        
    def wander(self):
        global person_talk
        if(p1.underworld == False):
            if(p1.explore_level == 1):
                print("You unlock the Village! Type 'Tavern', 'Shop', 'Farm'")
                p1.explore_level = p1.explore_level + 1
            elif(p1.explore_level == 10):
                print("You unlock the Forest! You can go there and wander around. Maybe you can find some stuff")
                p1.explore_level = p1.explore_level + 1
            else:
                p = [s5,s6,s7]
                x= randint(0,2)
                potato = p[x]
                print("You meet a ", potato.name, ".")
                p1.status = 't/t over'
                person_talk = potato.name
    def tavern(self):
        if(p1.explore_level >= 2):
            print("You arrive at the Tavern. The ", s2.name, " greets you.")
            if(p1.gold >= 100):
                print("He offers you a drink for 100 gold! Accept? accept or decline")
                p1.status = 'choice_tavern'

    def farm(self):
        if(p1.explore_level >= 2):
            print("You come to the Farm. The ",s4.name," looks up")
            p1.status = 'talk_over'

    def shop(self):
        if(p1.explore_level >=2):
            print("You enter the Shop. The ",s1.name," says hello.")
            print("Would you like to explore the Shop? accept or decline")
            p1.status = 'explore_shop'

    def tech(self):
        if(p1.status == 'explore_shop2'):
            print("There are various items for sale")
            x1 = randint(0,5)
            x2 = randint(0,5)
            if x1 == x2:
                if(x1 <=4):
                    x1 = x1+1
                elif(x1>=1):
                    x1 = x1-1
            
            tech = ['fire-blade', 'Excalibur', 'Ray-Gun', 'SMG', 'freeze-gun', 'grenade launcher']
            tech2 = [500, 300 , 400, 450, 700, 600]
            techy = tech[x1]
            techy2 = tech[x2]
            print("There are some weapons. ", techy, " ", techy2, ".")
            print("The price for the first tech is ",tech2[x1], "and the second, ",tech2[x2])
            techbuy = input("if you want to buy the first tech, type a, if second, type b. ")
            if(techbuy == 'a') and (p1.gold >= tech2[x1]):
                p1.gold = p1.gold - tech2[x1]
                print("You recieve the ", techy,"!")
                p1.inventory.append(techy)
                p1.status = 'normal'
            elif(techbuy == 'b') and (p1.gold >= tech2[x2]):
                print("You recieve the ",techy2,"!")
                p1.gold = p1.gold - tech2[x2]
                p1.inventory.append(techy2)
                p1.status = 'normal'
    
    
    def foods(self):
        if(p1.status == 'explore_shop2'):
            print("You see different foods on sale.")
            x1 = randint(0,4)
            x2 = randint(0,4)
            d = randint(0,5)
            e = randint(0,5)
            if x1 == x2:
                if(x1 <= 3):
                    x1 = x1+1
                elif x1>=1:
                    x1 = x1-1
            food = ['apple', 'bread', 'potato', 'orange', 'kiwi']
            description = ['enchanted', 'magical', 'potent', 'shining', 'grand', 'invisible']
            price = [200, 100, 600, 350, 400]
            print("There are two foods here, a",description[d],food[x1], "and", description[e],food[x2])
            print("The first price is",price[x1],"and the second is",price[x2])
            foodbuy = input("for the first food, press a and for the second, press b")
            if(foodbuy == 'a') and (p1.gold >= price[x1]):
                  p1.gold = p1.gold - price[x1]
                  p1.inventory.append(food[x1])
                  p1.status = 'normal'
            elif(foodbuy == 'b') and (p1.gold >= price[x2]):
                  p1.gold = p1.gold - price[x2]
                  p1.inventory.append(food[x2])
                  p1.status = 'normal'
    def apple(self):
        if("apple" in p1.inventory):
            p1.hp = p1.hp + 5
            p1.hp_max = p1.hp_max + 5
    def potato(self):
        if("potato" in p1.inventory):
            p1.hp = p1.hp + 500
            p1.hp_max = p1.hp_max + 500
            p1.attack = p1.attack + 1000
            p1.gold = p1.gold + 100
    def orange(self):
        p1.hp = p1.hp + 5
        p1.hp = p1.hp + 10
        p1.attack = p1.attack + 5
        p1.luck = p1.luck + 5
    def kiwi(self):
        p1.attack = p1.attack + 10
        p1.hp = p1.hp + 3
        p1.hp_max = p1.hp_max + 6
    def tokens(self):
        global token_message
        global heal_t
        global strength_t
        global speed_t
        global boost_t
        global rej_t
        global god_t
        global mana_t
        global essence_t
        global stealth_t
        if(p1.status == 'explore_shop2'):
            print("You see different tokens on sale.")
            x1 = randint(0,9)
            x2 = randint(0,9)
            if x1 == x2:
                if x1 <=8:
                    x1 = x1+1
                elif x1 >=1:
                    x1 = x1 -1
            token_type = ['healing', 'strength', 'speed', 'boosting', 'rejuvination', 'potato', 'god-like powers', 'mana', 'essence', 'stealth']
            token_price = [500,550,400,450,600,800,10000,300,250, 440]
            print("There are two tokens here, a token of", token_type[x1],"and a token of",token_type[x2])
            print("The price for the first is", token_price[x1],"and the second,",token_price[x2])
            tokenbuy = input("Press 'a' for the first, and 'b' for the second.")
            
            if(tokenbuy == 'a') and (p1.gold >= token_price[x1]):
                p1.gold = p1.gold - token_price[x1]
                p1.inventory.append("token_"+token_type[x1])
                p1.status = 'normal'
                print(token_message)
                
            elif(tokenbuy == 'b') and (p1.gold >= token_price[x2]):
                p1.gold = p1.gold - token_price[x2]
                p1.inventory.append("token_"+token_type[x2])
                p1.status = 'normal'
                print(token_message)

    def token_help(self):
        print("Tokens are passive skills that boost your character's stats.")
        print("The Healing Token gives additional health per each time you move.")
        print("The Strength Token gives passive attack over time")
        print("The Speed Token gives a extremely high chance of successful fleeing.")
        print("The Boost Token gives a small boost in all stats when meeting an enemy. These stats can accumulate.")
        print("The Rejuvination Token gives larger amounts of hp whenever you are under 20 under the hp_max")
        print("The Potato Token grants complete restoration in all stats (+100 in luck), however it is not passive. In order to use it, type, 'potato_token'")
        print("The GodPowers Token grants god-like powers.")
        print("The Mana Token creates a new stats - mana. This stat can be used to heal and can be gained by transferring gold.")
        print("The Essence Token creates life-steal after every monster you kill.")
        print("The Stealth Token can occasionally grant invinsibility when attacking monsters. All stats lost will be added back after the fight."
              "However, it has that effect based on a chance. If you die during the battle, it will not restore your hp.")
        print("All passive tokens start effects as soon as you buy the token.")
        


    def accept(self):
        if(p1.status == 'choice_tavern'):
            p1.gold = p1.gold - 100
            x= randint(0,4)
            drinks = ['water','soda','beer','juice','milk']
            current_drink = drinks[x]
            p1.inventory.append(current_drink)
            print("You collect a cup of", current_drink)
            p1.status = 'normal'

    
        elif(p1.status == 'explore_shop'):
            p1.status = 'normal'
            print("You explore the Shop. There are various goods and foods to buy.")
            buy = input("There are three sections of the Shop! foods, tokens, and tech. Type one of the catagories to see them. Or you can exit by declining.")
            p1.status = 'explore_shop2'
            if(buy == 'foods'):
                p1.foods()
            elif(buy == 'tokens'):
                p1.tokens()
            elif(buy == 'tech'):
                p1.tech()

                
    def decline(self):
        if(p1.status == 'choice_tavern'):
            p1.status = 'normal'
            print("You decline the drink")
        elif(p1.status == 'explore_shop'):
            print("You decline the offer to explore. You leave the Shop.")
            p1.status = 'normal'
        elif(p1.status == 'explore_shop2'):
            print("You exit the Shop.")
            p1.status = 'normal'
        
            
def potion_expand(x):
    if(p1.inventory.count(x) >= 5):
        for i in range(1,5):
            p1.inventory.remove(x)
        p1.inventory.append(x+"_super")
        p1.inventory.remove(x)
def potion_apply(x):
    global boost_t
    global heal_t
    global strength_t
    if (p1.inventory.count(x) >= 2):
        p1.inventory.remove(x)
        p1.inventory.remove(x)
        if (str(x) == "health_pot_super") and (buff_health == False):
            buff_health = True
        elif(str(x) == "strength_pot_super") and (buff_strength == False):
            buff_strength = True
        elif(str(x) == "mystery_pot_super") and (buff_mystery == False):
            buff_mystery = True
        elif(str(x) == "boost_pot_super") and (buff_boost == False):
            buff_boost = True
        elif(str(x) == "hp-regen_super") and (buff_regen == False):
            buff_regen = True
        elif(str(x) == "luck_pot_super") and (buff_luck == False):
            buff_luck = True
        elif(str(x) == "strength_pot_super") and (buff_strength == False):
            buff_strength = True
    print("LOL")

def token_expand(x):
    global boost_t
    global heal_t
    global strength_t
    global speed_t
    global boost_t
    global rej_t
    global potato_t
    global god_t
    global mana_t
    global essence_t
    global stealth_t
    if ("token_healing" in p1.inventory):
        heal_t = True
    if("token_speed" in p1.inventory):
        speed_t = True
    if("token_rejuvination" in p1.inventory):
        rej_t = True
    if("token_strength" in p1.inventory):
        strength_t = True
    if("token_potato" in p1.inventory):
        potato_t = True
    if("token_god-like powers" in p1.inventory):
        god_t = True
    if("token_mana" in p1.inventory):
        mana_t = True
    if("token_essence" in p1.inventory):
        essence_t = True
    if("token_boost" in p1.inventory):
        boost_t = True
    if("token_stealth" in p1.inventory):
        stealth_t = True
    print("LOL")
def guiege(lol):
    y = randint (1,2)
    if(y == 1):
        print("-10 hp! -500 gold! -10 hp_max! -everything in your inventory!")
        p1.inventory = []
        p1.hp = p1.hp - 10
        p1.hp_max = p1.hp_max - 10
        p1.gold = p1.gold - 500
    elif(y == 2):
        print("Hi, I'm Christian! I like searching up hentai on peoples computers!")
Commands = {
    'a': player.attack_accept,
  'quit': player.quit,
  'help': player.help,
  'status': player.status,
  'rest': player.rest,
  'explore': player.explore,
  'flee': player.flee,
  'attack': player.attack,
  'trade': player.trade,
  'talk' : player.talk,
  'bread' : player.bread,
  'sword' : player.sword,
  'armor' : player.armor,
  'pot_help':player.pot_help,
  'health': player.health_pot,
  'mystery': player.mystery_pot,
  'strength': player.strength_pot,
  'hp-regen': player.hp_regen_pot,
  'hp_regen': player.hp_regen_pot,
  'super' : player.super_pot,
  'boost': player.boost_pot,
  'luck': player.luck_pot,
  'apple': player.apple,
  'potato': player.potato,
  'w' : player.working,
  '1' : player.heal,
  '2' : player.fly,
  'bow': player.bow,
  'one': player.overworld,
  'zero':player.underworld,
  'wander': player.wander,
  'Tavern':player.tavern,
  'Shop':player.shop,
  'Farm': player.farm,
  'token_help': player.token_help,
  'accept':player.accept,
  'decline': player.decline,
  'guiege': guiege,
  }

p1 = player('normal', p_name, 15, 30, 18, 10, 500, p_inventory, False, False,
            False, False, False, False, False, False, False, False, 0, 0,
            True, True, 1)
print(p1.name, p1.status, p1.hp, p1.hp_max, p1.attack, p1.gold, p1.luck)
s1 = NPC('Shopkeeper',50)
s2 = NPC('Tavern Owner', 100)
s3 = NPC('Wandering Trader', 300)
s4 = NPC('Farmer',0)

s5 = NPC('Villager', 10)
s6 = NPC('Soldier', 30)
s7 = NPC('Foreigner', 400)

m1 = minion(m_name[b], 10, 5)

e1 = enemy('goblin', randint (1,10), randint (5, 15))
e2 = enemy('goblin', randint (1,10), randint (5, 15))
e3 = enemy('goblin', randint (1,10), randint (5, 15))
e4 = enemy('goblin', randint (1,10), randint (5, 15))
e5 = enemy('goblin', randint (1,10), randint (5, 15))
e6 = enemy('goblin', randint (1,10), randint (5, 15))
e7 = enemy('goblin', randint (1,10), randint (5, 15))
e8 = enemy('goblin', randint (1,10), randint (5, 15))
e9 = enemy('goblin', randint (1,10), randint (5, 15))
e10 = enemy('goblin', randint (1,10), randint (5, 15))
##enemy1 = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10]
e11= enemy('goblin', randint (5, 20), randint (10, 25))
e12= enemy('goblin', randint (5, 20), randint (10, 25))
e13= enemy('goblin', randint (5, 20), randint (10, 25))
e14= enemy('goblin', randint (5, 20), randint (10, 25))
e15= enemy('goblin', randint (5, 20), randint (10, 25))
e16= enemy('goblin', randint (5, 20), randint (10, 25))
e17= enemy('goblin', randint (5, 20), randint (10, 25))
e18= enemy('goblin', randint (5, 20), randint (10, 25))
e19= enemy('goblin', randint (5, 20), randint (10, 25))
e20= enemy('goblin', randint (5, 20), randint (10, 25))
##enemy2 = [e11, e12, e13, e14, e15, e16, e17, e18, e19, e20]
enemy_ = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20]

e21 = enemy('dragon' , randint(20, 50), randint (40,50))
e22 = enemy('Trundle the Troll King', randint(70,100), randint(70,90))
                      
if (p1.attack<=9):
    print("your attack is weak - under 10! be careful when fighting!")

while (1==1):
    p1.potion_combo()
    if (p1.hp <= 0):
        p1.die()
    if (p1.hp>0):
        potion_expand("health_pot")

        potion_expand("mystery_pot")

        potion_expand("boost_pot")

        potion_expand("strength_pot")

        potion_expand("health-regen_pot")

        potion_expand("luck_pot")

        if(p1.inventory.count("health_pot_super") >= 2) and buff_health == False:
            p1.inventory.remove("health_pot_super")
            p1.inventory.remove("health_pot_super")
            print("New buff! Every ten 'explores', gain one health potion.")
            buff_health = True
        if(p1.inventory.count("strength_pot_super") >= 2) and (buff_strength == False):
            p1.inventory.remove("strength_pot_super")
            p1.inventory.remove("strength_pot_super")
            print("New buff! Whenevery you attack a monster, your attack goes up 5")
            buff_strength = True


        if(b_health_count >= 10):
            p1.inventory.append("health_pot")
            b_health_count = 0
           
            
        if(p1.hp<=5) and (magic_genie == False):
            p1.magic_genie()
        line = input("> ")
        args = line.split()
        if len(args) > 0:
            commandFound = False
            for c in Commands.keys():
                if args[0] == c[:len(args[0])]:
                    Commands[c](p1)
                    commandFound = True
##                    t = t + 1
                    break
        if (not commandFound):
            print ( p1.name ,"doesn't understand the suggestion.")
        if (p1.hp > p1.hp_max):
            p1.hp = p1.hp_max
            print ("You have reached the max hp!")
        if(p1.bow_use < 0) and ("bow" in p1.inventory):
            p1.bow_use = 0
    num_bow_use = 5



