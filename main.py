#Sarah Kam, no collaborators
#CSC 111 Final Project: The Keyboard
#Allows user to 'play' piano by pressing letters on their computer keyboard which are associated with actual piano notes

from graphics import *
from piano import *
from time import sleep

#create the piano outside of function definitions so that you can call it within other functions
win = GraphWin("Piano", WIDTH, HEIGHT)

keys = [Key('Clow'), Key('Csharp'), Key('D'), Key('Eflat') , Key('E'), Key('F'), Key('Fsharp'), Key('G'), Key('Gsharp'), Key('A'), Key('Bflat'), Key('B'), Key('Chigh')]
#creates all the key objects at once and puts em in a list
for key in keys:
  key.body.draw(win)
  key.label.draw(win)

def user_player():
  '''Allows user-controlled playing with the computer keyboard'''

  print('''\nINSTRUCTIONS:
  Click on the window to start. To play, press a letter labeled on the piano on your computer keyboard. This letter  corresponds with a piano note (so 's' will play a C natural, 'e' plays a C-sharp, and so on).
  Press 'q' to quit.''')

  while True:
    keypress = win.checkKey().lower()
    #plays a note depending on what computer key the user presses
    if keypress == 's': #Clow
      keys[0].play(win)
    elif keypress == 'e': #Csharp
      keys[1].play(win)
    elif keypress == 'd': #D
      keys[2].play(win)
    elif keypress == 'r': #Eflat
      keys[3].play(win)
    elif keypress == 'f': #E
      keys[4].play(win)
    elif keypress == 'g': #F
      keys[5].play(win)
    elif keypress == 'y': #Fsharp
      keys[6].play(win)
    elif keypress == 'h': #G
      keys[7].play(win)
    elif keypress == 'u': #Gsharp
      keys[8].play(win)
    elif keypress == 'j': #A
      keys[9].play(win)
    elif keypress == 'i': #Bflat
      keys[10].play(win)
    elif keypress == 'k': #B
      keys[11].play(win)
    elif keypress == 'l': #Chigh
      keys[12].play(win)
    elif keypress == 'q':
      print('\nQuitting...')
      break

def prewritten_player():
  '''Allows user to play songs that already exist in the songs.txt file'''

  songs = open('songs.txt').readlines()
  #gives a list of songs, since each song in song.txt is a single line

  song_choice = input("\nWhat song would you like to play? Enter:\n'1' for Mary Had a Little Lamb \n'2' for Old MacDonald \n'3' for Twinkle Twinkle Little Star \n'4' for In the Hall of the Mountain King \n'5' for a surprise: ")
  while song_choice not in ['1', '2', '3', '4', '5']:
    song_choice = input("\nPlease input 1, 2, 3, 4, or 5: ") #protect against invalid inputs

  user_song = songs[int(song_choice) - 1].split() #takes the song that user has chosen and splits it into its letters

  for letter in user_song:
    #iterates over the letters coded into the song's text file, which was split by spaces
    if letter == 's': #Clow
      keys[0].play(win)
    elif letter == 'e': #Csharp
      keys[1].play(win)
    elif letter == 'd': #D
      keys[2].play(win)
    elif letter == 'r': #Eflat
      keys[3].play(win)
    elif letter == 'f': #E
      keys[4].play(win)
    elif letter == 'g': #F
      keys[5].play(win)
    elif letter == 'y': #Fsharp
      keys[6].play(win)
    elif letter == 'h': #G
      keys[7].play(win)
    elif letter == 'u': #Gsharp
      keys[8].play(win)
    elif letter == 'j': #A
      keys[9].play(win)
    elif letter == 'i': #Bflat
      keys[10].play(win)
    elif letter == 'k': #B
      keys[11].play(win)
    elif letter == 'l': #Chigh
      keys[12].play(win)
    elif letter in 'p/': #pause song
      sleep(DURATION)
    sleep(0.1) #gives a little break after each note


def main():
  '''Allows users to decide whether they want to play the piano themselves or have the computer play a song for them'''

  choice = input("Do you want to play the piano yourself or play some prewritten songs? Enter Y for yourself and P for prewritten: ").upper()

  while choice not in ['Y', 'P']: #protection against an invalid user input
    choice = input("\nEnter Y to play the piano yourself or P to play prewritten songs: ").upper()

  if choice == 'Y':
    user_player()
  elif choice == 'P':
    user_continue = ''
    while user_continue != 'q':
      prewritten_player()
      user_continue = input("\nEnter 'q' to quit, or enter any other key to listen to another song: ").lower()
    #loops over prewritten_player and plays one song until user is done
  

if __name__ == '__main__':
  main() #calls main module
