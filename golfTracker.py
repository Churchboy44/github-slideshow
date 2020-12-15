'''Author: Stephen Lorenz
Created for Code Lou's end of course Python project
---info---
This program tracks the golf score inputs of 2 players,
then returns the name of the winner and their score,
then asks if they want to play again
the info is then saved to a text file with a name chosen by the user'''

import re


def record_score_card(file_name, player1, player2):
    with open (file_name, "w") as scoreCard:
        for item in player1:
            scoreCard.write(item,' ')
        scoreCard.write('\n')
        for item in player2:
            scoreCard.write(item,' ')


if __name__ == '__main__':
    p1 = input("Please enter player 1's name: ").split()
    p2 = input("Please enter the second player's name: ").split()

    count = 1
    while True:
        answer = input('How many strokes did {} make on hole {}? Enter "done" to quit: '.format(p1[0], count)).lower()
        if answer == 'done':
            break
        else:
            p1.append(int(answer))

        p2.append(int(input('How many strokes did {} make on hole {}? '.format(p2[0], count))))
        print()
        count += 1

    p1_score = 0
    for points in range(1,len(p1)):
        p1_score += p1[points]

    p2_score = 0
    for points in range(1,len(p2)):
        p2_score += p2[points]

    
    if p1_score < p2_score:
        print("And the winner is {} with {} strokes!".format(p1[0], p1_score))
        print("{} made {} strokes.".format(p2[0], p2_score))
    else:
        print("And the winner is {} with {} strokes!".format(p2[0], p2_score))
        print("{} made {} strokes.\n".format(p1[0], p1_score))
    
