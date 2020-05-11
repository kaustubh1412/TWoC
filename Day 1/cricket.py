score1 = int(input("First player's score: "))
score2 = int(input("Second player's score: "))
score3 = int(input("Third player's score: "))
balls = 60

strike_rate_1 = (score1/balls)*100
strike_rate_2 = (score2/balls)*100
strike_rate_3 = (score3/balls)*100
print("The strike rate of each player is: " + str(strike_rate_1) + " "+ str(strike_rate_2) + " " + str(strike_rate_3))

new_score_1 = score1 + strike_rate_1*60/100
new_score_2 = score2 + strike_rate_2*60/100
new_score_3 = score3 + strike_rate_3*60/100
print("Score of each batsman if they playeda another 60 balls: " + str(new_score_1) + " " + str(new_score_2) + " " + str(new_score_3))

sixes_1 = score1//6
sixes_2 = score2//6
sixes_3 = score3//6
print("Maximum number of sixes each player hits: " + str(sixes_1) + " " + str(sixes_2) + " " + str(sixes_3))