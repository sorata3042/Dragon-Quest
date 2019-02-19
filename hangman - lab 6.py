#Steven Chau
#Lab Assignment 6
#Hangman: Pokemon Gen 1-4
"""
This Hangman Game uses a dictionary of lists and does the following:
a. Asks the user for their name
b. Introduces the Hangman Game
c. Lists of a minimum of 30 words of Pokemon
d. Provide the users with the ability to select which list to use.
e. Only contains words with 5 to 10 characters
f. List of guessed letters
g. List of the incorrect guesses
h. Users are allowed to guess wrong 5 times on the 6th time they lose and
you tell them the word.
i. Verify that what they guessed is a letter in the alphabet
"""

import time
import random

pokemon = {
"1" : [
"bulbasaur", "ivysaur", "venusaur", "charmander", "charmeleon", "charizard",
"squirtle", "wartortle", "blastoise", "caterpie", "metapod", "butterfree",
"weedle", "kakuna", "beedrill", "pidgey", "pidgeotto", "pidgeot",
"rattata", "raticate", "spearow", "fearow", "ekans", "arbok",
"pikachu", "raichu", "sandshrew", "sandslash",
"nidoran", "nidorina", "nidoqueen", "nidorino", "nidoking",
"clefairy", "clefable", "vulpix", "ninetales", "jigglypuff", "wigglytuff",
"zubat", "golbat", "oddish", "gloom", "vileplume", "paras", "parasect",
"venonat", "venomoth", "diglett", "dugtrio", "meowth", "persian",
"psyduck", "golduck", "mankey", "primeape", "growlithe", "arcanine",
"poliwag", "poliwhirl", "poliwrath", "kadabra", "alakazam",
"machop", "machoke", "machanp", "bellsprout", "weepinbell", "victreebell",
"tentacool", "tentacruel", "geodude", "graveler", "golem",
"ponyta", "rapidash", "slowpoke", "slowbro", "magnemite", "magneton",
"farfetchd", "doduo", "dodrio", "dewgong", "grimer", "shelder", "cloyster",
"gastly", "hauntzer", "gengar", "drowzee", "hypno", "krabby", "kingler",
"voltorb", "electrode", "exeggcute", "exeggutor", "cubone", "marowak",
"hitmonlee", "hitmonchan", "lickitung", "koffing", "weezing",
"rhyhorn", "rhydon", "chansey", "tangela", "kangaskhan", "horsea", "seadra",
"goldeen", "seaking", "staryu", "starmie", "scyther", "electabuzz", "magmar",
"pinsir", "tauros", "magikarp", "gyarados", "lapras", "ditto",
"eevee", "vaporeon", "jolteon", "flareon", "porygon", "omanyte", "omastar",
"kabuto", "kabutops", "aerodactyl", "snorlax", "articuno", "zapdos", "moltres",
"dratini", "dragonair", "dragonite", "mewtwo"
],
"2" : [
"chikorita", "bayleef", "meganium", "cyndaquil", "quilava", "typhlosion",
"totodile", "croconaw", "feraligator", "sentret", "furret",
"hoothoot", "noctowl", "ledyba", "ledian", "spinarak", "ariados",
"crobat", "chinchou", "lanturn", "pichu", "cleffa", "igglybuff",
"togepi", "togetic",  "mareep", "flaaffy", "ampharos", "bellossom",
"marill", "azumarill", "sudowoodo", "politoed",
"hoppip", "skiploom", "jumpluff", "aipom", "sunkern", "sunflora", "yanma",
"wooper", "quagsire", "espeon", "umbreon", "murkrow", "slowking", "misdreavus",
"uknown", "wobbuffet", "girafarig", "pineco", "forretress", "dunsparce",
"gligar", "steelix", "snubbull", "granbull", "qwilfish", "scizor", "shuckle",
"heracross", "sneasel", "teddiursa", "ursaring", "slugma", "magcargo",
"swinub", "piloswine", "corsola", "remoraid", "octillery", "delibird",
"mantine", "skarmory", "houndour", "houndoom", "kingdra", "phanpy", "donphan",
"stantler", "smeargle", "tyrogue", "hitmontop", "smoochum", "elekid", "magby",
"miltank", "blissey", "raikou", "entei", "suicune",
"larvitar", "pupitar", "tyranitar", "lugia", "hooh", "celebi"
],
"3" : [
"treecko", "grovyle", "sceptile", "torchic", "combusken", "blaziken",
"mudkip", "marshtomp", "swampert", "poochyena", "mightyena",
"zigzagoon", "linoone", "wurmple", "silcoon", "beautifly", "cascoon", "dustox",
"lotad", "lombre", "ludicolo", "seedot", "nuzleaf", "shiftry",
"taillow", "swellow", "wingull", "pelipper", "ralts", "kirlia", "gardevoir",
"surskit", "masquerain", "shroomish", "breloom", "slakoth", "vigoroth", "slaking",
"nincada", "ninjask", "shedinja", "whismur", "loudred", "exploud",
"makuhita", "hariyama", "azurill", "nosepass", "skitty", "delcatty",
"sableye", "mawile", "lairon", "aggron", "meditite", "medicham",
"electrike", "manectric", "plusle", "minun", "volbeat", "illumise", "roselia",
"gulpin", "swalot", "carvanha", "sharpedo", "wailmer", "wailord",
"numel", "camerupt", "torkoal", "spoink", "grumpig", "spinda",
"trapinch", "vibrava", "flygon", "cacnea", "cacturne",
"swablu", "altaria", "zangoose", "seviper", "lunatone", "solrock",
"barboach", "whiscash", "corphish", "crawdaunt", "baltoy", "claydol",
"lileep", "cradily", "anorith", "armaldo", "feebas", "milotic",
"castform", "kecleon", "shuppet", "banette", "duskull", "dusclops", "tropius",
"chimecho", "absol", "wynaut", "snorunt", "glalie", "spheal", "sealeo", "walrein",
"clamperl", "huntail", "gorebyss", "relicanth", "luvdisc",
"bagon", "shelgon", "salamence", "beldum", "metang", "metagross",
"regirock", "regice", "registeel", "latias", "latios", "kyogre", "groudon",
"rayquaza", "jirachi", "deoxys"
],
"4" : [
"turtwig", "grotle", "torterra", "chimchar", "monferno", "infernape",
"piplup", "prinplup", "empoleon", "starly", "staravia", "staraptor",
"bidoof", "bibarel", "kricketot", "kricketune", "shinx", "luxio", "luxray",
"budew", "roserade", "cranidos", "rampardos", "shieldon", "bastiodon",
"burmy", "wormadam", "mothim", "combee", "vespiquen", "pachirisu",
"buizel", "floatzel", "cherubi", "cherrim", "shellos", "gastrodon",
"ambipom", "drifloon", "drifblim", "buneary", "lopunny", "mismagius",
"honchkrow", "glameow", "purugly", "chingling", "stunky", "skuntank",
"bronzor", "bronzong", "bonsly", "happiny", "chatot", "spiritomb",
"gible", "gabite", "garchomp", "munchlax", "riolu", "lucario",
"hippopotas", "hippowdon", "skorupi", "drapion", "croagunk", "toxicroak",
"carnivine", "finneon", "lumineon", "mantyke", "snover", "abomasnow",
"weavile", "magnezone", "lickilicky", "rhyperior", "tangrowth", "electivire",
"magmortar", "togekiss", "yanmega", "leafeon", "glaceon", "gliscor",
"mamoswine", "porygonz", "gallade", "probopass", "dusknoir", "froslass",
"rotom", "mesprit", "azelf", "dialga", "palkia", "heatran", "regigigas",
"giratina", "cresselia", "phione", "manaphy", "darkrai", "shaymin", "arceus",
"victini"
]}

