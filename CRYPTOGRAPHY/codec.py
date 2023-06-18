from collections import Counter, namedtuple



class  Codec:
    def __init__(self, delimiter='#'):
        self.delimiter = delimiter

    def encode(self, text):
        binary_message = text + self.delimiter
        binary = ' '.join(format(ord(c), '08b') for c in binary_message)
        return binary.replace(' ', '')

    def decode(self, data):
         # split by 8-bits
        all_bytes = [ data[i: i+8] for i in range(0, len(data), 8) ]
        # convert from bits to characters
        decoded_data = ""
        for byte in all_bytes:
            if(chr(int(byte, 2)) == "#"):
                break
            decoded_data += chr(int(byte, 2))
        return decoded_data

        # binary = data.replace(self.delimiter, ' ')
        # text = ''.join([chr(int(b, 2)) for b in binary.split()])
        # return text.replace(self.delimiter, '')


class CaesarCypher(Codec):
    def __init__(self, delimiter='#', shift=3):
        super().__init__(delimiter=delimiter)
        self.shift = shift

    def encode(self, text):
        shifted_text = ''.join([chr((ord(c) + self.shift) % 256) for c in text])
        return super().encode(shifted_text)

    def decode(self, data):
        shifted_text = super().decode(data)
        text = ''.join([chr((ord(c) - self.shift) % 256) for c in shifted_text])
        return text.replace(self.delimiter, '')

# a helper class used for class HuffmanCodes that implements a Huffman tree
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.left = left
        self.right = right
        self.freq = freq
        self.symbol = symbol
        self.code = ''
        

class HuffmanCodes(Codec):
    
    def __init__(self,delimiter='#'):
        self.nodes = None
        super().__init__(delimiter=delimiter)
        self.name = 'huffman'
    
    # make a Huffman Tree    
    def make_tree(self, data):
        # make nodes
        nodes = []
        for char, freq in data.items():
            nodes.append(Node(freq, char))
            
        # assemble the nodes into a tree
        while len(nodes) > 1:
            # sort the current nodes by frequency
            nodes = sorted(nodes, key=lambda x: x.freq)
            # pick two nodes with the lowest frequencies
            left = nodes[0]
            right = nodes[1]
            # assign codes
            left.code = '0'
            right.code = '1'
            # combine the nodes into a tree
            root = Node(left.freq+right.freq, left.symbol+right.symbol,
                        left, right)
            # remove the two nodes and add their parent to the list of nodes
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(root)
        return nodes[0]  # return the root of the tree
    
    # traverse a Huffman tree and assign codes to symbols
    def traverse_tree(self, node, code_dict, current_code=''):
        next_code = current_code + node.code
        if node.left:
            self.traverse_tree(node.left, code_dict, next_code)
        if node.right:
            self.traverse_tree(node.right, code_dict, next_code)
        if not node.left and not node.right:
            code_dict[node.symbol] = next_code
    
    # convert text into binary form
    def encode(self, text):
        # calculate frequency of each character
        freq_dict = {}
        for char in text:
            if char not in freq_dict:
                freq_dict[char] = 1
            else:
                freq_dict[char] += 1
        # make a Huffman tree
        root = self.make_tree(freq_dict)
        # traverse the Huffman tree and assign codes to symbols
        code_dict = {}
        self.traverse_tree(root, code_dict)
        # encode the text using the codes
        binary_data = ''
        for char in text:
            binary_data += code_dict[char]
        return binary_data
    
    # convert binary data into text
    def decode(self, data):
        # make a Huffman tree
        freq_dict = {}
        for char in data:
            if char not in freq_dict:
                freq_dict[char] = 1
            else:
                freq_dict[char] += 1
        root = self.make_tree(freq_dict)
        # traverse the Huffman tree and assign codes to symbols
        code_dict = {}
        self.traverse_tree(root, code_dict)
        # decode the binary data using the codes
        current_code = ''
        text = ''
        for bit in data:
            current_code += bit
            for symbol, code in code_dict.items():
                if code == current_code:
                    text += symbol
                    current_code = ''
                    break
        return text



if __name__ == '__main__':
    text = 'hello' 
    #text = 'Casino Royale 10:30 Order martini' 
    print('Original:', text)
    
    c = Codec()
    binary = c.encode(text)
    # NOTE: binary should have a delimiter and text should not have a delimiter
    print('Binary:', binary) # should print '011010000110010101101100011011000110111100100011'
    data = c.decode(binary)  
    print('Text:', data)     # should print 'hello'
    
    cc = CaesarCypher()
    binary = cc.encode(text)
    # NOTE: binary should have a delimiter and text should not have a delimiter
    print('Binary:', binary)
    data = cc.decode(binary) 
    print('Text:', data)     # should print 'hello'
     
    h = HuffmanCodes()
    binary = h.encode(text + h.delimiter)
    # NOTE: binary should have a delimiter and text should not have a delimiter
    print('Binary:', binary)
    data = h.decode(binary)
    print('Text:', data)     # should print 'hello'

    