from random import randint


class Player:
    def __init__(self, health, damage, shield):
        self.health = health
        self.damage = damage
        self.shield = shield

mc = Player(20, 5, 0)

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
            if enemy_move == 1:
                print(f"The {enemy.name} is eyeing you up")
            elif enemy_move > 4:
                print(f"The {enemy.name} is ready to attack")
            elif enemy_move >1:
                print(f"The {enemy.name} is preparing a heavy attack")


        player_turn(mc_modifier)
        if enemy.health < 1:
            return True


        if stunned:
            stunned = False 
            continue

        if dark:
            enemy_modifier *= 1.5

        if enemy_move > 4:
            print(f"The {enemy.name} attacks you for {enemy.damage*enemy_modifier} damage")
            mc.shield -= enemy.damage * enemy_modifier
            if mc.shield < 0:
                mc.health += mc.shield

        elif enemy_move > 1:
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
                print("enrage text")
                enraged = True

            elif enemy_move == 2:
                print("charm/weaken text")
                mc_modifier *= 0.5

            elif enemy_move == 3:
                print("margoth's damage increases text")
                enemy.damage += 2

            else:
                print("lifesteal text")
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
# enemy = Enemy(num, num, name) Changes stats of enemy
# combat() starts fight
# boss_combat() starts boss fight








##player_health
#dog_health
#bandit_health
#boss_health
items = ['ring']
dark = False

# Introduction and initial dialogue
print("You, a former knight, awaken in a dimly lit room, the air thick with the scent of herbs and burning candles. The wooden beams overhead creak softly as you sit up on the rough-hewn bed. Shadows dance on the stone walls, cast by the flickering light of a single lantern. The room is cluttered with strange trinkets, jars of mysterious substances, and ancient tomes. A sense of eerie calm fills the space, and as your eyes adjust, you notice a kind-faced stranger watching over you, concern etched into their features.")
input()
print("???: Hello traveler, you're safe here.  I found you unconcious out in the forest, so brought you back to my home to rest.  I was worried you wouldn't pull through.  What's your name?")
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
print("You turn and you see a woman staring from the corner of a cobbled street, leading down to an orphanage.  She is a weary and cautious figure, with lines of worry etched deeply into her face. Her once-bright green eyes are now dulled by years of hardship and mistrust. She has short, curly brown hair, now streaked with grey, and she dresses in worn, practical clothing that has seen better days. She introduces herself as Matilda, and though she reluctantly helps the protagonist, her distrust is evident, and she constantly glances over her shoulder as if expecting trouble.")
input()
print("???: You ought to watch where you go in this town.  It's no place for a stranger.  My name is Matilda, and I take care of the kids down in that orphanage down there.  This town is filled with a lot of sadness and tragedy.")
input()
print("Matilda: You're heading through the cemetery?  Be careful - I've heard of a wild dog lurking around there - it's eaten a couple of my orphans who explored a little too far. Rumour is that its former owner died and is buried there, so it has settled by their grave.  If you can rid the town of that dog, you'd be bringing Clayvault a little bit of relief.  Regarding the forest, you'd be wise to grab some supplies before you go - Maurin's Butcher has some meat and bread for sale - just be sure to give it a sniff first!")

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

# Dialogue with the butcher
print("The butcher's shop stands as a grim reminder of the town's former vitality. The building is dark and dilapidated, with its thatched roof sagging and its wooden sign hanging askew. Inside, the air is thick with the smell of decay, and the floor is covered in a layer of grime. The meat, once fresh and plentiful, is now scarce and of questionable quality, hanging limply from rusty hooks. The atmosphere is oppressive and cold, with an eerie silence that only adds to the sense of desolation.")
input()
print("Upon the tolling of the door bell, a hulking figure with a grim demeanour and a perpetual scowl turns. His once-burly frame is now gaunt and his skin pallid, giving him a ghostly appearance. The butcher’s eyes, dark and hollow, reflect years of struggle and disillusionment. His hands are calloused and stained, and he wears a blood-stained apron that has seen better days. Despite his imposing presence, there is an air of resignation about him, as if he has long given up hope. He reveals his name as Maurin and speaks in a gruff, almost resentful tone, and his interactions with you are terse and begrudging.")
input()
print("Maurin: Hello, you want somethin'?  Perhaps some meat? I got some offcuts of wild boar... kinda fresh.")
print("Yes (1), No (2)")
option_3 = input()

