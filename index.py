from time import sleep
import sys
# Colours

from termcolor import colored

ps = colored('(Pet Snail)', 'blue')
you = colored('(You)', 'magenta')

shoots = colored('*shoots*', 'red')
fingers = colored('*eats fingers and toes*', 'red')

cuts = colored('*cuts toes and fingers out of old ladys stomach*', 'red')
demon = colored('demon...', 'red')
lady = colored('(Old Lady/Demonic Demon)', 'red')

man = colored('(Shop Keeper)', 'green')
almost = colored('almost...', 'blue')

stab = colored('stabs you', 'red')

limbs = colored('eats limbs', 'red')

news = colored('DAILY NEWS', 'blue')
# Intro

name = input('What is your name? ')
print(f'Welcome, {name}!\n')
sleep(1)
print('There has been a monster terrorizing this land for many years...')
sleep(2.5)
print(f'You, {name} are the only person who can truly stop him...')
sleep(2)
print(
    f'{name}, Be Careful... You need to pick the right cave on Mount Luckula.')

# Game Functions


def gameover():
    print('You have died...')
    sleep(.5)
    print(news)
    print(f'{name} has died')
    sys.exit()


# Accept

accept = input('Do you wish to accept this quest? (yes/no) ').lower()

if accept == 'yes':
    print('Ok, good.')
else:
    rusure = input('Are you sure? (yes/no) ').lower()
    rusure.lower()
    if rusure == 'yes':
        print(f'😭Goodbye, {name}😭')
        gameover()
    else:
        print('Thank you.')

# House

sleep(2)
print(
    '\nAfter that talk, you head home to try and get some sleep as tommorow is gonna be a big day...'
)
sleep(3)
print(
    'As the big day grows nearer you just cant seem to sleep so you consult your pet snail...\n'
)
sleep(1.5)
print(f'{ps} Wewee!')
sleep(1.5)
print(f'{you} Well that wasnt useful *licks snails head*')
sleep(1.5)
print(f'{ps} HOIYAAAAAAAAA')
sleep(1.5)
print(f'{you} Wait... You can talk????')
sleep(1.5)
print(f'{ps} Yes i can, i mean why else would you talk to me weirdo???')
sleep(1.5)
print(f'{you} Can you help me on my journey?')
sleep(1.5)
print(f'{ps} No im a snail dummy.')
sleep(1.5)
print(f'{ps} Bring your dog!')
sleep(1.5)
print(f'{you} No hes to special.')
sleep(1.5)
print(f'{ps} Then bring your pet rock, loser!')
sleep(1.5)
print(f'{you} ...')
sleep(1.5)

# Anger Snail

anger = input('\nYell at pet snail? (yes/no) ').lower()
if anger == 'yes':
    print(f'{ps} {shoots}')
    sleep(2)
    print(f'{ps} {fingers}\n')
    sleep(1)
    gameover()
if anger == 'no':
    print('You chose to not yell at your pet snail.\n')

# Entering Town

sleep(1)
print('After that chat with your pet snail you head to town...')
sleep(1)
print('You see an old lady...\n')
sleep(1)

# Old lady

n = input('lick old lady (1) /punch old lady (2) : ').lower()
if n == "1":
    print(f'\nThe old lady turns into a {demon}')
    sleep(1)
    print(fingers)
    sleep(1)
    print(f'{lady} Well that was easy.')
    sleep(1)
    print(cuts)
    sleep(1)
    print(
        f'{you} Eeewww my toes and fingers, there all wet and soggy better put them in the dryer'
    )
    sleep(1)
if n == '2':
    print('\nThe old lady crumbles to ash at your feet...')
    sleep(1)
    print(
        'You run for help but fall into a ditch and sadly lose your head from gas.'
    )
    sleep(1)
    gameover()

    # Dryer

    meep = input('Put in dryer (yes/no): ').lower()
    if meep == "yes":
        print('You realise your toes have a weird mark on them...')
        sleep(1)
        seww = input('Do you sew them back on? (yes/no)').lower()
        if seww == "yes":
            print(
                'As soon as your toe gets back on it starts bending around in all directions before settling down...'
            )
            sleep(1)
            print('You realize you have now been cursed!')
            sleep(1)
            print(f'A {demon} Comes out of you...')
            sleep(1)
            print('GAME OVER')
            gameover()
        else:
            print('You throw your toes in the bin...')
            sleep(1)

# Shop

