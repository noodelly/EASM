import sys
import os
import time

startTime = time.perf_counter()
entry_pointer_name = 0
entry_pointer_loc = 0
toklist = []

#TODO
#def convert_to_bin(code):
 #   print(type(code))
  #  print(bin(code))
    
  #  return code

def lex(line, count):
    machine_code = 0
    #Remove whitespace
    line = line.replace("\t", "")
    line = line.replace(" ", "")
    line = line.upper()
    if len(line.strip()) == 0:
        print("Whitespace, skip.")
        pass
    elif "MOVI" in line:
        machine_code = 6000
        dpointer = line.find("$")
        dpointer = line[dpointer+2]
        machine_code = machine_code + int(dpointer) * 100
        cpointer = line.find(",")
        cpointer = int(line[cpointer+1:])
        machine_code = machine_code + cpointer
        print(str(machine_code))
        file = open("a.eo", "a")
        file.write(str(machine_code) + "\n")
    elif ".GLOBAL" in line:
        entry_pointer = line.find("_")
        entry_pointer = line[entry_pointer:]
        print("Entry pointer is " + entry_pointer)
    elif line[0] == "_":
        print("Subroutine found! " + line)
        
        
        
        
    
    
def read(file):
    lines = []
    lines = file.readlines()
    count = 0
    for line in lines:
        lex(line, count)
        count = count + 1
    

def main():
    #open file
    file = open(sys.argv[1], "r")
    print("Assembling: " + sys.argv[1])
    read(file)
    print("Lexed in: " + str(time.perf_counter()) + " ms")
    print("Assembled in: " + str(time.perf_counter()) + " ms!")
    
main()