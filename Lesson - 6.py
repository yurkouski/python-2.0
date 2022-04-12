# Светофор
from time import sleep
class TrafficLight:
    color = ['Red', 'yellow', 'green']
    def running(self):
        i = 0
        while 3 > i:
            print(f'Цвет светофора: {TrafficLight.color[i]} ')
            if i == 0:
                sleep(7)
            if i == 1:
                sleep(2)
            elif i == 2:
                sleep(3)
            i += 1

a = TrafficLight()
a.running()