# Loop for butcher's interaction
while True:
    if option_3 == "1":
        print("Maurin: How would you like to pay?")
        print(f"{name}: I've only got a couple of bronze coins.")
        print("Maurin:  How about that ring you're wearing?")
        print(f"{name}: For a piece of greying boar meat?  Seems a bit much - how about, you also send your next fresh catch to the orphanage.")
        print("Maurin: Okay, fine - So the ring?")
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
        print("Okay, let me know if there's anything else.")
        break

# Return to town and more interactions
print("Some text.")
print("Would you like to go back to the town square? (1) Yes, (2) No")
option_5 = input()

if option_5 == "1":
    print("As you walk back through the deserted town square, you notice that Matilda has now gone.  You spot a large rat with half its tail missing, feasting on another rat’s intestines - this turns your stomach.")
    # Interaction in town

print("Would you like to enter the cemetery? (1) Yes, (2) No")
option_6 = input()

if option_6 == "1":
    print(f"{name} has entered the cemetery.")
else:
    print("You decide to stare at the cannibalistic rat a little longer...")

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
    print(f"You have {items}. (1) Use first item (2) Use second item")
else:
    print("Fight dog text.")
    # Placeholder for combat function

# Select an item to use
option_8 = input()
if option_8 == "1" and items:
    print(f"You have selected {items[0]}. Would you like to use it? (1) Yes, (2) No")
    option_9 = input()

    if option_9 == "1":
        print(f"You have used {items[0]}.")
        items.pop(0)  # Remove the used item
    else:
        print("Placeholder fight scene thing.")
        print(f"{name} has found the way to the dark forest.")
else:
    print("You don't have any usable items!")

# Scene transition to the dark forest
print("The dog has become ecstatic at the sight of the meat, and instantly calms - becoming almost obedient.  Once the dog has eaten, he signals for you to follow him.  He leads you to an opening in the fence with a path that leads to the dark forest.")
print("Would you like to enter the dark forest? Yes (1), No (2)")
option_10 = input()

if option_10 == "1":
    print("You have entered the dark forest.  The dog stays behind, presumably to return to his master's grave.")
    input()
    print("The dark forest is an imposing and eerie place, its dense canopy blocking out much of the light. Twisted trees with gnarled branches loom overhead, their trunks covered in thick moss. The air is damp and filled with the sounds of unseen creatures. As you move cautiously through the underbrush, the forest seems to close in around you, every rustle and snap setting your nerves on edge.")
    # Dark forest interaction

# Encounter with the dead knight's pouch
print("As your eyes adjust, you come across a dead knight's corpse lying on the side of the dirt path.  There is a pouch lying next to the corpse.")
print("Would you like to open the pouch? Yes (1), No (2)")
option_11 = input()

if option_11 == "1":
    print(f"{name} has found a torch.")
    items.append("torch")

    print("Would you like to equip the torch? Yes (1), No (2)")
    option_12 = input()

    if option_12 == "1":
        print("Your first instinct is to check that the corpse isn't your brother - you breathe a sigh of relief when you see that it is not.  As you look up, you notice that the torchlight has transformed the forsest. The once ominous shadows retreat, replaced by a warm, inviting glow that reveals several berry bushes.  The player is given an opportunity to eat the berries and restore HP.  After this, bandit’s approach and attack.")
        # Should we input something about berries HP here?
    else:
        print("This is what happens if you don't equip the torch.")
else:
    print("You feel that it is rude to open another Knight's belongings - perhaps this is being too noble, and indeed a little stupid?")