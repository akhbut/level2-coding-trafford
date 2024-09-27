from random import randint

class Player:
    def __init__(self, health, damage, shield):
        self.health = health
        self.damage = damage
        self.shield = shield

mc = Player(30, 5, 0)

class Enemy:
    def __init__(self, health, damage,name):
        self.health = health
        self.damage = damage
        self.name = name

def player_turn(mc_modifier):
    global enemy_modifier
    print("1 : Attack")
    print("2 : Block")
    print("3 : Dodge")
    choice = input("")
    if choice == '1':
        total_damage = mc.damage*mc_modifier
        enemy.health -= total_damage
        print(f"You dealt {total_damage} damage")

    elif choice == "2":
        mc.shield += 5
        print("You ready your defences")
        print("Gain 5 armor")

    elif choice == "3":
        dodge_chance = randint(1,5)
        if dodge_chance > 2:
            if dark:
                print("You try to move away but fail")
            else:
                print("You prepare and evade the attack")
                enemy_modifier = 0
        else:
            if dark:
                print("You prepare and evade the attack")
                enemy_modifier = 0
            else:
                print("You try to move away but fail")


def combat():
    global enemy_modifier
    mc_modifier = 1
    stunned = False
    count = 0
    while True:
        global enemy_modifier
        enemy_modifier = 1
        count += 1
        mc.shield = 0

        # i think clear terminal only works on certain OS, so \n as substitute
        input("")
        print("\n\n\n\n\n")
        print(f"Turn {count}")
        print(f"{name}'s Health: {mc.health}")
        print(f"{enemy.name}'s Health: {enemy.health}")


        if stunned:
            print("The enemy is still recovering")
        else:
            enemy_move = randint(1,10)
            if enemy_move <= 2:
                print(f"The {enemy.name} is eyeing you up")
            elif enemy_move > 5:
                print(f"The {enemy.name} is ready to attack")
            elif enemy_move >2:
                print(f"The {enemy.name} is preparing a heavy attack")


        player_turn(mc_modifier)
        if enemy.health < 1:
            return True


        if stunned:
            stunned = False 
            continue

        if dark:
            enemy_modifier *= 1.5

        if enemy_move > 5:
            print(f"The {enemy.name} attacks you for {enemy.damage*enemy_modifier} damage")
            mc.shield -= enemy.damage * enemy_modifier
            if mc.shield < 0:
                mc.health += mc.shield

        elif enemy_move > 2:
            print(f"The {enemy.name} attacks you for {enemy.damage*2*enemy_modifier} damage")
            mc.shield -= enemy.damage*2*enemy_modifier
            if mc.shield < 0:
                mc.health += mc.shield
            stunned = True


        if mc.health < 1:
            return False


def boss_combat():
    count = 0
    enraged = False
    charged = False
    mc_modifier = 1
    while True:
        global enemy_modifier
        enemy_modifier = 1
        count += 1
        mc.shield = 0

        input("")
        print("\n\n\n\n\n")
        print(f"Turn {count}")
        print(f"{name}'s Health: {mc.health}")
        print(f"{enemy.name}'s Health: {enemy.health}")

        if enraged:
            print(f"A blind fury overwhelms {enemy.name}")

        elif not charged:
            print(f"{enemy.name} begins speaking in an unknown language as a vile aura floods the room")

        else:
            print("The air grows stale as her voice loudens")

        player_turn(mc_modifier)
        mc_modifier = 1
        if enemy.health < 1:
            return True



        if dark:
            enemy_modifier *= 1.5

        if enraged:
            print(f"{enemy.name} strikes you with her staff for {enemy.damage*enemy_modifier} damage")
            mc.shield -= enemy.damage * enemy_modifier
            if mc.shield < 0:
                mc.health += mc.shield
            enraged = False

        if charged:
            enemy_move = randint(1,4)
            if enemy_move == 1:
                print(f"{enemy.name}'s eyes are filled with a blind rage")
                enraged = True

            elif enemy_move == 2:
                print("Your will wavers as a warm haze envelops your mind")
                mc_modifier *= 0.5

            elif enemy_move == 3:
                print(f"Every movement {enemy.name} makes feels more powerful than before")
                enemy.damage += 2

            else:
                print(f"A chilling surge courses through your body for {(enemy.damage * enemy_modifier) / 2} damage")
                mc.shield -= (enemy.damage * enemy_modifier) / 2
                if mc.shield < 0:
                    mc.health += mc.shield
                    enemy.health -= mc.shield

            charged = False

        else:
            charged = True


        if mc.health < 1:
            return False

