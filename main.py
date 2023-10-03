{
  "version": 1,
  "author": "Anonymous maker",
  "editor": "wokwi",
  "parts": [
    { "type": "wokwi-arduino-uno", "id": "uno", "top": -106.3, "left": -38.56, "attrs": {} },
    {
      "type": "wokwi-lcd2004",
      "id": "lcd1",
      "top": 307.35,
      "left": 10.02,
      "attrs": { "pins": "i2c" }
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn1",
      "top": -323.42,
      "left": -55.53,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    { "type": "wokwi-hc-sr04", "id": "ultrasonic1", "top": -452.71, "left": 248.41, "attrs": {} }
  ],
  "connections": [
    [ "btn1:2.l", "uno:GND.1", "green", [ "h0" ] ],
    [ "btn1:2.r", "uno:4", "green", [ "v0" ] ],
    [ "ultrasonic1:VCC", "uno:5V", "red", [ "v0" ] ],
    [ "ultrasonic1:ECHO", "uno:2", "green", [ "v0" ] ],
    [ "ultrasonic1:TRIG", "uno:3", "green", [ "v0" ] ],
    [ "ultrasonic1:GND", "uno:GND.2", "black", [ "v0" ] ],
    [ "lcd1:GND", "uno:GND.3", "black", [ "h0" ] ],
    [ "lcd1:VCC", "uno:5V", "red", [ "h0" ] ],
    [ "lcd1:SDA", "uno:8", "green", [ "h0" ] ],
    [ "lcd1:SCL", "uno:9", "green", [ "h0" ] ]
  ],
  "dependencies": {}
}