#Hangman pictures; right limbs are double, otherwise they don't show correctly
HANGMAN = ['''
_________
|       |
|
|
|
|          ''', '''
_________
|       |
|       0
|
|
|          ''', '''
_________
|       |
|       0
|       |
|
|          ''', '''
_________
|       |
|       0
|       |
|      /
|          ''', '''
_________
|       |
|       0
|       |
|      / \\
|          ''', '''
_________
|       |
|       0
|      /|
|      / \\
|          ''', '''
_________
|       |
|       0
|      /|\\
|      / \\
|          ''']

def prompt ():
    #prompts user for name; done before the functions so that the user is prompted once
    name = input ("What is your name?: ")
    print ("Hello " + name + ", welcome to Hangman!")
    time.sleep (1.5)
    print ("You begin with 6 lives in this game, so use them wisely!")
    time.sleep (2)

    #tells the user which topic the game is taking the word from
    print ("The topic of this game is Pokemon: Gen 1, 2, 3, and 4.")
    print ("(Some pokemon names were too short to appear)")
    time.sleep (2)

#picks the word the user has to guess
def pick_word ():
    print ("What Generation Pokemon do you want to guess from?")
    print ("(Generation 1, 2, 3, or 4)" )
    print ("(Please type a number: 1, 2, 3, 4)")
    while True:
        chosentype = input()
        if chosentype in pokemon.keys ():
            secret_list = list (pokemon [chosentype])
            secret_word = random.choice (secret_list)
            break
        else:
            print ("That's not an option.")
            print ("Please, try again.")
    return secret_word

