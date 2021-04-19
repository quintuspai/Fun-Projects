import sys, webbrowser

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    webbrowser.open("https://www.google.com/maps/place/"+address)
else:
    print("Pass address through cmd")
