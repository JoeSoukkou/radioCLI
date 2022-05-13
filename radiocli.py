import json
import os 

stationsFile = open("stations.json")

parsedStations = json.load(stationsFile)

stationsFile.close() 

print("---------------Welcome to RadioCLI------------------")
print("This is a barebone cli tool that lets you")
print("listen to the radio stations over the terminal")
print("using only mpv and a json file")
print("----------------------------------------------------")

def loop() :
    print("> Enter l to list available stations")
    print("> Enter p followed by the ID of the radio channel to play it")
    l = input("> ")
    if (l == 'l') : 
        for station in parsedStations : 
            print(str(station["id"]) + ':' + station["station"]["name"])
        loop()
    elif (l and l != "" and l[0] == "p") :   
        aRGS = l.split(' ')
        id = int(aRGS[1])
        for st in parsedStations :
            if (st["id"] == id) :
                url = st["station"]["url"]
                name = st["station"]["name"]
                print("playing ... " + name)
                print("press q to quit")
                command = "mpv " + url
                os.system(command)
                loop()
            
    elif (l == 'q'): 
        os.system("exit")                
    else : 
        print("Invalid Command !")
        loop()            

loop()
   