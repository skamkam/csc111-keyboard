from graphics import *
from replit import audio
from time import sleep

OUTLINE = 'gray'
LINEWIDTH = 5
WIDTH = 800
HEIGHT = 450
DURATION = 0.35

class Key:
  def __init__(self, key):
    '''Sets up the body polygon and letter label of each key and the frequency that goes with that key; also the colors per key'''

    #key specific attributes: body shape, label, frequency
    if key == 'Clow':
      self.freq = 262
      p1 = Point(0, HEIGHT)
      p2 = Point(0, 0)
      p3 = Point(65, 0)
      p4 = Point(65, HEIGHT//2)
      p5 = Point(100, HEIGHT//2)
      p6 = Point(100, HEIGHT)
      self.body = Polygon(p1, p2, p3, p4, p5, p6)
      self.label = Text(Point(50, 3*HEIGHT//4), 's')

    elif key == 'Csharp':
      self.freq = 278
      p1 = Point(65, 0)
      p2 = Point(135, HEIGHT//2)
      self.body = Rectangle(p1, p2)
      self.label = Text(Point(100, HEIGHT//4), 'e')

    elif key == 'D':
      self.freq = 294
      p1 = Point(135, 0)
      p2 = Point(165, 0)
      p3 = Point(165, HEIGHT//2)
      p4 = Point(200, HEIGHT//2)
      p5 = Point(200, HEIGHT)
      p6 = Point(100, HEIGHT)
      p7 = Point(100, HEIGHT//2)
      p8 = Point(135, HEIGHT//2)
      self.body = Polygon(p1, p2, p3, p4, p5, p6, p7, p8)
      self.label = Text(Point(150, 3*HEIGHT//4), 'd')

    elif key == 'Eflat':
      self.freq = 312
      p1 = Point(165, 0)
      p2 = Point(235, HEIGHT//2)
      self.body = Rectangle(p1, p2)
      self.label = Text(Point(200, HEIGHT//4), 'r')

    elif key == 'E':
      self.freq = 330
      p1 = Point(235, 0)
      p2 = Point(300, 0)
      p3 = Point(300, HEIGHT)
      p4 = Point(200, HEIGHT)
      p5 = Point(200, HEIGHT//2)
      p6 = Point(235, HEIGHT//2)
      self.body = Polygon(p1, p2, p3, p4, p5, p6)
      self.label = Text(Point(250, 3*HEIGHT//4), 'f')

    elif key == 'F':
      self.freq = 350
      p1 = Point(300, 0)
      p2 = Point(365, 0)
      p3 = Point(365, HEIGHT//2)
      p4 = Point(400, HEIGHT//2)
      p5 = Point(400, HEIGHT)
      p6 = Point(300, HEIGHT)
      self.body = Polygon(p1, p2, p3, p4, p5, p6)
      self.label = Text(Point(350, 3*HEIGHT//4), 'g')

    elif key == 'Fsharp':
      self.freq = 371
      p1 = Point(365, 0)
      p2 = Point(435, HEIGHT//2)
      self.body = Rectangle(p1, p2)
      self.label = Text(Point(400, HEIGHT//4), 'y')

    elif key == 'G':
      self.freq = 393
      p1 = Point(435, 0)
      p2 = Point(465, 0)
      p3 = Point(465, HEIGHT//2)
      p4 = Point(500, HEIGHT//2)
      p5 = Point(500, HEIGHT)
      p6 = Point(400, HEIGHT)
      p7 = Point(400, HEIGHT//2)
      p8 = Point(435, HEIGHT//2)
      self.body = Polygon(p1, p2, p3, p4, p5, p6, p7, p8)
      self.label = Text(Point(450, 3*HEIGHT//4), 'h')

    elif key == 'Gsharp':
      self.freq = 416
      p1 = Point(465, 0)
      p2 = Point(535, HEIGHT//2)
      self.body = Rectangle(p1, p2)
      self.label = Text(Point(500, HEIGHT//4), 'u')

    elif key == 'A':
      self.freq = 441
      p1 = Point(535, 0)
      p2 = Point(565, 0)
      p3 = Point(565, HEIGHT//2)
      p4 = Point(600, HEIGHT//2)
      p5 = Point(600, HEIGHT)
      p6 = Point(500, HEIGHT)
      p7 = Point(500, HEIGHT//2)
      p8 = Point(535, HEIGHT//2)
      self.body = Polygon(p1, p2, p3, p4, p5, p6, p7, p8)
      self.label = Text(Point(550, 3*HEIGHT//4), 'j')

    elif key == 'Bflat':
      self.freq = 467
      p1 = Point(565, 0)
      p2 = Point(635, HEIGHT//2)
      self.body = Rectangle(p1, p2)
      self.label = Text(Point(600, HEIGHT//4), 'i')

    elif key == 'B':
      self.freq = 495
      p1 = Point(635, 0)
      p2 = Point(700, 0)
      p3 = Point(700, HEIGHT)
      p4 = Point(600, HEIGHT)
      p5 = Point(600, HEIGHT//2)
      p6 = Point(635, HEIGHT//2)
      self.body = Polygon(p1, p2, p3, p4, p5, p6)
      self.label = Text(Point(650, 3*HEIGHT//4), 'k')

    elif key == 'Chigh':
      self.freq = 525
      p1 = Point(700, 0)
      p2 = Point(765, 0)
      p3 = Point(765, HEIGHT//2)
      p4 = Point(800, HEIGHT//2)
      p5 = Point(800, HEIGHT)
      p6 = Point(700, HEIGHT)
      self.body = Polygon(p1, p2, p3, p4, p5, p6)
      self.label = Text(Point(750, 3*HEIGHT//4), 'l')

    #general attributes of each key
    if ('sharp' in key) or ('flat' in key):
      self.color = 'black'
      self.label.setTextColor('white')
    else:
      self.color = 'white'

    self.label.setSize(30)
    self.body.setFill(self.color)
    self.body.setOutline(OUTLINE)
    self.body.setWidth(LINEWIDTH)


  def play(self, win):
    '''All the actions associated with pressing a key: playing a sound and lighting up'''
    
    #changes color to green temporarily
    self.body.undraw()
    self.label.undraw()
    self.body.setFill('green')
    self.body.draw(win)

    #each note is 0.35 seconds: key lights up and tone plays
    audio.play_tone(DURATION, self.freq, 0)
    sleep(DURATION)

    #once the note is done playing, the key changes back to its original color
    self.body.undraw()
    self.body.setFill(self.color)
    self.body.draw(win)
    self.label.draw(win)