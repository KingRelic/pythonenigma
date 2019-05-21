import math
#I need this for later usage 
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
#reference index
message_done = "no"
#global variable used in repeating code
need_to_encode = input("Need to encode?: ")

def set_num(g):
    while True:
        g = g - 26
        if g < 26:
            break;
    return g
#fixes math later on in algorithm
def encode(e):
    dial_set1 = int(input("What is dial 1 set at?[1-10]: "))
    dial_set2 = int(input("What is dial 2 set at?[1-10]: "))
    dial_set3 = int(input("What is dial 3 set at?[1-10]: "))
    dial_set4 = int(input("What is dial 4 set at?[1-10]: "))
    #set up numbers for maths
    while e == "no":
        #negative_check = False
        counter_null = 0
        message = input("What's the letter?: ")
        signal = alphabet.index(message)
        rotor1_output = signal * dial_set1
        rotor2_output = rotor1_output + dial_set1
        rotor3_output = rotor2_output - (3 * dial_set2)
        rotor4_output = rotor3_output - dial_set3
        #maths to work out code
        if rotor4_output < 0:
            rotor4_output = abs(rotor4_output)
            print("Negative")
            #can't have negative numbers
            #negative_check = True
        if rotor4_output >= 26:
            rotor4_output = set_num(rotor4_output)
            counter_null = counter_null + 1
            #cant have numbers above 25
            #allows to know amount of rollback for decryption
        print(alphabet[rotor4_output])
        print(counter_null)
        #output
        #print(negative_check)
        e = input("Is the message done?[yes/no]:")
        
def decode(f):
    dial_set1 = int(input("What is dial 1 set at?[1-10]: "))
    dial_set2 = int(input("What is dial 2 set at?[1-10]: "))
    dial_set3 = int(input("What is dial 3 set at?[1-10]: "))
    dial_set4 = int(input("What is dial 4 set at?[1-10]: "))
    #start of decryption
    while f == "no":
        message = input("What's the letter?: ")
        #give me a letter
        check1 = input("Is it negative?: ")
        #Resets number to negative
        check2 = int(input("What is the number?: "))
        #reverses rollback
        signal = alphabet.index(message)
        rotor4_output = signal + (26 * check2)
        if check1 == "yes":
            signal = 0 - signal
        rotor3_output = rotor4_output - dial_set3
        rotor2_output = rotor3_output + (2 * dial_set2)
        rotor1_output = rotor2_output + dial_set1
        signal0 = rotor1_output / dial_set1
        #backwards maths
        print(alphabet[math.floor(signal0)])
        f = input("Is the message done?[yes/no]:")
        
if need_to_encode == "yes":
    encode(message_done)
else:
    decode(message_done)
    #function calls
