import re


def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True


class Decoder:
    def __init__(self,LineToDecode):
        self.Data = LineToDecode
        pass



    def FindStartMarker(self):

        RollingDecode = self.Data[0:14]
        RollingDecode = [*RollingDecode]
        Restbuffer = self.Data[14:]

        index = 14
        for x in Restbuffer :
            #print ("Checking for ",RollingDecode)

            if (checkIfDuplicates_1(RollingDecode)):
                #print("Duplicates Found !")
                pass
            else:
                print (" No Duplicates")
                print ("Index", index)
                return index

            #Pop the 1st char.
            RollingDecode.pop(0)
            #Add the next one.
            RollingDecode.append(x)
            index +=1
