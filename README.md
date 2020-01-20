# GeoScentsHack
A Python Program that cheats at GeoScents.net.
================

[GeoScents](http://geoscents.net/) is a game that pits online users against each other in a challenge to guess where a given location is in a certain amount of time. It is a remake of an old game called GeoSense, made by a reddit user, [u/mattfel](https://www.reddit.com/user/mattfel). I heard about this game through a [r/webgames thread](https://www.reddit.com/r/WebGames/comments/ehs0ie/geoscents_an_online_world_geography_game/).

## Dependencies

- pyautogui
- pytesseract
- pynput
- geopy

## Explanation

I decided to use an afternoon to make a program to beat the game for me. There were 3 things needed:

- Reading the place given to players
- Looking up where that place is (latitude/longitude coordinates)
- Moving the mouse to where the place is on the world map

I decided to use [Python-tesseract](https://pypi.org/project/pytesseract/), a wrapper for Google's Tesseract OCR Engine. It can read image files and output the text on the images. To get the image itself, I used something called [PyAutoGUI](https://pypi.org/project/PyAutoGUI/), a library that automates GUI features, to capture a screenshot given coordinates on the screen. To get those coordinates, I needed keyboard input and thus required [pynput](https://pypi.org/project/pynput/), a library that controls input devices. When setting up the program, the user has to give coordinates on the screen of where the text of the location to look up will show up. Thus, we can get an image of the text and passing it into pytesseract, we get the location in string.

To look up where the place is, I used a libary called [geopy](https://pypi.org/project/geopy/). Geopy has [OpenStreetMap's Nominatum](https://wiki.openstreetmap.org/wiki/Nominatim) which allows me to get the latitude and longitude of a place given an address. Thus, all it needed was a simple function to look up the latitude/longitude of a given location. The lookup took less than 1 second in most cases as well.

Finally, to move the mouse to the given latitude and longitude on the GeoScents map, I used PyAutoGUI. However I ran into a problem - the map given wasn't entirely correct (the equator was much lower than the center of the map). Because this was a hack and not something that needed immense precision (and because GeoScents lets you guess the location within a radius), I decided to forego precision for convenience and instead allowed the user to input 2 known locations and extrapolated where the mouse would be given the scaling. I chose the equator and the Cape of Good Hope as the two places needed to be selected. Once the screen coordinates are received, the program automatically finds the conversion from latitude/longitude coordinates to pixels and thus converts the location coordinates to pixel coordinates on screen.
