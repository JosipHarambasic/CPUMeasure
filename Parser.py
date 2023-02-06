class Parser:
    def __init__(self, collectedDataFile):
        self.collectedDataFile = collectedDataFile

    def parse(self):
        nethogs = open(self.collectedDataFile, "r")

        parsedFile = []
        uploadxmrig = 0
        uploadsensor = []
        downloadxmrig = 0
        downloadsnesor = []
        counter = 1
        ind = 0
        id = 0
        for i in nethogs:
            index = 0
            if i.startswith("Refreshing:"):
                counter += 1
                uploadsensor.append(uploadxmrig)
                downloadsnesor.append(downloadxmrig)
                uploadxmrig = 0
                downloadxmrig = 0
            if not i.startswith("Refreshing:"):
                for j in i:
                    if j.isalpha():
                        i = i[index:].strip().replace('/(\r\n|\n|\r)/gm', "")
                        break
                    index += 1
                if len(i) > 1:
                    file = (" ".join(i.split()).split(" ")[::-1])
                    if not file[2].startswith("es_sensor"):
                        uploadxmrig+= float(file[1])
                        downloadxmrig+= float(file[0])

        return uploadxmrig, downloadxmrig, uploadsensor, downloadsnesor