#the beginning code
def intro (secret_word):
    #tells the user how many letters they will have to guess, probably
    print ("I am thinking of a word that is " + str (len (secret_word)) + " letters long.")
    time.sleep (1)

    #displays the number of spaces
    time.sleep(1)
    print (HANGMAN [0])
    print ()

    blank = ["_"] * len (secret_word)

    #Remove the stuff between the spaces
    for letter in blank:
        print(letter, end=' ')

    #prompts the user
    time.sleep (1)
    print ()
    print ("What will your first guess be?")

    return blank

#actual game code
def hangman_GAME (secret_word, blank):
    #stores user guesses
    wrong_letters = []
    correct_letters = []
    letters_guessed = []

    #makes sure the user inputs a letter that has not been guessed
    while True:

        letters_guessed = wrong_letters + correct_letters
        #str.lower makes the guess lowercase
        guess = str.lower(input ("Please input a letter: "))

        if len (guess) != 1:
            print ("Please enter a single letter.")
        elif guess in letters_guessed:
            print ("You have already tried that letter. Please, try again.")
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print ("Please, enter a letter.")
        else:
            #print (list (secret_word))
            if guess in list (secret_word):
                #if guess in secret_word:
                correct_letters += guess

                print ("Wrong letters you have guessed: " )
                print (wrong_letters)

                #Replace blanks with correctly guessed letters.
                for i in range (len (secret_word)):
                    if secret_word[i] in correct_letters:
                        blank = blank[:i] + (list ((secret_word)[i])) + blank[i+1:]

                print ("The word so far: " )
                for letter in blank:
                    print(letter, end=' ')
                print()

                #print (letters_guessed)
                if all (item in correct_letters for item in list (secret_word)):
                    print ("Congratulations!! You have won!!!")
                    print ("The word is " + secret_word + ".")
                    break
                else:
                    print ("Good job. Continue guessing!")
                    print ()
            else:
                print ()
                print ("Oh no! That's not in the word!!")
                wrong_letters += guess
                print ("Wrong letters you have guessed: " )
                print (wrong_letters)
                print ("The word so far: ")
                for letter in blank: # Show the secret word with spaces in between each letter.
                    print(letter, end=' ')
                print()

                if len (wrong_letters) <= 5:
                    print (HANGMAN [0 + len(wrong_letters)])
                else:
                    print (HANGMAN [6])
                    print ("Oh no, you're out of lives!!")
                    time.sleep (0.5)
                    print ("The word is " + secret_word + ".")
                    print ("GAME OVER")
                    break

#sets up loop and game
prompt ()
play_again = "yes"
while play_again == "yes":
    word = pick_word ()
    start = intro (word)
    hangman_GAME (word, start)

    time.sleep (0.5)
    print ()
    time.sleep (1)

    print ("Do you wish to play again?")
    print ("(To play again, type yes; else, it closes)")
    play_again = str.lower(input())
    print ()