# you do not need to understand this 

#You can copy the following text if you want to start any fight
#except the boss which uses boss_combat() instead of combat()


# enemy = Enemy(amount of health they have, base damage they do,  enemy name)
# if combat():
#   print("The dog falls to the ground with a yelp")
# else:
#   print("The dog latches at your throat. ")
#  text


items = ['ring']
dark = False

input("Welcome to Knight's End")
# Introduction and initial dialogue
print("You, a former knight, awaken in a dimly lit room, the air thick with the scent of herbs and burning candles. The wooden beams overhead creak softly as you sit up on the rough-hewn bed. Shadows dance on the stone walls, cast by the flickering light of a single lantern. The room is cluttered with strange trinkets, jars of mysterious substances, and ancient tomes. A sense of eerie calm fills the space, and as your eyes adjust, you notice a kind-faced stranger watching over you, concern etched into their features.")
input()
print("???: Hello traveler, you're safe here.  I found you unconcious out in the forest, so brought you back to my home to rest.  I was worried you wouldn't pull through.  What's your name?")
print("Please type your name and press Enter")
name = input()
print(f"???: Hello, {name}, my name is Ealdred.")
input()
print("Ealdred is an elderly apothecary with a gentle demeanor and a seemingly wealthy knowledge of herbs and potions. He has a scruffy, greying beard and kind, blue eyes that twinkle with wisdom. Despite his frail appearance, Ealdred moves with surprising agility, and his hands are steady and sure. He wears simple robes, adorned with various pouches and trinkets.")
input()
print("Ealdred: Welcome to the the town of Clayvault.  It was once a thriving town filled with traders, but the evil witch, Morgath, placed a curse over Clayvault and its people.  It's now a shell of its former self.")
input()
print("Ealdred: What were you doing out in the forest alone?")
input()
print(f"{name}: I was with my brother, Bertram.  We are both former knights looking for a new place to settle.  But I don't know what happened?  One minute we were walking through woodland, and the next moment I wake up here.  Was Bertram not where you found me?")
input()
print("Ealdred: There was no trace of anyone else there, but you were discovered very close to Morgath's cave.  It's possible he's still out there?")
input()
print("Ealdred: Once you are rested, you should head out and look for him - the forest is just beyond the town's cemetery. Here, take this bag of supplies.  Your sword is resting next to the front door.")
input()

# Loop for choosing zone 2
while True:
    print("Would you like to go outside? (1) yes, (2) no")
    option_1 = input()

    if option_1 == "1":
        print("You have entered Clayvault Town Square")
        break
    else:
        print("Okay, you can rest a little while longer.")
        # Loop back to option 1

# Scene setting
print("The town square, once the bustling heart of the village, now feels like a ghost town. The cobblestone streets are cracked and overgrown with weeds, and the once-lively shops and taverns stand abandoned and decrepit. The grand fountain in the centre, once a symbol of the town's prosperity, now lies dry and covered in grime. A heavy silence hangs in the air, broken only by the distant creak of a swaying sign or the occasional gust of wind. As you step into the square, an uneasy feeling settles over you, and you can't shake the sense that unseen eyes are watching your every move.")
input()
print("You turn and you see a woman staring from the corner of a cobbled street, leading down to an orphanage.  She is a weary and cautious figure, with lines of worry etched deeply into her face. Her once-bright green eyes are now dulled by years of hardship and mistrust. She has short, curly brown hair, now streaked with grey, and she dresses in worn, practical clothing that has seen better days. Though she reluctantly helps the protagonist, her distrust is evident, and she constantly glances over her shoulder as if expecting trouble.")
input()
print("???: You ought to watch where you go in this town.  It's no place for a stranger.  My name is Matilda, and I take care of the kids down in that orphanage down there.  This town is filled with a lot of sadness and tragedy.")
input()
print("Matilda: You're heading through the cemetery?  Be careful - I've heard of a wild dog lurking around there - it's eaten a couple of my orphans who explored a little too far. Rumour is that its former owner died and is buried there, so it has settled by their grave.  If you can rid the town of that dog, you'd be bringing Clayvault a little bit of relief.  Regarding the forest, you'd be wise to grab some supplies before you go - Maurin's Butcher has some meat and bread for sale - just be sure to give it a sniff first!")
input()

