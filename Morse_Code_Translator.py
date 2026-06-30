# Today I'm going to do Challenge 08, which is converting 
# text to Morse Code

# Right here is my list from page 517 of the textbook
# I'm starting with the numbers, letters, then the space

morse_code_list = {
    '0':'-----','1':'.----','2':'..--- ','3':'...--','4':'....-',
    '5':'.....','6':'-....','7':'--...','8':'---..','9':'----.',
    'A': '.-','B': '-...','C': '-.-.','D': '-..','E': '.',
    'F': '..-.','G':'--.','H':'....','I':'..','J':'.---','K':'-.-',
    'L':'.-..','M':'--','N':'-.','O':'---','P':'.--.','Q':'--.-',
    'R':'.-.','S':'...','T':'-','U':'..-','V':'...-',
    'W':'.--','X':'-..-','Y':'-.-','Z':'--..',' ':' \t',
    ',':'--..--','.':'.-.-.-','?':'..--..','!':'-.-.--', '@':'.--.-.',
    '/':'-..-.','(': '-.--.',')':'-.--.-', '&': '.-...', ':':'---...', 
    ';':'-.-.-.','=':'-...-', '+':'.-.-.', '-':'-....-', '_':'..--.-', 
    '"':'.-..-.', '$':'...-..-', '\'':'.----.'
}

# ^ after the letter "Z", for the space, I added two spaces to make
# the morse code more readable since i've gone back and tried to get 
# the spacing right


# here I'm creating the function where all the magic happens
# To be honest I kept trying ways to figure out what to use until
# I remebered .items because we're dealing with pairs in the list here


def alpha_numb_to_morse(alpha_numb):
 
 # Since the mosre code list has capital letter I'm converting
 # whatever the user says to uppercase
 
    morse_code = alpha_numb.upper()
    for dmx, birthday in morse_code_list.items():
        morse_code = morse_code.replace(dmx, birthday)
    return morse_code

# I'm using the .replace to replce some strings in the dictonary 
# dmx = text letter and birthday = morse

        
# Now I'm asking the using the enter a string of text. 
# After user enters, The Morse Code is printed out

def main():
    
    alpha_numb = input("\nEnter text to be converted to morse code: ")
    print_user_morse = alpha_numb_to_morse(alpha_numb)
    print(f"\nMorse Code: " ,(print_user_morse))

# Calling it and executing it!!
main()

# Overall I think the examples in class helped a little bit
# This was [retty interesting