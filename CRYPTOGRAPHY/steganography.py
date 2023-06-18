import cv2
from codec import Codec, CaesarCypher, HuffmanCodes

class Steganography:
    def __init__(self):
        self.binary = None
        self.text = None
    
    def print(self):
        if self.binary is not None and self.text is not None:
            print("Encoded message (text):", self.text)
            print("Encoded message (binary):", self.binary)
            print("Decoded message (text):", self.decode(self.binary))
            print("Decoded message (binary):", self.decode(self.binary, binary_output=True))
        else:
            print("No message has been encoded or decoded yet.")
    
    def show(self, filein):
        img = cv2.imread(filein)
        cv2.imshow('Image',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def encode(self, filein, fileout, message, codec):
        img = cv2.imread(filein)
        rows, cols, channels = img.shape
        data = img.flatten()

        self.text = message

        if codec == 'binary':
            # Add delimiter to binary message
            binary_codec = Codec()
            self.binary = binary_codec.encode(message)
        elif codec == 'caesar':
            caesar_codec = CaesarCypher()
            self.binary = caesar_codec.encode(message)
        elif codec == 'huffman':
            huffman_codec = HuffmanCodes()
            huffman_codec.encode(message)
            self.binary = huffman_codec.encoded_message
        else:
            print("Invalid codec name. Use 'binary', 'caesar', or 'huffman'.")
            return
    
        if len(self.binary) > len(data):
            print("Message is too long to be encoded in the image.")
            return
    
        for i in range(len(self.binary)):
            data[i] = (data[i] & ~1) | int(self.binary[i])
    
        data = data.reshape(rows, cols, channels)
        cv2.imwrite(fileout, data)
    
    def decode(self, filein, codec='binary'):
        img = cv2.imread(filein)
        data = img.flatten()
        binary_message = ''
        
        for i in range(len(data)):
            binary_message += str(data[i] & 1)
            if binary_message.endswith('\0'):
                break
        
        if codec == 'binary':
            binary_codec = Codec()
            return binary_codec.decode(binary_message[:-1])
        elif codec == 'caesar':
            caesar_codec = CaesarCypher()
            return caesar_codec.decode(binary_message[:-1])
        elif codec == 'huffman':
            huffman_codec = HuffmanCodes()
            huffman_codec.decode(binary_message[:-1])
            return huffman_codec.decoded_data
        else:
            print("Invalid codec name. Use 'binary', 'caesar', or 'huffman'.")
            return


if __name__ == '__main__':
    
    s = Steganography()

    s.encode('/Users/anshuljagtap/Desktop/cse 30/Programming Assignments/PA-3/fractal.jpg', '/Users/anshuljagtap/Desktop/cse 30/Programming Assignments/PA-3/fractal.png', 'hello', 'binary')
    # NOTE: binary should have a delimiter and text should not have a delimiter
    assert s.text == 'hello'
    assert s.binary == '011010000110010101101100011011000110111100100011'

    s.decode('/Users/anshuljagtap/Desktop/cse 30/Programming Assignments/PA-3/fractal.png', 'binary')
    # NOTE: binary should have a delimiter and text should not have a delimiter
    assert s.text == 'hello'
    assert s.binary == '011010000110010101101100011011000110111100100011'

    print('Everything works!!!')