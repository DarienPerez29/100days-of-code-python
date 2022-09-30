print(r'''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/

 ======================================================================
 ||||||||||||||||||||| WELCOME TO TREASURE ISLAND |||||||||||||||||||||
 ======================================================================
 |     Your mission is to take decisions to find the right path       |
 |    to discover the treasure. If you take the wrong decision...     |
 |                      >>>> YOU MIGHT DIE <<<<                       |
 |                                                                    |
 |                       Best of luck, pirate                         |
 ----------------------------------------------------------------------''')
# ASCII art from: https://ascii.co.uk/art/treasuremap

print(".\n.\n.\n.\nYou arrive at the treasure island... that island that you've been searching")
print("for years. Immediately, you jump ashore and the final search for the treasure")
print("begins. You have a map of the treasure island, but the path is not clear")
print("because the paper is very damaged, so you try your luck.")

print("\nYou spend some time walking, searching for any signal of the treasure. Then")
print("you meet a fork: you have to take one of the two paths ahead.")

print("\n■ Which path would you choose? (type left or right)")
q1 = input("> ").lower()

if q1 == "left":
    print("\nHaving choosing the left path, you start to see some swords, bones and hats")
    print("of pirates. You start wonder why they have died, but that doesn't stop your search.")

    print("\nYou reach a dead end, but there are also two levers, one made of wood, and the")
    print("other one, made of stone.")

    print("\n■ Which lever would you pull down? (type wood or stone)")
    q2 = input("> ").lower()

    if q2 == "stone":
        print("\nThe wall in front of you rises, and you see an old, enormous ship in the distance.")
        print("You believe that you have finally made it! You found the treasure!, but when you get into")
        print("the ship, you find 3 chest, and a note that says:")

        print(r'''
         ---------------------------------_
        | The right chest you must choose  \
        | if your objective is to not lose.|
        / One of them has the big prize    |
       |  while the rest can't be defused. |
        ----------^~^^---------~-----^-----''')

        print("\n■ Which lever would you pull down? (type 1, 2 or 3)")
        q3 = input("> ").lower()

        if q3 == "3":
            print(r'''
            =================================
            |||||||||  YOU WIN !!!  |||||||||
            =================================
                             _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
            ''')
            # ASCII art from: https://ascii.co.uk/art/treasure
        else:
            print("\nThe chest made you blow up...")
            print("\n>>>>> GAME OVER <<<<<")

    else:
        print("\nA venomous gas fills the air and you die...")
        print("\n>>>>> GAME OVER <<<<<")
else:
    print("\nYou've fallen into a trap with spikes...")
    print("\n>>>>> GAME OVER <<<<<")
