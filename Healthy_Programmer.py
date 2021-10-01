import pygame
from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while True:
        input_of_user=input()
        if input_of_user==stopper:
            pygame.mixer.music.stop()
            break
def log_now(msg):
    with open("My_Logs.txt","a") as f:
        f.write(f"{msg} :: {datetime.now()}\n")
if __name__=='__main__':
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    water_secs=30*60
    eye_secs=35*60
    phy_secs=40*60
    while True:
        if time()-init_water>water_secs:
            print("It's Time to Drink Water. Enter 'drank' to stop the alarm.")
            musiconloop('Water_Flow.mp3', 'drank')
            init_water=time()
            log_now("Drank Water at :: ")
        if time()-init_eyes>eye_secs:
            print("It's Time for Eye Exercise. Enter 'doneeyes' to stop the alarm.")
            musiconloop('Blue_Eyes.mp3', 'doneeyes')
            init_eyes=time()
            log_now("Eyes Relaxed at :: ")
        if time()-init_exercise>phy_secs:
            print("It's Time for Physical Exercise. Enter 'donephy' to stop the alarm.")
            musiconloop('Exercise.mp3', 'donephy')
            init_eyes=time()
            log_now("Eyes Relaxed at :: ")

        