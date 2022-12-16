
class TextParser:

    def __init__(self):
        self.FileReadIn = []
        pass

    def ReadFile(self,filepath):
        try:
            fp = open(filepath, "r")
            count = 0
            while True:
                count += 1


                # Get next line from file
                line = fp.readline()
                if not line:
                    break


                self.FileReadIn += [line]
                # if line is empty
                # end of file is reached
                print("Line{}: {}".format(count, line.strip()))

            print(fp.read())
            fp.close()
        except FileNotFoundError:
            print("Please check the path.")

