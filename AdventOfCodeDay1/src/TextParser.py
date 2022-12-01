
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
        ListOfElves = []
        if len(self.FileReadIn) == 0 :
            return False

        ElfNumber = 1

        ListOfElves = []
        ElfInventory = []
        TotalCalories = 0
        MaxCaloriesHighWaterMark = 0
        MaxCaloriesElf = 0

        for line in self.FileReadIn:
            if line.strip():
                print("Elf %s has %s" % (ElfNumber,line.strip()))
                ElfInventory += [line.strip()]
                TotalCalories += int(line.strip())
            else:
                print('Next Elf !')
                ListOfElves += [[[ElfNumber],[ElfInventory],[TotalCalories]]]

                if TotalCalories > MaxCaloriesHighWaterMark :
                    MaxCaloriesElf = ElfNumber
                    MaxCaloriesHighWaterMark = TotalCalories
                ElfNumber += 1
                TotalCalories = 0


        return MaxCaloriesElf,MaxCaloriesHighWaterMark
