import pickle

pickle_in = open("./data/frame_game_dict.pkl", "rb")
frame_dict, desc = pickle.load(pickle_in)
print(desc)

for game in frame_dict.keys():

    myGame = frame_dict[game]

    for halves in myGame.keys():

        myHalfGame = myGame[halves]

        num_frames = len(myHalfGame)

        tempHalfGameXs = [None]*num_frames
        tempHalfGameYs = [None]*num_frames
        counter = 0

        for specific_frame in myHalfGame.keys():

            tempXs = [None] * 17
            tempYs = [None] * 17

            for i in range(len(myHalfGame[specific_frame])):

                player_id = int(myHalfGame[specific_frame][i][0])
                player_lat = float(myHalfGame[specific_frame][i][8])
                player_long = float(myHalfGame[specific_frame][i][9])

                tempXs[player_id-1] = player_lat
                tempYs[player_id-1] = player_long

            tempHalfGameXs[counter] = tempXs
            tempHalfGameYs[counter] = tempYs
            counter+=1

        break

    break

pickle_out = open("./data/play_gpsdata.pkl", "wb")
desc = "one set of gps data specific to one half game"
pickle.dump((tempHalfGameXs, tempHalfGameYs, desc), pickle_out)
pickle_out.close()