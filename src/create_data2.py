import pickle
import csv

#storing data
# with open('data/wellness2.csv') as csvfile:
#
#     readCSV = csv.reader(csvfile, delimiter=',')
#
#     exhaustion = dict()
#     for row in readCSV:
#         key = row[0]
#         name = row[1]
#         exhaustion[key] = dict()
#         exhaustion[key][name] = row[2]
#
# csvfile.close()

with open('data/gameday2.csv') as csvfile2:

    readCSV2 = csv.reader(csvfile2, delimiter=',')
    #length 334
    X = [None]*169
    y = [None]*169

    info = dict()
    index = 0
    for row in readCSV2:
        # create first game data
        # #key
        # date = row[0]
        # playerID = row[1]
        # info[index] = [date, playerID]
        #
        # #x values
        # sprintdist = float(row[4])
        # rundist = float(row[5])
        # walkdist = float(row[6])
        # dist = float(row[7])
        # dailyload = float(row[8])
        # try:
        #     acuteload = float(row[9])
        # except ValueError:
        #     acuteload = None
        # try:
        #     chronicload = float(row[10])
        # except ValueError:
        #     chronicload = None
        # temp = [sprintdist, rundist, walkdist, dist, dailyload] #, acuteload, chronicload]
        # X[index] = temp
        #
        # #y value
        # exhaustion = float(row[2])
        # y[index] = exhaustion

        #new
        #x
        sleep = float(row[1])
        pain = float(row[2])
        illness = float(row[3])
        menstration = float(row[4])
        nutrition = float(row[5])
        nutriadjust = float(row[6])
        trainread = float(row[7])
        sprint = float(row[8])
        run = float(row[9])
        walk = float(row[10])
        dist = float(row[11])
        outcome = float(row[12])
        teamp = float(row[13])
        teampa = float(row[14])
        th = float(row[15])
        tl = float(row[16])
        humid = float(row[17])
        pressure = float(row[18])
        windsp = float(row[19])
        X[index] = [sleep, pain, illness, menstration, nutrition, nutriadjust,
                    trainread, sprint, run, walk, dist, outcome, teamp, teampa,
                    th, tl, humid, pressure, windsp]

        #y
        y[index] = float(row[0])



        index+=1

csvfile2.close()

pickle_out = open("./data/data_v2.pkl", "wb")
desc = "X (longer), y" #"identifier dictionary, X, y"
pickle.dump(((X, y), desc), pickle_out)
pickle_out.close()
