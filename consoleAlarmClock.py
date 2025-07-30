import pygame
import datetime
import time
def set_alarm(alarm_time):
    sound="assets/Circuit Rush - The Mini Vandals.mp3"
    print(f'Alarm set for {alarm_time}')
    while True:
        present = datetime.datetime.now().strftime("%H:%M:%S")
        print(present)
        if present==alarm_time:
            print('TIME\'S UP!!!')
            pygame.init()
            pygame.mixer.music.load(sound)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            break
        time.sleep(1)
if __name__=='__main__':
    alarm_time = input("Enter alarm time: (HH:MM:SS) ")
    set_alarm(alarm_time)
