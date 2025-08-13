'''
Let's say we have a home theater system with several components like a DVDPlayer, Projector, Lights, and Screen. 
Each component has its own methods to turn on, turn off, etc. Instead of the client interacting with each of these
components directly, we use a Facade to simplify the process.
'''
#Subsystem classes
class DVDPlayer:
    def on(self):
        print("DVD Player is On")
    def play(self,movie):
        print(f"Playing {movie}")
    def off(self): 
        print("DVD Player is Off")
        
class Projector:
    def on(self):
        print("Projector is On")
    def off(self):
        print("Projector is Off")

class Lights:
    def dim(self):
        print("Lights are dimmed")

class Screen:
    def down(self):
        print("Screen is down")
    def up(self):
        print("Screen is up")

#Facade class
class HomeTheaterFacade:
    def __init__(self,dvd_player,projector, lights,screen):
        self.dvd_player = dvd_player
        self.projector = projector
        self.lights = lights
        self.screen = screen
    def watch_movie(self,movie):
        print("Get ready to watch the movie...")
        self.lights.dim()
        self.screen.down()
        self.projector.on()
        self.dvd_player.on()
        self.dvd_player.play(movie)
    def end_movie(self):
        print("Shutting down the home theater...")
        self.dvd_player.off()
        self.projector.off()
        self.screen.up()
        self.lights.dim()
#Client Code
# Client code
dvd_player = DVDPlayer()
projector = Projector()
lights = Lights()
screen = Screen()
home_theater = HomeTheaterFacade(dvd_player, projector, lights, screen)
# Using the facade to watch a movie
home_theater.watch_movie("The Matrix")
print("---- End of Movie ----")
home_theater.end_movie()
'''
Output:
Get ready to watch the movie...
Lights are dimmed
Screen is down
Projector is On
DVD Player is On
Playing The Matrix
---- End of Movie ----
Shutting down the home theater...
DVD Player is Off
Projector is Off
Screen is up
Lights are dimmed
'''