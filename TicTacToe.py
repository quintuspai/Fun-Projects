board = [" "] * 9
turn = "X"
def draw_board():
    print("{} | {} | {}".format(board[6],board[7], board[8]))
    print("----------")
    print("{} | {} | {}".format(board[3],board[4], board[5]))
    print("----------")
    print("{} | {} | {}".format(board[0],board[1], board[2]))

def game():
    turn = "X"
    count = 0
    for i in range(10):
        draw_board()
        print(turn + " turn. Enter postion\t")
        move = int(input()) - 1
        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("Invalid move. Filled\n Try Again : \t")
            continue
        if count >= 5:
            if board[6] == board[7] == board[8] != " ":
                print("\n Game Over.\n")
                print(" !!!!!!! " +turn + " won. !!!!!!! ")
                break
            elif board[3] == board[4] == board[5] != " ":
                print("\n Game Over.\n")
                print(" !!!!!!! " +turn + " won. !!!!!!! ")
                break
            elif board[0] == board[1] == board[2] != " ":
                print("\n Game Over.\n")
                print(" !!!!!!! " +turn + " won. !!!!!!! ")
                break
            elif board[6] == board[3] == board[0] != " ":
                print("\n Game Over.\n")
                print(" !!!!!!! " +turn + " won. !!!!!!! ")
                break
            elif board[7] == board[4] == board[1] != " ":
                print("\n Game Over.\n")
                print(" !!!!!!! " +turn + " won. !!!!!!! ")
                break
            elif board[8] == board[5] == board[2] != " ":
                print("\n Game Over.\n")
                print(" !!!!!!! " +turn + " won. !!!!!!! ")
                break
            elif board[6] == board[4] == board[2] != " ":
                print("\n Game Over.\n")
                print(" !!!!!!! " +turn + " won. !!!!!!! ")
                break
            elif board[0] == board[4] == board[8] != " ":
                print("\n Game Over.\n")
                print(" !!!!!!! " +turn + " won. !!!!!!! ")
                break
        
        if count == 9:
            print("Game Over\n It's a draw.\n")
        
        turn = "O" if turn == "X" else "X"
        
    play_again = input("Do you want to play again? y or n : ")
        
    if play_again == 'y' or play_again == 'Y':
        for i in board:
            board[i] = " "
        game()
            
if __name__ == "__main__":
    game()