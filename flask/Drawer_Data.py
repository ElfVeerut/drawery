import csv

filename = "new_finger_track.csv"
header = ("ID","Name","Item","Public/Private","Availability","Process")
def recall_data():
    global box
    global public_box
    global private_box
    box = []
    public_box = []
    private_box = []
    with open(filename,'r', newline= "") as file:
        reader = csv.reader(file, delimiter=',')
        i=0
        for line in reader:
            if i == 0: i+=1; continue
            box.append(int(line[4]))
        print(box)
        public_box = [box[0],box[1]]
        private_box = [box[2],box[3]]
    
    return 

def rewrite_data(number, dbValue):

    with open(filename,'r', newline= "") as file:

        readData = [row for row in csv.DictReader(file)]
        readData[number-1]['Availability'] = dbValue

    readHeader = readData[0].keys()

    with open (filename, "w", newline = "") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = header)
        writer.writeheader()
        writer.writerows(readData)
#    file.close()
#    csvfile.close()
    return 