# Loop for zone selection
while True:
    print("Where would you like to go next?")
    print("Maurin's Butcher Shop (1), Cemetery (locked) (2)")
    option_2 = input()

    if option_2 == "1":
        print(f"{name} has entered Maurin's Butcher Shop.")
        break
    else:
        print("Did you not hear what Matilda said?!")
        # Loop back to option 2
        continue

# Dialogue with the butcher
print("The butcher's shop stands as a grim reminder of the town's former vitality. The building is dark and dilapidated, with its thatched roof sagging and its wooden sign hanging askew. Inside, the air is thick with the smell of decay, and the floor is covered in a layer of grime. The meat, once fresh and plentiful, is now scarce and of questionable quality, hanging limply from rusty hooks. The atmosphere is oppressive and cold, with an eerie silence that only adds to the sense of desolation.")
input()
print("Upon the tolling of the door bell, a hulking figure with a grim demeanour and a perpetual scowl turns. His once-burly frame is now gaunt and his skin pallid, giving him a ghostly appearance. The butcher’s eyes, dark and hollow, reflect years of struggle and disillusionment. His hands are calloused and stained, and he wears a blood-stained apron that has seen better days. Despite his imposing presence, there is an air of resignation about him, as if he has long given up hope. He reveals his name as Maurin and speaks in a gruff, almost resentful tone, and his interactions with you are terse and begrudging.")
while True:
    input()
    print("Maurin: Hello, you want somethin'?  Perhaps some meat? I got some offcuts of wild boar... kinda fresh.")
    print("Yes (1), No (2)")
    option_3 = input()

    # Loop for butcher's interaction
    if option_3 == "1":
        print("Maurin: How would you like to pay?")
        input()
        print(f"{name}: I've only got a couple of bronze coins.")
        input()
        print("Maurin:  How about that ring you're wearing?")
        input()
        print(f"{name}: For a piece of greying boar meat?  Seems a bit much - how about, you also send your next fresh catch to the orphanage.")
        input()
        print("Maurin: Okay, fine - So the ring?")
        input()
        print("Ring (1)")
        option_4 = input()

        if option_4 == "1" and "ring" in items:
            print("You have bought the meat.")
            items.pop(0)  # Remove the ring
            items.append("fresh meat")  # Add the fresh meat
            break
        else:
            print("You don't have the ring!")
    else:
        print("Well, what did you come in for?!")
        continue

while True:
    # Return to town and more interactions
    print("Would you like to go back to the town square? (1) Yes, (2) No")
    # There is an error here, where not wanting to buy meat goes straight to asking whether to leave, and if you say no, it goes straight to the cemetery.
    option_5 = input()

    if option_5 == "1":
        print("As you walk back through the deserted town square, you notice that Matilda has now gone.  You spot a large rat with half its tail missing, feasting on another rat’s intestines - this turns your stomach.")
        break
        # Interaction in town
    else:
        print("You wait around in the butchers shop for a while")
        continue

while True:
    print("Would you like to enter the cemetery? (1) Yes, (2) No")
    option_6 = input()

    if option_6 == "1":
        print(f"{name} has entered the cemetery.")
        break
    else:
        print("You decide to stare at the cannibalistic rat a little longer...")
        continue

