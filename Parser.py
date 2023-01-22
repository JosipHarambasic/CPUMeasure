class Parser:
    def __init__(self, collectedDataFile):
        self.collectedDataFile = collectedDataFile

    def parse(self):
        nethogs = open(self.collectedDataFile, "r")

        parsedFile = []
        uploadxmrig = []
        uploadsensor = []
        downloadxmrig = []
        downloadsnesor = []
        counter = 0
        ind = 0
        id = 0
        for i in nethogs:
            index = 0
            if i.startswith("Refreshing:"):
                if len(uploadxmrig) < counter:
                    uploadxmrig.append(0)
                    downloadxmrig.append(0)
                counter += 1
            if not i.startswith("Refreshing:"):
                for j in i:
                    if j.isalpha():
                        i = i[index:].strip().replace('/(\r\n|\n|\r)/gm', "")
                        break
                    index += 1
                if len(i) > 1:
                    file = (" ".join(i.split()).split(" ")[::-1])

                    if file[2].startswith("es_sensor"):
                        uploadsensor.append(float(file[1]))
                        downloadsnesor.append(float(file[0]))
                    if file[2].startswith("xmrig"):
                        uploadxmrig.append(float(file[1]))
                        downloadxmrig.append(float(file[0]))

        return uploadxmrig, downloadxmrig, uploadsensor, downloadsnesor
