#This specific set is reviewed proteins found within humans, 
#and contains 20,379 proteins.

#If you want to switch data sets, download your search results 
#from the above website as FASTA, and then just change the 
#extension to a .txt


fileName = "sequenceData.txt"
sequenceData = []
sequenceInfo = []

def getData():
    with open(fileName,'r') as fp:
        i = -1
        for line in fp:
            if(line[0] == '>'):
                i = i+1
                sequenceInfo.append(line)
            else:
                if(i == len(sequenceData)):
                    sequenceData.append(line)
                else:
                    sequenceData.append(line)
                    #sequenceData[i]+=line
    return

#the checkSequence() function takes in the amino acid sequence 
#and checks the file for any matching sequences, and alerts the 
#user if there are any possible matches that the passed sequence 
#contain and tells the user which sequence match is closest 
#in size.


def checkSequence(AAsequence):
    getData()
    count = 0
    bestMatch = -1
    bestMatchID = -1
    i = 0
    for entry in sequenceData:
        if(AAsequence in entry):
            print("Amino acid sequence contained within:")
            print(sequenceInfo[i])
            if(len(AAsequence)/len(entry) > bestMatch):
                bestMatch = len(AAsequence)/len(entry)
                bestMatchID = i
            count+=1
        i += 1
    print("Total number of potential matches: " + str(count))
    if(bestMatchID > -1):
        print("\nClosest potential match: \n" 
              + sequenceInfo[bestMatchID] + "\n" 
              + sequenceData[bestMatchID])
    return


checkSequence("MPTTK")