shop = input(
    '\nYou keep contemplating if you want to head into the shop or not. Head into the shop? (yes/no) '
).lower()
if shop == 'yes':
    print(f'{man} Welcome to the shop.')
    sleep(1)
    haha = input(f'{man} Would you like to buy anything? (yes/no) ').lower()
    if haha == 'yes':
        print(f'{you} Yes.')
        sleep(1)
        print(f'{man} What would you like to purchase?')
        sleep(1)
        print(f'{man} We have {almost} Anything you can imagine!')
        sleep(1)
        roll = input(
            f'{man} Would you like to get a bread roll? This kind lady makes them for us every day! (yes/no) '
        ).lower()

        if roll == 'yes':
            print(f'{you} Yes please, How much is it?')
            sleep(1)
            print(f'{man} $2.30.')
            sleep(1)
            print('*purchases*')
            sleep(1)
            print('*eats bread roll inside shop*')
            sleep(1)
            print(f'{you} Why does this taste like human?')
            sleep(1)
            print(
                f'{man} Please, save me the lecture. There is no human in there! Its all organic...'
            )
            sleep(1)
            print(f'{you} ...')
            sleep(1)
            kill = input('Kill shop keeper? (yes/no) ').lower()
            if kill == "yes":
                print(f'{you} DIE!')
                sleep(1)
                print(
                    "*shoots epik lasers out of hands onto shop keepers head*")
                sleep(1)
                print(f'{man} I want a refund... ')
                sleep(1)
                print(f'{man} *dies*')
            else:
                print(
                    'You throw the leftover bread roll at the shop keeper and leave the store to return outside.\n'
                )
            if kill == 'no':
                print(
                    'You run out of the store with the bread roll in hand ready to kill anyone and anything in your way.'
                )
                sleep(1)
                print('Except for dogs offcourse, cats? Eh your choice.\n')
                sleep(1)
        if roll == 'no':
            print(f'{you} No thanks, I will not be buying anything.')
            sleep(1)
            print(f'{man} Why? Too fancy? *grabs gun*')
            sleep(1)
            print(f'{you} No you stinky shart nugget')
            sleep(1)
            print(f'{man} *shoots*')
            gameover()

print('You walk outside to see a lady staring at you creepily...')
sleep(1)
print('The mysterious lady does the chrissy crumble and doesnt wake up...')
sleep(1)

# Home

home = input('Head home? (yes/no) ').lower()
if home == 'yes':
    print('You decide to head home.')
if home == 'no':
    print('You decide to not head home.')
    sleep(1)
    print('After deciding not to go home')
    sleep(1)
    print(f'You head down the street where the old lady {stab}')
    sleep(2)
    print('GAME OVER')
    gameover()

# Stone Axe AKA The Hog AKA The North Korean Government

print(
    'You head home and look for your stone axe that you remember leaving in your room somewhere.'
)
sleep(1)
print('You enter your room and find a mysterious door under your wardrobe...')
sleep(1)
eakw = input('Open the door? (yes/no) ').lower()
if eakw == 'yes':
    print(
        'You walk down a long mysterious stair way leading you to a fork end')
    sleep(1)
    print('You feel kind of queasy')
    sleep(1)
    woahth = input('Head left or right? (left/right) ').lower()
    if woahth == 'left':
        print('You enter another dark hallway that leads to light...')
        sleep(1)
        print('The light has a red button on it saying "DO NOT PRESS"')
        press = input('Press the red button? (yes/no) ').lower()
        if press == 'yes':
            print('You blew up your house.')
            sleep(1)
            print(
                'You did this because nuclear bombs launched from korea and hit your house.'
            )
            gameover()

        if press == 'no':
            print(
                'You decide to not press the button but to enter the door you noticed to the right of you.'
            )
            sleep(2)
            print('You open the door and enter...')
            sleep(1)
            print(
                'You realize you shouldnt have done that as the korean government have now seen what you look like but they let you pass anyway and let you out of the door under your wardrobe.'
            )
            print(f'{you} Well that was weird')
            print(f'{you} Welp at least now i have my very own axe 😊')
    if woahth == 'right':
        print(
            'A wild hog chases you down the road snorting like peppa pig while eating human guts.'
        )
        sleep(2)
        print(
            'The hog soon catches up to you and rips off your limbs making you unable to walk any futher.'
        )
        sleep(1)
        print('The hog now has ate your head off.')
        sleep(1)
        print('GAME OVER')
        gameover()

if eakw == 'no':
    print(
        'You decide to not head into the room and continue looking for your stone axe.'
    )
    sleep(1)
    print(
        'A wild hog enters your house through the door under your wardrobe and destroys your bed then goes to attack your limbs'
    )
    sleep(1)
    print(f'(Hog) *{limbs}*')
    sleep(1)
    print(
        'You realize you made a bad choice as the hog rips off your head in a painful twist'
    )
    sleep(1)
    print('GAME OVER')
    sleep(1)
    print('You lost to the hog from under the door under your wardrobe')
    gameover()

# Mountain/Island

mori = input(
    'You find two paths, one heading left, the other heading straight. (left/straight)'
).lower()
if mori == 'left':
    print('You head left and find a path leading somewhere.')
    sleep(1)

