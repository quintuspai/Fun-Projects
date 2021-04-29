
class Morse(object):
    """docstring for Morse."""
    morse_code = {'A': '.-',     'B': '-...',   'C': '-.-.', 
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',   '?': '..--..',
        '.': '.-.-.-', ',': '--..--', '0': '-----',
        '1': '.----',  '2': '..---', '3': '...--',
        '4': '....-',  '5': '.....', '6': '-....',  
        '7': '--...',  '8': '---..', '9': '----.', 
        ' ': '/s'
        }
    morse_reversed = {value:key for (key,value) in morse_code.items()}
   
    def encrypt(self, s):
        return ' '.join(self.morse_code.get(char) for char in s)
    
    def decrypt(self, s):
        return ''.join(self.morse_reversed.get(char) for char in s.split())    

morse = Morse()
choice = int(input("1: To convert Text to Morse Code 2: To convert Morse Code to Text 0:Exit"))
while True:
    if choice == 1:
        s = input("Enter text: ").upper()
        print(morse.encrypt(s))
    elif choice == 2:
        code = input("Enter Morse Code: ")
        print(morse.decrypt(code))
    else:
        break
    choice = int(input("1: To convert Text to Morse Code 2: To convert Morse Code to Text 0:Exit"))