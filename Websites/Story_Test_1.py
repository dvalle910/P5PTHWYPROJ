from time import sleep
import sys

# This is the story code for my story game made with the assistance of Thomas Ortiz
"""
\"The Hyperborean Solstice\"
Interactive Fiction
Diego Valle & Thomas Ortiz
"""


def story_mode():
    title = "The Bitter Solstace"
    print (title.center(19))
    print(" ")
    print("*TANK turns TV on*")
    print (" News Roprter: Hi Mike! So tell us... How is the project going along, you know... The... secret one. ")
    print ("Mike Schwartzkanoff: Nice for you to ask of that, yes we've completed the suits to venture into that beastly forest, we may now figure out what is wrong with that cursed plot. It will only-")
    print("*Your TV seemed to cut out...*")
    print (""" TANK: Man... I have to tell what just happened to BOMAR! We can finally steal the suits! We've planned this since we were ten and now is the perfect oppourtunity to stop that corrupted German company by findiny what they want with that forest. Especially for what they did to mom... """)
    KARMA = 0
    try:
        print("")
        decision_1 = input("Do you [call] BOMAR, or [run] to his house?: ")
        if decision_1 == "call":
            KARMA += 1
            print ("You called BOMAR and told him what happened, he decided to come on over to your house to talk \'The Plan\' over.")
        elif decision_1 == "run":
            KARMA += 2
            print ("You ran to BOMAR's house and discussed the report with him.")
        else:
            print("You ruined the story, restart with one of two options.")
        print(""" You and BOMAR talked over the two plans you made.
        #1/TANK, TANK will hack into the electrical grid, allowing you to control all objects that tap into the system for enough of a time for one of you to go and steal the four suits in their compacted form.
        #2/BOMAR, You go all out and destroy everything causing all chaos """)
        print("")
        decision_2 = input("Will you go with your\[TANK]\'s plan, or [BOMAR]\'s plan?: ")
        if decision_2 == "BOMAR":
            print ("BOMAR and TANK infiltrate the facility and using sleep darts, sleep every single guard in sight.")
        elif decision_2 == "TANK":
            print ("TANK hacks system, disabling everything and allowing you complete control of all electronics. You decide who goes in and takes the suits")
            print("")
            decision_3 = input("Will you/[TANK] go as offense, or go with [BOMAR] as offense?: ")
            if decision_3 == "BOMAR":
                print ("BOMAR and TANK find themselves at a fork in the hallway.")
                BOMAR_decision = input("Do you choose the [left] path or the [right] path?: ")
                if BOMAR_decision == "left":
                    print ("TANK and BOMAR enter a room that contains E-DAY-GO, a guard that turned against the facility, and 4 suits. Continuing to the forest, TANK, BOMAR, and E-DAY-GO find a character that wants to help them discover the secret of the forest. When entering the forest, the character that is found has a suit malfunction and dies. BOMAR also has a suit malfunction, but E-DAY-GO gives up his suit to save him. While BOMAR is inspecting something, TANK wonders off and is never heard from again. BOMAR eventually finds out the secret of the forest, but then dies. GAME OVER!!!")
                elif BOMAR_decision == "right":
                    print ("TANK and BOMAR enter a room that contains SHARQUISHQWANIQWA, a guard that turned against the facility, and 4 suits. Continuing to the forest, TANK, BOMAR, and SHARQUISHQWANIQWA find a character that wants to help them discover the secret of the forest. When entering the forest, the character that is found has a suit malfunction and dies. BOMAR also has a suit malfunction, but SHARQUISHQWANIQWA gives up her suit to save him. While BOMAR is inspecting something, TANK wonders off and is never heard from again. BOMAR eventually finds out the secret of the forest, but then dies. GAME OVER!!!")
            elif decision_3 == "TANK":
                print(" ")
                decision_4 = input("You see an [airshaft] and a [corridor], which do you follow?: ")
                if decision_4 == "corridor":
                    print ("You went into the corrisor only to be flanked by guards from all sides... Only if BOMAR was on offense.")
                    sleep(1)
                    sys.exit(0)
                elif decision_4 == "airshaft":
                    print ("You crawl into the room with the four suits and two rogue scientists, SHARQUISHQWANIQWA and E-DAY-GO.")
                    print ("They agree to take you to the forest to end this corrupt organization.")
                    print(" ")
                    decision_5 = input("They both lead you to the forest and you have to decide between going to the [mountain] to prepare, or rush to the [base] to end their experiments before they begin?: ")
                    if decision_5 == "base":
                        print("They lead you to the base and give you the proper equipment in order to make it through the base unscathed.")
                        print("You and BOMAR then are able to take pictures and steal survealance to expose the organization.")
                        sleep(1)
                        sys.exit(0)
                    elif decision_5 == "mountain":
                        print(" ")
                        decision_6 = input("You find two caves at the base of the mountain, will you go to the [left] or the [right] cave?: ")
                        if decision_6 == "left":
                            if KARMA == 1:
                                print("SHARQUISHQWANIQWA is trailing along, when you hear a scream. You turn around only to find... Sorry, I can't say what occured, it simply isn't made for people with a soul to reatin their sanity anymore. Yet, you tread on.")
                                print("E-DAY-GO leads you to the base and give you the proper equipment in order to make it through the base unscathed.")
                                print("You and BOMAR then are able to take pictures and steal survealance to expose the organization.")
                                sleep(1)
                                sys.exit(0)
                            elif KARMA == 2:
                                print("E-DAY-GO is trailing along, when you hear a scream. You turn around only to find... Sorry, I can't say what occured, it simply isn't made for people with a soul to reatin their sanity anymore. Yet, you tread on.")
                                print("E-DAY-GO leads you to the base and give you the proper equipment in order to make it through the base unscathed.")
                                print("You and BOMAR then are able to take pictures and steal survealance to expose the organization.")
                                sleep(1)
                                sys.exit(0)
                        elif decision_6 == "right":
                            print(" ")
                            decision_7 = input("Find a cavern that looks as if it is ready to crumble with four items: Tablet of layout of secret base and history of Forest [1], suits that entirely camouflage you [2], a control panel of everything with electricity around a mile radius [3], or a device that controls microbots that infect and control its victims [4].")
                            if int(decision_7) == 1:
                                print ("Using the tablet, SHARQUISHQWANIQWA and E-DAY-GO helped you expose the Organization, save the forest, and all of you disguised it so no one will ever try to harm it again.")
                                sleep(1)
                            elif int(decision_7) == 2:
                                print ("Using the suits, you overrode the base, locked everyone in, and caused them to expose themselves to everyone as to all of their secrets while stealing all of their info unanimously. Your hometown was grateful for the heros, but they didn't have any evidence to who to bestow the honor to. This led to you, BOMAR, and your two new friends normal lives to live for the rest of their days.")
                                sleep(1)
                            elif int(decision_7) == 3:
                                print ("You used the control panel to destroy all of The Organization's data, thus making all of their data useless and ruining any attempt of destroying The Forest. THE END.")
                                sleep(1)
                            elif int(decision_7) == 4:
                                print ("Using the microbots, you made all of the scientists fall asleep, take over base, shut it all down. Then, you erased all data and progress, cuts all ties for progression, and you left the base to rot in its own misery.")
                                sleep(1)
                            else:
                                print ("Try again with one of the provided options.")
                        else:
                            print("Try again with one of the provided options.")
                    else:
                        print("Try again with one of the provided options.")
                else:
                    print("Try again with one of the provided options.")
            else:
                print("Try again with one of the provided options.")
        else:
            print("Try again with one of the provided options.")
        sys.exit(0)
    except TypeError:
        print("Idk man")
        sleep(1)
        sys.exit(0)


story_mode()