if mori == 'straight':
    print('You head straight and find a path to a large mountain...')
    sleep(1)
    print('You find a little shed, a large tree and a pen.')
    sleep(1)
    shedopen = input('Head inside the shed or the pen? (pen/shed)').lower()
    sleep(1)
    if shedopen == 'shed':
        print('You enter the shed and find a large box sitting ontop of hay.')
        sleep(1)
        open = input('Open the box? (yes/no) ').lower()
        if open == 'yes':
            print(
                'You decide to open the box and find a dinosaur sleeping inside of it with an egg wrapped in plastic film.'
            )
            sleep(1)
            print(
                'The dinosaur slowly wakes up while screeching something in a foreign language.'
            )
            sleep(1)
            print(
                'You start to run as the dinosaur has fully waken up and is chasing you at high speed.'
            )
            sleep(1)
            print(
                'You run into a large tree and smack the dinosaurs head on it.'
            )
            sleep(1)
            print(
                'The dinosaur falls to the ground and you are able to see its guts. You decide to run away after witnessing that gruesome moment...'
            )
            sleep(1)

        if open == "no":
            print(
                'You decide to not open the box but to put hay all over it instead.'
            )
            sleep(1)
            print(
                'A dinosaur comes out of the box while screaming in a foreign language'
            )
            sleep(1)
            print('You run away while screaming in a foreign language')
            sleep(1)
            print(
                'The dinosaur quickly catches up to you while drooling as he is hungry...'
            )
            sleep(1)
            print(
                'You rush into a pen and find a large metal door with a big red button that reads CLOSE.'
            )
            sleep(1)
            close = input('Close the door? (y/n) ').lower()
            if close == 'y':
                print(
                    'You decide to close the door and walk down the path while the dinosaur is bashing its head into the large door trying to get to you.'
                )
                sleep(1)
                print(
                    'This bashing continues for the next few seconds before you hear silence and think "Hmm, must of died already."'
                )
                sleep(1)
                print(
                    'You find an exit to the outside world and decide to walk outside following the path. '
                )
                sleep(1)

            if close == "n":
                print(
                    'You decide to not close the door but run to find an exit to the outside world but run into a tree and the dinosaur catches up to you...'
                )
                sleep(1)
                print(
                    'The dinosaur catches up to you and rips you apart head to toe.'
                )
                sleep(1)
                gameover()
    if shedopen == 'pen':
        print('You decide to head to the pen next to the shed.')
        sleep(1)
        print('You find a large egg wrapped in a cocoon.')
        sleep(1)
        nani = input('Open the egg? (y/n) ').lower()
        if nani == 'y':
            print(
                'You decide to open the egg and find a large dinosaur sleeping inside of it.'
            )
            sleep(1)
            print('The dinosaur wakes up and eats your head off.')
            gameover()
        if nani == 'n':
            print('You decide to not open the egg.')
            sleep(1)

print('You find a large island and decide to walk to it.')
sleep(1)
print('On the a small blue gem.')
pwa = input('(pickup/leave) ').lower()
if pwa == 'pickup':
    print('You pick up the gem and walk to a small shed next to a power box.')
    sleep(1)
    print(
        'You walk inside the shed and find a small microscope ontop of a small shelf.'
    )
    sleep(1)
    print('You grab the microscope and place it onto a bench.')
    look = input('Look inside of the microscope? (y/n) ').lower()
    if look == 'y':
        print('You decide to look inside of the microscope.')
        sleep(1)
        print('You find a small crystal of silicon.')
        sleep(1)
        print(
            'Your chest starts to tighten, you have difficulty breathing and then...'
        )
        sleep(3)
        print('BAM')
        sleep(1)
        print('You pass out...')

    if look == 'n':
        print('You decide to not look inside of the microscope.')
        sleep(1)
        print(
            'Your chest starts to tighten, you have difficulty breathing and then...'
        )
        sleep(3)
        print('BAM')
        sleep(1)
        print('You pass out...')

if pwa == 'leave':
    print('You leave the shed and walk to the outside world.')
    sleep(1)
    print(
        'You feel something attach to your chest and you feel a little bit of a tightness...'
    )
    sleep(3)
    print('You suddenly pass out...')

sleep(1)
print('You open your eyes and you see Tardigrades (water bears).')
sleep(1)
seethem = input('Want to know more about Tardigrades? (y/n) ').lower()
if seethem == 'y':
    print('LENGTH')
    print('0-0IN')
    print('0-0.1cm')
    sleep(2)
    print('DIET')
    print('Omnivore')
    print('plant cells, algae, small invertabrates')
    sleep(2)
    print("They're the first animal known to survive in outer space.")
    print(
        "The 2014 science documentary show Cosmos: A Spacetime Odyssey mentions tardigrades in the second episode on biological evolution."
    )
    sleep(2)
    print('FACTS')
    print('They can go decades without food or water.')
    print('They can survive an atomic bomb.')
    print(
        "• Tardigrades have been on Earth for about 600 million years, about 400 million years before dinosaurs."
    )

    print('• Tardigrades are sometimes called “moss piglets.”')
    print("• Tardigrade eggs take between 40 and 90 days to hatch.")
    print('Thats all i have coded so far! Thanks for playing!')
