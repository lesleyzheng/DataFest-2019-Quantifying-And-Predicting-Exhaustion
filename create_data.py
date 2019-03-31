import pickle
import csv

#storing data
with open('data/gps.csv') as csvfile:

    readCSV = csv.reader(csvfile, delimiter=',')

    row_num = 0

    for row in readCSV:
        if(row_num==0):
            player_game_dict = dict()
            frame_game_dict = dict()
        else:

            key = row[0] #game id
            half = row[1]
            playerID = row[2]
            frameID = row[3]
            time = row[4]
            gameClock = row[5]
            speed = row[6]
            accelImpulse = row[7]
            accelX = row[8]
            accelY = row[9]
            accelZ = row[10]
            long = row[11]
            lat = row[12]

            # creating player_game_dict
            if key not in player_game_dict:
                player_game_dict[key] = dict()
                player_game_dict[key][half] = dict()
                player_game_dict[key][half][playerID] = []
                player_game_dict[key][half][playerID].append([frameID, time, gameClock, speed, accelImpulse,
                                                  accelX, accelY, accelZ, long, lat])
            else: #if key is in game_dict
                if half not in player_game_dict[key]:
                    player_game_dict[key][half] = dict()
                    player_game_dict[key][half][playerID] = []
                    player_game_dict[key][half][playerID].append([frameID, time, gameClock, speed, accelImpulse,
                                                           accelX, accelY, accelZ, long, lat])

                else: #the half game is already stored
                    if playerID not in player_game_dict[key][half]:
                        player_game_dict[key][half][playerID] = []
                        player_game_dict[key][half][playerID].append([frameID, time, gameClock, speed, accelImpulse,
                                                               accelX, accelY, accelZ, long, lat])
                    else: #player already registered
                        player_game_dict[key][half][playerID].append([frameID, time, gameClock, speed, accelImpulse,
                                                               accelX, accelY, accelZ, long, lat])

            # creating frame_game_dict
            if key not in frame_game_dict:
                frame_game_dict[key] = dict()
                frame_game_dict[key][half] = dict()
                frame_game_dict[key][half][frameID] = []
                frame_game_dict[key][half][frameID].append([playerID, time, gameClock, speed, accelImpulse,
                                                  accelX, accelY, accelZ, long, lat])
            else: #if key is in game_dict
                if half not in frame_game_dict[key]:
                    frame_game_dict[key][half] = dict()
                    frame_game_dict[key][half][frameID] = []
                    frame_game_dict[key][half][frameID].append([playerID, time, gameClock, speed, accelImpulse,
                                                           accelX, accelY, accelZ, long, lat])

                else: #the half game is already stored
                    if frameID not in frame_game_dict[key][half]:
                        frame_game_dict[key][half][frameID] = []
                        frame_game_dict[key][half][frameID].append([playerID, time, gameClock, speed, accelImpulse,
                                                               accelX, accelY, accelZ, long, lat])
                    else: #player already registered
                        frame_game_dict[key][half][frameID].append([playerID, time, gameClock, speed, accelImpulse,
                                                               accelX, accelY, accelZ, long, lat])

        row_num+=1
csvfile.close()

print("complete!")

pickle_out = open("./data/player_game_dict.pkl", "wb")
desc = "a dictionary of game.csv; game_id, half_game, player ID"
pickle.dump((player_game_dict, desc), pickle_out)
pickle_out.close()

pickle_out_2 = open("./data/frame_game_dict.pkl", "wb")
desc2 = "a dictionary of game csv; game_id, half_game, frameID"
pickle.dump((frame_game_dict, desc), pickle_out_2)
pickle_out_2.close()

print("file loaded")


