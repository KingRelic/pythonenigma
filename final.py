import math
 
alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

message_done = "no"

need_to_encode = input("Need to encode?: ")

def set_num(g):
    while True:
        g = g - 26
        if g < 26:
            break;
    return g

def encode(e):
    dial_set1 = int(input("What is dial 1 set at?[1-10]: "))
    dial_set2 = int(input("What is dial 2 set at?[1-10]: "))
    dial_set3 = int(input("What is dial 3 set at?[1-10]: "))
    dial_set4 = int(input("What is dial 4 set at?[1-10]: "))
    while e == "no":
        #negative_check = False
        counter_null = 0
        message = input("What's the letter?: ")
        signal = alphabet.index(message)
        rotor1_output = signal * dial_set1
        rotor2_output = rotor1_output + dial_set1
        rotor3_output = rotor2_output - (3 * dial_set2)
        rotor4_output = rotor3_output - dial_set3
        if rotor4_output < 0:
            rotor4_output = abs(rotor4_output)
            print("Negative")
            #negative_check = True
        if rotor4_output >= 26:
            rotor4_output = set_num(rotor4_output)
            counter_null = counter_null + 1
        print(alphabet[rotor4_output])
        print(counter_null)
        #print(negative_check)
        e = input("Is the message done?[yes/no]:")
        
def decode(f):
    dial_set1 = int(input("What is dial 1 set at?[1-10]: "))
    dial_set2 = int(input("What is dial 2 set at?[1-10]: "))
    dial_set3 = int(input("What is dial 3 set at?[1-10]: "))
    dial_set4 = int(input("What is dial 4 set at?[1-10]: "))
    while f == "no":
        message = input("What's the letter?: ")
        check1 = input("Is it negative?: ")
        check2 = int(input("What is the number?: "))
        signal = alphabet.index(message)
        if check1 == "yes":
            signal = 0 - signal
        rotor4_output = signal + (26 * check2)
        rotor3_output = rotor4_output - dial_set3
        rotor2_output = rotor3_output + (2 * dial_set2)
        rotor1_output = rotor2_output + dial_set1
        signal0 = rotor1_output / dial_set1
        print(alphabet[math.floor(signal0)])
        f = input("Is the message done?[yes/no]:")
        
if need_to_encode == "yes":
    encode(message_done)
else:
    decode(message_done)