# Encounter with a wild dog
print("The cemetery is a sombre place, shrouded in mist and silence. Ancient tombstones jut from the ground at odd angles, their inscriptions worn and faded by time. Gnarled trees, bare of leaves, cast long shadows across the overgrown paths. A chill hangs in the air, and the only sound is the distant hoot of an owl. As you venture deeper, the sense of foreboding grows stronger, and you hear the low growl of a dog echoing through the gloom.")
input()
print("The dog is a pitiful sight, with matted fur and a gaunt frame. Its eyes are wild and bloodshot, and it growls menacingly as you approach. Despite its weakened state, the dog is fiercely aggressive, driven by hunger and desperation. Its once noble features are now twisted and scarred, a shadow of the loyal companion it once was.")
input()
print("The dog approaches you.")
print(f"What will you do, {name}?")
print("Fight (1), Explore inventory (2)")
option_7 = input()

if option_7 == "2":
    print(f"You have {items}. (1) Use first item")
    option_8 = input()
    if option_8 == "1": #and items
        print(f"You have selected {items[0]}. Would you like to use it? (1) Yes, (2) No")
        option_9 = input()
        if option_9 == "1":
            print(f"You have used {items[0]}.")
            items.pop(0)  # Remove the used item
            print("The dog has become ecstatic at the sight of the meat, and instantly calms - becoming almost obedient.  Once the dog has eaten, he signals for you to follow him.  He leads you to an opening in the fence with a path that leads to the dark forest.")
        else:
            print("The dog approaches baring its fangs and growling viciously")
            enemy = Enemy(30, 3,  "Dog")
            if combat():
                print("The dog falls to the ground with a yelp")
            else:
                print("You were defeated by a dog. Game Over.")
                exit()
        print(f"{name} has found the way to the dark forest.")
    else:
        print("The dog approaches baring its fangs and growling viciously")
        enemy = Enemy(30, 3,  "Dog")
        if combat():
            print("The dog falls to the ground with a yelp")
        else:
            print("You were defeated by a dog. Game Over.")
            exit()

else:
    print("The dog approaches baring its fangs and growling viciously")
    enemy = Enemy(30, 3,  "Dog")
    if combat():
        print("The dog falls to the ground with a yelp")
    else:
        print("You were defeated by a dog. Game Over.")
        exit()


# Scene transition to the dark forest
while True:
    print("Would you like to enter the dark forest? Yes (1), No (2)")
    option_10 = input()

    if option_10 == "1":
        print("You have entered the dark forest.")
        input()
        print("The dark forest is an imposing and eerie place, its dense canopy blocking out much of the light. Twisted trees with gnarled branches loom overhead, their trunks covered in thick moss. The air is damp and filled with the sounds of unseen creatures. As you move cautiously through the underbrush, the forest seems to close in around you, every rustle and snap setting your nerves on edge.")
        break
        # Dark forest interaction
    else:
        print("You explore the cemetary a little longer. A chill runs down your spine as you walk between the graves")


# Encounter with the dead knight's pouch
dark = True
print("As your eyes adjust, you come across a dead knight's corpse lying on the side of the dirt path.  There is a pouch lying next to the corpse.")
print("Would you like to open the pouch? Yes (1), No (2)")
option_11 = input()

if option_11 == "1":
    print(f"{name} has found a torch.")
    items.append("torch")

    print("Would you like to equip the torch? Yes (1), No (2)")
    option_12 = input()

    if option_12 == "1":
        print("Your first instinct is to check that the corpse isn't your brother - you breathe a sigh of relief when you see that it is not.  As you look up, you notice that the torchlight has transformed the forsest. The once ominous shadows retreat, replaced by a warm, inviting glow that reveals several berry bushes.")
        dark = False
    else:
        print("This is what happens if you don't equip the torch.")
else:
    print("You feel that it is rude to open another Knight's belongings - perhaps this is being too noble, and indeed a little stupid?")


