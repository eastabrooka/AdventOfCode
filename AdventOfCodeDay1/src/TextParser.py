
class TextParser:

    def __init__(self):
        self.FileReadIn = []
        self.ListOfElves = []

        pass

    def ReadFile(self,filepath):
        # Opening the file with relative path
        self.ListOfElves = []
        try:
            fp = open(filepath, "r")

            count = 0
            while True:
                count += 1

                # Get next line from file
                line = fp.readline()
                self.FileReadIn += [line]
                # if line is empty
                # end of file is reached
                if not line:
                    break
                print("Line{}: {}".format(count, line.strip()))

            print(fp.read())
            fp.close()
        except FileNotFoundError:
            print("Please check the path.")

    def SplitFileIntoElves(self):
        if len(self.FileReadIn) == 0 :
            return False

        ElfNumber = 1

        ElfInventory = []
        TotalCalories = 0
        MaxCaloriesHighWaterMark = 0
        MaxCaloriesElf = 0
        self.ListOfElves=[]

        for line in self.FileReadIn:
            if line.strip():
                print("Elf %s has %s" % (ElfNumber,line.strip()))
                ElfInventory += [line.strip()]
                TotalCalories += int(line.strip())
            else:
                print('Next Elf !')
                self.ListOfElves += [[[ElfNumber],[ElfInventory],[TotalCalories]]]

                if TotalCalories > MaxCaloriesHighWaterMark :
                    MaxCaloriesElf = ElfNumber
                    MaxCaloriesHighWaterMark = TotalCalories
                ElfNumber += 1
                TotalCalories = 0


        return MaxCaloriesElf,MaxCaloriesHighWaterMark

    def DoExtendedChallenge(self):
        postprocess = []

        for Elf in self.ListOfElves:
            print("Elf %s has %s" % (Elf[0], Elf[2]))
            #At this point, I want to go do something else
            Temp1 = Elf[0]
            Temp1 = Temp1[0]
            Temp2 = Elf[2]
            Temp2 = Temp2[0]

            postprocess += [ [Temp1, int(Temp2)]]
        from operator import itemgetter
        print("Sorted List B based on index 1: % s" % (sorted(postprocess, key=itemgetter(1),reverse=True)))
        output = (sorted(postprocess, key=itemgetter(1),reverse=True))

        goal1 =  output[0][1]
        goal2 =  output[1][1]
        goal3 =  output[2][1]


        print ( goal1 + goal2 + goal3)
        pass