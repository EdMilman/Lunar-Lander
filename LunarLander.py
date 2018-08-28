"""
Edward Milman - emilma01@dcs.bbk.ac.uk
PoP Assignment One:
A "Lunar Lander" game based on the specification in the readme file. Players enter fuel usage when prompted to try and
land at a velocity of less than 10 per second. At the end of the game, players can choose to play again
"""
import os


def main():
    # base values
    start_altitude = 1000.0
    start_velocity = 100.0
    start_fuel = 1000.0
    start_time = 1
    difficulty = 0.15
    play = True
    # play loop
    while play:
        intro()
        os.system("pause")
        os.system('cls')
        # assign base values to variables used in game loop
        altitude = start_altitude
        fuel = start_fuel
        game_time = start_time
        velocity = start_velocity
        turn_summary(altitude, velocity, fuel, game_time)
        # game loop - loops until altitude <= 0 i.e landing
        while altitude > 0.0:
                # change game variables based on user input and return status
                to_burn = burn_fuel(fuel)
                os.system('cls')
                fuel -= to_burn
                velocity = change_velocity(velocity, difficulty, to_burn)
                altitude = change_altitude(velocity, altitude)
                game_time += 1
                # display 'flying' summary if still landing
                if altitude > 0:
                    turn_summary(altitude, velocity, fuel, game_time)
                    if fuel == 0:
                        print("Oh dear, you ran out of fuel. Please put on your seatbelt.")
        # end game summary / play again
        check_landing(velocity, altitude, fuel, game_time)
        play = play_again()
        os.system('cls')


# prompts user to enter fuel and returns value adjusted so 0 <= value <= current fuel
def burn_fuel(fuel, to_burn=0):
    while True:
        try:
            to_burn = int(input("Please choose how much fuel to burn: "))
        except ValueError:
            print("Please enter a whole number to choose the amount of fuel to burn.")
        else:
            if to_burn > fuel:
                to_burn = fuel
            if to_burn < 0:
                to_burn = 0
            return to_burn


# returns new velocity calculated from fuel usage and difficulty
def change_velocity(velocity, diff, burn):
    # velocity** *increases* by 1.6 metres/second, due to the acceleration of gravity
    # **velocity** *decreases* by an amount proportional to the amount of fuel you just burned
    velocity += 1.6 - (burn * diff)
    # rounded to 2 s.f. to avoid imprecision making printing 'ugly'
    return round(velocity, 2)


# returns new altitude calculated from velocity
def change_altitude(velocity, altitude):
    # Your **altitude** *decreases* by your velocity multiplied by the amount of "time" each turn takes. time = 1
    new_altitude = altitude - velocity
    return round(new_altitude, 2)


# checks altitude greater than 0, raises error if not, calls success or fail landing functions based on velocity
def check_landing(velocity, altitude, fuel, game_time):
    if altitude > 0:
        raise ValueError("Error: Impossible to land if altitude < 0")
    # A safe landing occurs if your speed is under 10 meters/second.
    if velocity < 10.0:
        land_success(fuel, game_time)
    else:
        land_fail(velocity, fuel, game_time)


# give information to player about the game
def intro():
    print("You are coming into land on this mysterious looking planet. "
          "\nYou will accelerate towards the planet at 1.6 metres per second unless you take action and burn fuel."
          "\nBurning fuel will slow your descent, just make sure you are travelling less than 10m per second"
          "\nwhen you land - your no claims bonus on your space insurance depends on it!"
          "\nGet to it then!\n")


# provides status of current variables so player can see the state of play
def turn_summary(alt, velo, fuel, game_time):
    print("Your current altitude is {} metres above the surface.".format(alt))
    if velo < 0:
        direction = "away from"
    else:
        direction = "towards"
    print("Your current velocity is {} metres per second. You are moving {} the surface".format(velo, direction))
    print("You have {} units of fuel remaining.".format(fuel))
    print("You have been on the mission for {} seconds.\n".format(game_time))


# returns true or false after prompting the player for input regarding playing again
def play_again():
    answer = False
    while True:
        try:
            response = input("Would you like to play again? (Y/N) ")
            if response.lower()[0] != "y" and response.lower()[0] != "n":
                raise ValueError
        except ValueError:
            print("Please input Y or N")
        else:
            if response.lower()[0] == "y":
                answer = True
            return answer


# prints statement in event of a successful landing
def land_success(fuel, game_time):
    print("After {} suspense filled seconds you have successfully landed on the surface!\n"
          "Congratulations - you didn't kill everyone horribly, they seem surprised!\n"
          "You have {} fuel remaining...is that enough to get home?\n".format(game_time, fuel))


# prints statement in even of failed landing
def land_fail(velocity, fuel, game_time):
    if fuel > 0:
        burning = "The remaining {} units of fuel makes a beautiful fire, almost visible from Earth!".format(fuel)
    else:
        burning = "Running out of fuel, meant nothing was left for an awesome explosion, what an anticlimax!"
    print("You tried to land too quickly! \n"
          "You hit the ground at {} metres per second, creating a scenic crater.\n"
          "{}\n"
          "It took you just {} seconds to mess things up this badly.\n"
          "Just before your ship smashes into the ground and vapourises,\n"
          "your crew mates curse the day they let you fly - you don't even have a license!\n".format(velocity, burning, game_time))


if __name__ == "__main__":
    main()