if not dark:
    print("You pick and eat some of the berries - suddenly you feel stronger, and you start to relax")
    print(f"{name} is restored to full health")
    #mc relaxes and gets healed
    mc.health = 30
    #describe approaching bandit
    print("Suddenly, you hear a rustling in the bushes.  A bandit stands before you, a grizzled veteran with a patch over one eye and a cruel smile. He wields a rusty sword that has seen better days.  He looks ready for a fight.")
    enemy = Enemy(20, 6, "bandit")
    if combat():
        print("As the bandit's body hits the ground for in a heavy thud, you breathe a sigh of relief and regroup your thoughts.  That's when you notice a cave hidden behind a curtain of vines, and nestled at the base of a rocky hill. After taking a few moments to recover you strenght, you pick up your torch and head inside.")
    else:
        print("You have been slain by the bandit.  Game Over.")
        exit()

else:
    #mc is suprised by bandit
    print("Suddenly, you hear a rustling in the bushes.  A bandit stands before you, a grizzled veteran with a patch over one eye and a cruel smile. He wields a rusty sword that has seen better days.  He looks ready for a fight.")
    enemy = Enemy(20, 6, "bandit")
    if combat():
        print("As the bandit's body hits the ground for in a heavy thud, you breathe a sigh of relief and regroup your thoughts.  That's when you notice a cave hidden behind a curtain of vines, and nestled at the base of a rocky hill. After taking a few moments to recover you strenght, you pick up the bandit's torch and head inside.")
        dark = False
    else:
        print("You have been slain by the bandit.  Game Over.")
        exit()

#find cave text
print(f"{name} restored 10 health")
mc.health += 10
if mc.health < 30:
    mc.health = 30
input()
print("Inside the cave, the air is cool and damp, and the walls glisten with moisture. The passageways are narrow and winding, the silence broken only by the occasional drip of water echoing through the caverns. As you delve deeper, the cave opens up into a vast chamber, illuminated by an eerie, phosphorescent glow.")
input()
print("At the heart of the chamber stands the witch, her eyes gleaming with malevolent intent, ready for the final confrontation.  This must be Morgoth, the witch that Ealdred warned you about.")
input()
print("Morgath is a powerful sorceress, shrouded in dark robes that seem to blend into the shadows. Her eyes burn with an intense, malevolent light, and her long, black hair flows like a river of ink. She wields a staff carved with ancient runes and crackling with dark energy. Morgath's voice is both mesmerizing and terrifying, capable of ensnaring the minds of those who listen. She is cunning, ruthless, and will stop at nothing to achieve her dark ambitions.")
#boss text
enemy = Enemy(65,7, "Margoth")
if boss_combat():
    print("With a final, powerful strike, you bring Morgath to her knees. The sorceress's dark magic fades, and the oppressive atmosphere in the cave lifts. As Morgath's life slips away, she curses you one last time before falling silent.")
    input()
    print("As you survey the cave, now quiet except for the sound of your heartbeat racing in your head.  In a hidden alcove, you find a small cell. Inside, your brother lies motionless.")
    input()
    print("'Brother...' your voice breaks as you kneel beside the lifeless body, tears streaming down your face.")
    input()
    print("The journey back to the village is a somber one. You carry your brother's body, your heart heavy with grief. The townspeople gather in the square, their initial hope turning to sorrow as they see your burden. Despite defeating Morgath and lifting the curse, the victory feels hollow.")
    print("The village begins the painful process of mourning and healing, and you, though hailed as a hero, carry the weight of your loss. You vow to honour your brother's memory by finding home in Clayvault and vowing to protect the village and ensure that such darkness never falls upon it again. The curse is broken, but the scars remain.")
else:
    print("Morgoth has killed you.  Game Over.")
    exit()


for x in range(3):
    if input() == "ABRAXAS":
        input("_;_")
        mc.health = 100
        mc.attack = 10
        counter = 0
        while True:
            counter+=1
            enemy = Enemy(counter, counter/2, "Apostle")
            if combat():
                print("Another approaches")
                continue
            else:
                print(f"killed {counter-1} apostles")
                break