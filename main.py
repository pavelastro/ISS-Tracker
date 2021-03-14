#!/bin/python3

import json
import turtle
import urllib.request
import time 
url= 'http://api.open-notify.org/iss-now.json'
response= urllib.request.urlopen(url)
   
result=json.loads(response.read())
location = result['iss_position']
lat =float(location['latitude'])
lon=float(location['longitude'])

print('latitude:',lat)
print('Longitude',lon)

screen= turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss=turtle.Turtle()
iss.shape('iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon,lat)

lat=22.5726
lon=88.3639
location=turtle.Turtle()
location.penup()
location.color('yellow')
location.goto(lon,lat)
location.dot(5)
location.hideturtle()

url='http://api.open-notify.org/iss-pass.json'
url=url+ '?lat=' + str(lat) + '&lon=' + str(lon)
response=urllib.request.urlopen(url)
result = json.loads(response.read())

over= result['response'][1]['risetime']
print(over)

style=('arial',6,'bold')
location.write(time.ctime(over),font=style)  