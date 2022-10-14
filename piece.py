import pygame


class piece:
    def __init__(self,name,x,y,colour):
        self.name = name
        self.x = x
        self.y = y
        self.initialX = x
        self.initialY = y
        self.color = colour #black = 1, white = -1
        self.moved = False


    def findMoves(self,board, blackPieces, whitePieces):
        possibleMoves = [] #x, y, Kill
        x = self.x
        y = self.y
        color = self.color

        if self.name == 'whitePawn':
            if x == self.initialX and y == self.initialY:
                if x in range(0,8) and y-2 in range(0,8):
                    if board[x][y-2] == 0 and board[x][y-1] == 0:
                        possibleMoves.append([x,y-2,False])
                if x in range(0,8) and y-1 in range(0,8):
                    if board[x][y-1] == 0:
                        possibleMoves.append([x,y-1,False])
                if x-1 in range(0,8) and y-1 in range(0,8):
                    if board[x-1][y-1] == 1:
                        possibleMoves.append([x-1,y-1,True])
                if x+1 in range(0,8) and y-1 in range(0,8):
                    if board[x+1][y-1] == 1:
                        possibleMoves.append([x+1,y-1,True])
            else:
                if x in range(0,8) and y-1 in range(0,8):
                    if board[x][y-1] == 0:
                        possibleMoves.append([x,y-1,False])
                if x-1 in range(0,8) and y-1 in range(0,8):
                    if board[x-1][y-1] == 1:
                        possibleMoves.append([x-1,y-1,True])
                if x+1 in range(0,8) and y-1 in range(0,8):
                    if board[x+1][y-1] == 1:
                        possibleMoves.append([x+1,y-1,True])

        elif self.name == 'blackPawn':
            if x == self.initialX and y == self.initialY:
                if x in range(0,8) and y+2 in range(0,8):
                    if board[x][y+2] == 0 and board[x][y+1] == 0:
                        possibleMoves.append([x,y+2,False])
                if x in range(0,8) and y+1 in range(0,8):
                    if board[x][y+1] == 0:
                        possibleMoves.append([x,y+1,False])
                if x-1 in range(0,8) and y+1 in range(0,8):
                    if board[x-1][y+1] == -1:
                        possibleMoves.append([x-1,y+1,True])
                if x+1 in range(0,8) and y+1 in range(0,8):
                    if board[x+1][y+1] == -1:
                        possibleMoves.append([x+1,y+1,True])
            else:
                if x in range(0,8) and y+1 in range(0,8):
                    if board[x][y+1] == 0:
                        possibleMoves.append([x,y+1,False])
                if x-1 in range(0,8) and y+1 in range(0,8):
                    if board[x-1][y+1] == -1:
                        possibleMoves.append([x-1,y+1,True])
                if x+1 in range(0,8) and y+1 in range(0,8):
                    if board[x+1][y+1] == -1:
                        possibleMoves.append([x+1,y+1,True])

        elif self.name[5:] == 'Knight':
            if x+2 in range(0,8) and y+1 in range(0,8) and board[x+2][y+1] != color:
                if board[x+2][y+1] == 0:
                    possibleMoves.append([x+2,y+1,False])
                else:
                    possibleMoves.append([x+2,y+1,True])
            if x+2 in range(0,8) and y-1 in range(0,8) and board[x+2][y-1] != color:
                if board[x+2][y-1] == 0:
                    possibleMoves.append([x+2,y-1,False])
                else:
                    possibleMoves.append([x+2,y-1,True])
            if x-2 in range(0,8) and y+1 in range(0,8) and board[x-2][y+1] != color:
                if board[x-2][y+1] == 0:
                    possibleMoves.append([x-2,y+1,False])
                else:
                    possibleMoves.append([x-2,y+1,True])
            if x-2 in range(0,8) and y-1 in range(0,8) and board[x-2][y-1] != color:
                if board[x-2][y-1] == 0:
                    possibleMoves.append([x-2,y-1,False])
                else:
                    possibleMoves.append([x-2,y-1,True])
            if x+1 in range(0,8) and y-2 in range(0,8) and board[x+1][y-2] != color:
                if board[x+1][y-2] == 0:
                    possibleMoves.append([x+1,y-2,False])
                else:
                    possibleMoves.append([x+1,y-2,True])
            if x+1 in range(0,8) and y+2 in range(0,8) and board[x+1][y+2] != color:
                if board[x+1][y+2] == 0:
                    possibleMoves.append([x+1,y+2,False])
                else:
                    possibleMoves.append([x+1,y+2,True])
            if x-1 in range(0,8) and y+2 in range(0,8) and board[x-1][y+2] != color:
                if board[x-1][y+2] == 0:
                    possibleMoves.append([x-1,y+2,False])
                else:
                    possibleMoves.append([x-1,y+2,True])
            if x-1 in range(0,8) and y-2 in range(0,8) and board[x-1][y-2] != color:
                if board[x-1][y-2] == 0:
                    possibleMoves.append([x-1,y-2,False])
                else:
                    possibleMoves.append([x-1,y-2,True])
        
        elif self.name[5:] == 'Queen':
            for i in range(1,8):
                if x+i in range(0,8):
                    if board[x+i][y] == 0:
                        possibleMoves.append([x+i,y,False])
                    elif board[x+i][y] == color*-1:
                        possibleMoves.append([x+i,y,True])
                        break
                    else:
                        break

            for i in range(1,8):
                if x-i in range(0,8):
                    if board[x-i][y] == 0:
                        possibleMoves.append([x-i,y,False])
                    elif board[x-i][y] == color*-1:
                        possibleMoves.append([x-i,y,True])
                        break
                    else:
                        break

            for i in range(1,8):
                if y+i in range(0,8):
                    if board[x][y+i] == 0:
                        possibleMoves.append([x,y+i,False])
                    elif board[x][y+i] == color*-1:
                        possibleMoves.append([x,y+i,True])
                        break
                    else:
                        break

            for i in range(1,8):
                if y-i in range(0,8):
                    if board[x][y-i] == 0:
                        possibleMoves.append([x,y-i,False])
                    elif board[x][y-i] == color*-1:
                        possibleMoves.append([x,y-i,True])
                        break
                    else:
                        break

            for i in range(1,8):
                if x-i in range(0,8) and y-i in range(0,8):
                    if board[x-i][y-i] == 0:
                        possibleMoves.append([x-i,y-i,False])
                    elif board[x-i][y-i] == color*-1:
                        possibleMoves.append([x-i,y-i,True])
                        break
                    else:
                        break

            for i in range(1,8):
                if x+i in range(0,8) and y+i in range(0,8):
                    if board[x+i][y+i] == 0:
                        possibleMoves.append([x+i,y+i,False])
                    elif board[x+i][y+i] == color*-1:
                        possibleMoves.append([x+i,y+i,True])
                        break
                    else:
                        break

            for i in range(1,8):
                if x-i in range(0,8) and y+i in range(0,8):
                    if board[x-i][y+i] == 0:
                        possibleMoves.append([x-i,y+i,False])
                    elif board[x-i][y+i] == color*-1:
                        possibleMoves.append([x-i,y+i,True])
                        break
                    else:
                        break

            for i in range(1,8):
                if x+i in range(0,8) and y-i in range(0,8):
                    if board[x+i][y-i] == 0:
                        possibleMoves.append([x+i,y-i,False])
                    elif board[x+i][y-i] == color*-1:
                        possibleMoves.append([x+i,y-i,True])
                        break
                    else:
                        break

        elif self.name[5:] == 'Rook':
            for i in range(1,8):
                if x+i in range(0,8):
                    if board[x+i][y] == 0:
                        possibleMoves.append([x+i,y,False])
                    elif board[x+i][y] == color*-1:
                        possibleMoves.append([x+i,y,True])
                        break
                    else:
                        break

            for i in range(1,8):
                if x-i in range(0,8):
                    if board[x-i][y] == 0:
                        possibleMoves.append([x-i,y,False])
                    elif board[x-i][y] == color*-1:
                        possibleMoves.append([x-i,y,True])
                        break
                    else:
                        break

            for i in range(1,8):
                if y+i in range(0,8):
                    if board[x][y+i] == 0:
                        possibleMoves.append([x,y+i,False])
                    elif board[x][y+i] == color*-1:
                        possibleMoves.append([x,y+i,True])
                        break
                    else:
                        break

            for i in range(1,8):
                if y-i in range(0,8):
                    if board[x][y-i] == 0:
                        possibleMoves.append([x,y-i,False])
                    elif board[x][y-i] == color*-1:
                        possibleMoves.append([x,y-i,True])
                        break
                    else:
                        break

        elif self.name[5:] == 'Bishop':
            for i in range(1,8):
                if x-i in range(0,8) and y-i in range(0,8):
                    if board[x-i][y-i] == 0:
                        possibleMoves.append([x-i,y-i,False])
                    elif board[x-i][y-i] == color*-1:
                        possibleMoves.append([x-i,y-i,True])
                        break
                    else:
                        break

            for i in range(1,8):
                if x+i in range(0,8) and y+i in range(0,8):
                    if board[x+i][y+i] == 0:
                        possibleMoves.append([x+i,y+i,False])
                    elif board[x+i][y+i] == color*-1:
                        possibleMoves.append([x+i,y+i,True])
                        break
                    else:
                        break

            for i in range(1,8):
                if x-i in range(0,8) and y+i in range(0,8):
                    if board[x-i][y+i] == 0:
                        possibleMoves.append([x-i,y+i,False])
                    elif board[x-i][y+i] == color*-1:
                        possibleMoves.append([x-i,y+i,True])
                        break
                    else:
                        break

            for i in range(1,8):
                if x+i in range(0,8) and y-i in range(0,8):
                    if board[x+i][y-i] == 0:
                        possibleMoves.append([x+i,y-i,False])
                    elif board[x+i][y-i] == color*-1:
                        possibleMoves.append([x+i,y-i,True])
                        break
                    else:
                        break

        elif self.name[5:] == 'King':
            if x+1 in range(0,8) and y+1 in range(0,8):
                if board[x+1][y+1] == 0:
                    possibleMoves.append([x+1,y+1,False])
                elif board[x+1][y+1] == color*-1:
                    possibleMoves.append([x+1,y+1,True])
            if x+1 in range(0,8) and y-1 in range(0,8):
                if board[x+1][y-1] == 0:
                    possibleMoves.append([x+1,y-1,False])
                elif board[x+1][y-1] == color*-1:
                    possibleMoves.append([x+1,y-1,True])
            if x-1 in range(0,8) and y+1 in range(0,8):
                if board[x-1][y+1] == 0:
                    possibleMoves.append([x-1,y+1,False])
                elif board[x-1][y+1] == color*-1:
                    possibleMoves.append([x-1,y+1,True])
            if x-1 in range(0,8) and y-1 in range(0,8):
                if board[x-1][y-1] == 0:
                    possibleMoves.append([x-1,y-1,False])
                elif board[x-1][y-1] == color*-1:
                    possibleMoves.append([x-1,y-1,True])

            if x+1 in range(0,8):
                if board[x+1][y] == 0:
                    possibleMoves.append([x+1,y,False])
                elif board[x+1][y] == color*-1:
                    possibleMoves.append([x+1,y,True])
            if x-1 in range(0,8):
                if board[x-1][y] == 0:
                    possibleMoves.append([x-1,y,False])
                elif board[x-1][y] == color*-1:
                    possibleMoves.append([x-1,y,True])
            if y+1 in range(0,8):
                if board[x][y+1] == 0:
                    possibleMoves.append([x,y+1,False])
                elif board[x][y+1] == color*-1:
                    possibleMoves.append([x,y+1,True])
            if y-1 in range(0,8):
                if board[x][y-1] == 0:
                    possibleMoves.append([x,y-1,False])
                elif board[x][y-1] == color*-1:
                    possibleMoves.append([x,y-1,True])

        return possibleMoves