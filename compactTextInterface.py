#---Imports---#
from os import name
from os import system
from time import sleep
#---       ---#

#---Functions---#
def clear():
    system('cls' if name == 'nt' else 'clear')
#---         ---#

#---Read---#
from itertools import zip_longest

def singleCodeToText(input):
    match input:
        case "11111":
            return 'a'
        case "11110":
            return 'b'
        case "11101":
            return 'c'
        case "11011":
            return 'd'
        case "10111":
            return 'e'
        case "01111":
            return 'f'
        case "11100":
            return 'g'
        case "11010":
            return 'h'
        case "11001":
            return 'i'
        case "10110":
            return 'j'
        case "10101":
            return 'k'
        case "10011":
            return 'l'
        case "01110":
            return 'm'
        case "01101":
            return 'n'
        case "01011":
            return 'o'
        case "00111":
            return 'p'
        case "11000":
            return 'q'
        case "10100":
            return 'r'
        case "10010":
            return 's'
        case "10001":
            return 't'
        case "01100":
            return 'u'
        case "01010":
            return 'v'
        case "01001":
            return 'w'
        case "00110":
            return 'x'
        case "00101":
            return 'y'
        case "00011":
            return 'z'
        case "10000":
            return ')'
        case "01000":
            return '.'
        case "00100":
            return ','
        case "00010":
            return '/'
        case "00001":
            return '('
        case "00000":
            return ' '

def multiCodeToText(inputList):
    output = []
    for x in range(len(inputList)):
        output.append(singleCodeToText(inputList[x]))
    return output

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return list(zip_longest(*args, fillvalue=fillvalue))

def readBin(filePath):
    # Open the binary file in "rb" mode
    with open(filePath, 'rb') as f:
        # Read the contents of the file into a bytes object
        data = f.read()
    f.close()

    # Convert the bytes object to a hexadecimal string
    hex_str = hex(int.from_bytes(data, 'big'))

    # Convert the hexadecimal string to a binary string
    bin_str = format(int(hex_str, 16), 'b')

    bin_str = bin_str.zfill(len(data) * 8)

    return bin_str

def segmentAssembler(inputList):
    outList = []
    temp = ""
    inputList = list(inputList)
    for x in range(len(inputList)):
        for y in range(len(inputList[x])):
            temp += str(inputList[x][y])
        outList.append(temp)
        temp = ""

    return outList

def Read(filePath, translate=True):
    if translate:
        return "".join(multiCodeToText(segmentAssembler(grouper(readBin(filePath), 5, 0))))
    else:
        return readBin(filePath)
#---    ---#

#---Write---#
from itertools import zip_longest

def translateChar(input):
    match input:
        case "a":
            return [1,1,1,1,1]
        case "b":
            return [1,1,1,1,0]
        case "c":
            return [1,1,1,0,1]
        case "d":
            return [1,1,0,1,1]
        case "e":
            return [1,0,1,1,1]
        case "f":
            return [0,1,1,1,1]
        case "g":
            return [1,1,1,0,0]
        case "h":
            return [1,1,0,1,0]
        case "i":
            return [1,1,0,0,1]
        case "j":
            return [1,0,1,1,0]
        case "k":
            return [1,0,1,0,1]
        case "l":
            return [1,0,0,1,1]
        case "m":
            return [0,1,1,1,0]
        case "n":
            return [0,1,1,0,1]
        case "o":
            return [0,1,0,1,1]
        case "p":
            return [0,0,1,1,1]
        case "q":
            return [1,1,0,0,0]
        case "r":
            return [1,0,1,0,0]
        case "s":
            return [1,0,0,1,0]
        case "t":
            return [1,0,0,0,1]
        case "u":
            return [0,1,1,0,0]
        case "v":
            return [0,1,0,1,0]
        case "w":
            return [0,1,0,0,1]
        case "x":
            return [0,0,1,1,0]
        case "y":
            return [0,0,1,0,1]
        case "z":
            return [0,0,0,1,1]
        case ")":
            return [1,0,0,0,0]
        case "(":
            return [0,1,0,0,0]
        case "/":
            return [0,0,1,0,0]
        case ".":
            return [0,0,0,1,0]
        case ",":
            return [0,0,0,0,1]
        case " ":
            return [0,0,0,0,0]
        case _:
            return '�'

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

def textToIntArray(input):
    output = []
    
    for char in input:
        output += translateChar(char)
    
    return list(grouper(output, 8, 0))
        

def writeByteArray(bytes, file):
    byte_value = []
    for x in range(len(bytes)):
        # convert the list of bits into an integer
        byte_value.append(int("".join([str(bit) for bit in bytes[x]]), 2))
    # write the byte value to the file
    file.write(bytearray(byte_value))

def Write(inputText="example text", filePath="binary_file.bin"):
    binary = textToIntArray(inputText.lower().strip())

    # open the file in binary write mode
    with open(filePath, "wb") as f:
        # write a byte to the file
        writeByteArray(binary, f)
    f.close()

    #print(str(binary).replace("[", "").replace("(", "").replace("]", "").replace(")", "").replace(",", "").replace(" ", ""))
#---     ---#

#---Manager---#
print("Made by Noxfy on 1/7/23\n\nTip: when providing file paths make sure to specify the file and not just the folder (This will cause it to crash)\n\nDescription: a program that allows you to read and write compact text files\n\nCharecter restrictions: a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z, (, ), /, ., and ,\n\n\n")

#ask mode
while True:
    match input("Please choose a mode\n\n\t0) Write to a file\n\n\t1) Read from a file\n").strip():
        case "0":
            mode = True  #write to file
            break
        case "1":
            mode = False #read from file
            break
        case _:
            print("Not an option")
            sleep(1)
            clear()

#get file path
filePath = input("File Path: ").lower().strip()
clear()

if mode:
    #ask mode
    while True:
        match input("Please choose an input text method\n\n\t0) Get from terminal\n\n\t1) Get from file\n").strip():
            case "0":
                inputMethod = True  #get from terminal
                break
            case "1":
                inputMethod = False #get from file
                break
            case _:
                print("Not an option")
                sleep(1)
                clear()

    if inputMethod:
        Write(input("Text: "), filePath)
    else:
        #get file path
        #TODO check that userin only contains text that is viable
        fileFilePath = input("File Path: ").lower().strip()
        clear()
        inputTextFile = open(fileFilePath, "rb")
        with open(filePath, "wb") as f1:
            # write a byte to the file
            f1.write(bytearray(inputTextFile.read()))
        f1.close()
        inputTextFile.close()
else: #read file
    #ask output
    while True:
        match input("Please choose an input text method\n\n\t0) Output to terminal\n\n\t1) Output to file\n").strip():
            case "0":
                outMethod = True  #Output to terminal
                break
            case "1":
                outMethod = False #Output to file
                break
            case _:
                print("Not an option")
                sleep(1)
                clear()
    if outMethod:
        print(Read(filePath))
        input()
    else:
        outputFilePath = input("File Path: ").lower().strip()
        clear()

        with open(outputFilePath, "w") as f3:

            f3.write(Read(filePath))
        f3.close()
#---       ---#

