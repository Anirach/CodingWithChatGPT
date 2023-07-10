def encode_morse(text):
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                  'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
                  'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
                  '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': ' '}
    
    encoded_text = ''
    for char in text:
        char = char.upper()
        if char in morse_code:
            encoded_text += morse_code[char] + ' '
    
    return encoded_text.strip()

# Example usage
print(encode_morse("EDABBIT CHALLENGE"))  # Output: ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."
print(encode_morse("HELP ME ! A"))          # Output: ".... . .-.. .--.   -- .   -.-.--"
