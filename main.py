'''
Programmed by Alexander Kung
'''

import sys
import pygame
import random
import copy
 
from piece import piece

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 800,800
screen = pygame.display.set_mode((width, height))

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

turn = -1
inCheck = 0

selectedPiece = []
possibleMoves = []

pieces = pygame.image.load('chessPieces.jpg')

whitePawn = pygame.image.load('whitePawn.png')
whiteRook = pygame.image.load('whiteRook.png')
whiteKnight = pygame.image.load('whiteKnight.png')
whiteBishop = pygame.image.load('whiteBishop.png')
whiteQueen = pygame.image.load('whiteQueen.png')
whiteKing = pygame.image.load('whiteKing.png')

blackBishop = pygame.image.load('blackBishop.png')
blackKing = pygame.image.load('blackKing.png')
blackKnight = pygame.image.load('blackKnight.png')
blackPawn = pygame.image.load('blackPawn.png')
blackQueen = pygame.image.load('blackQueen.png')
blackRook = pygame.image.load('blackRook.png')

board = [[0]*8]*8

blackPieces = []
for i in range(8):
    newPiece = piece('blackPawn',i,1,1)
    blackPieces.append(newPiece)
blackPieces.append(piece('blackKing',4,0,1))
blackPieces.append(piece('blackQueen',3,0,1))
blackPieces.append(piece('blackRook',0,0,1))
blackPieces.append(piece('blackRook',7,0,1))
blackPieces.append(piece('blackKnight',1,0,1))
blackPieces.append(piece('blackKnight',6,0,1))
blackPieces.append(piece('blackBishop',2,0,1))
blackPieces.append(piece('blackBishop',5,0,1))

whitePieces = []
for i in range(8):
    newPiece = piece('whitePawn',i,6,-1)
    whitePieces.append(newPiece)
whitePieces.append(piece('whiteKing',4,7,-1))
whitePieces.append(piece('whiteQueen',3,7,-1))
whitePieces.append(piece('whiteRook',0,7,-1))
whitePieces.append(piece('whiteRook',7,7,-1))
whitePieces.append(piece('whiteKnight',1,7,-1))
whitePieces.append(piece('whiteKnight',6,7,-1))
whitePieces.append(piece('whiteBishop',2,7,-1))
whitePieces.append(piece('whiteBishop',5,7,-1))


def scoreCalcBasic(whitePieces, blackPieces):
    currentScore = 0

    for i in whitePieces:
        if i.name[5:] == 'Pawn':
            currentScore += 1
        elif i.name[5:] == 'Knight':
            currentScore += 3
        elif i.name[5:] == 'Bishop':
            currentScore += 3
        elif i.name[5:] == 'Queen':
            currentScore += 9
        elif i.name[5:] == 'King':
            currentScore += 1000000


    for i in blackPieces:
        if i.name[5:] == 'Pawn':
            currentScore -= 1
        elif i.name[5:] == 'Knight':
            currentScore -= 3
        elif i.name[5:] == 'Bishop':
            currentScore -= 3
        elif i.name[5:] == 'Queen':
            currentScore -= 9
        elif i.name[5:] == 'King':
            currentScore -= 1000000
        
    return currentScore

def setBoard():
    pass

def scoreCalc(whitePieces, blackPieces):
    currentScore = 0

    for i in whitePieces:
        if i.name[5:] == 'Pawn':
            currentScore += 2
        elif i.name[5:] == 'Knight':
            currentScore += 6
        elif i.name[5:] == 'Bishop':
            currentScore += 6
        elif i.name[5:] == 'Queen':
            currentScore += 18
        elif i.name[5:] == 'Rook':
            currentScore += 10
        #elif i.name[5:] == 'King':
            #currentScore += 1000000
        if i.name[5:] == 'Pawn' and i.x == 5 and i.y == 4:
            currentScore += 3
        if i.name[5:] == 'Rook' and i.x != 0 and i.y != 7 and i.x != 7:
            currentScore += 2
        if i.name[5:] == 'Knight' and i.x != 1 and i.y != 7 and i.x != 6:
            currentScore += 1
        if i.name[5:] == 'Bishop' and i.x != 2 and i.y != 7 and i.x != 5:
            currentScore += 1

    for i in blackPieces:
        if i.name[5:] == 'Pawn':
            currentScore -= 2
        elif i.name[5:] == 'Knight':
            currentScore -= 6
        elif i.name[5:] == 'Bishop':
            currentScore -= 6
        elif i.name[5:] == 'Queen':
            currentScore -= 18
        elif i.name[5:] == 'Rook':
            currentScore -= 10
        #elif i.name[5:] == 'King':
            #currentScore -= 1000000
        if i.name[5:] == 'Pawn' and i.x == 5 and i.y == 3:
            currentScore -= 3
        if i.name[5:] == 'Rook' and i.x != 0 and i.y != 0 and i.x != 7:
            currentScore -= 2
        if i.name[5:] == 'Knight' and i.x != 1 and i.y != 0 and i.x != 6:
            currentScore -= 1
        if i.name[5:] == 'Bishop' and i.x != 2 and i.y != 0 and i.x != 5:
            currentScore -= 1

    return currentScore


def minimax(board, whitePieces, blackPieces, newInCheck, turn, depth, alpha, beta):
    #White is maximizing, black is minimizing

    #print(checkmateCheck2(board, turn, whitePieces, blackPieces, newInCheck))

    
    if checkmateCheck2(board, turn, whitePieces, blackPieces, newInCheck):
        print('hi')
        if turn == 1:
            return float('-inf')
        if turn == -1:
            return float('inf')
    
    if depth == 0:
        score = scoreCalcBasic(whitePieces, blackPieces)
        return score


    if turn == 1:
        #black Turn
        minScore = float('inf')
        
        for i in blackPieces:
            breakAll = False
            possibleMoves = copy.deepcopy(i.findMoves(board, blackPieces, whitePieces))
            if i.name == "blackKing":
                possibleMoves = copy.deepcopy(addCastle(board, blackPieces, whitePieces, turn, [i.x,i.y], possibleMoves))
                possibleMoves = pieceLimit(board, possibleMoves, [i.x,i.y], turn)
                #print(possibleMoves)
            if newInCheck != 0:
                kingX = 0
                kingY = 0
                for a in whitePieces:
                    if a.name == "blackKing":
                        kingX = a.x
                        kingY = a.y
                        break

                if i.name == "blackKing":
                    possibleMoves = copy.deepcopy(checkLimit(possibleMoves, [i.x, i.y], turn, i.x, i.y, True))
                else:
                    possibleMoves = copy.deepcopy(checkLimit(possibleMoves, [i.x, i.y], turn, kingX, kingY, False))


            #if i.name == "blackQueen":
             #   print(possibleMoves)

            for j in possibleMoves:
                newBoard = copy.deepcopy(board)
                newWhitePieces = copy.deepcopy(whitePieces)
                newBlackPieces = copy.deepcopy(blackPieces)
                newerInCheck = 0

                if j[2]:
                    #kill
                    for a in newBlackPieces:
                        if a.x == i.x and a.y == i.y:
                            a.x = j[0]
                            a.y = j[1]
                            a.moved = True
                            break
                        
                    
                    for b in range(len(newWhitePieces)):
                        if newWhitePieces[b].x == j[0] and newWhitePieces[b].y == j[1]:
                            newWhitePieces.pop(b)
                            break

                    newBoard = copy.deepcopy(updateBoard2(newBlackPieces, newWhitePieces))

                    temp = 0
                    for a in newBlackPieces:
                        if a.name == "blackKing":
                            temp = checkCheck(copy.deepcopy(newBoard), turn, a.x, a.y)
                    if temp != 0:
                        newerInCheck = temp

                else:
                    #move

                    for a in newBlackPieces:
                        if a.x == i.x and a.y == i.y:
                            a.x = j[0]
                            a.y = j[1]
                            a.moved = True

                            if a.name == "blackKing":
                                newWhitePieces, newBlackPieces = checkCastle2(newBoard, newBlackPieces, newWhitePieces, turn)

                            break

                    newBoard = copy.deepcopy(updateBoard2(newBlackPieces, newWhitePieces))

                    temp = 0
                    for a in newBlackPieces:
                        if a.name == "blackKing":
                            temp = checkCheck(copy.deepcopy(newBoard), turn, a.x, a.y)
                    if temp != 0:
                        newerInCheck = temp
                
                score = minimax(newBoard, newWhitePieces, newBlackPieces, newerInCheck, turn*-1, depth-1, alpha, beta)

                
                minScore = min(score, minScore)

                beta = min(beta, score)
                if beta <= alpha:
                    breakAll = True
                    break

            if breakAll:
                break

        return minScore
        
    elif turn == -1:
        #white Turn
        maxScore = float('-inf')

        for i in whitePieces:
            breakAll = False
            possibleMoves = copy.deepcopy(i.findMoves(board, blackPieces, whitePieces))
            if i.name == "whiteKing":
                possibleMoves = copy.deepcopy(addCastle(board, blackPieces, whitePieces, turn, [i.x,i.y], possibleMoves))
                possibleMoves = pieceLimit(board, possibleMoves, [i.x,i.y], turn)
                #print(possibleMoves)
            if newInCheck != 0:
                kingX = 0
                kingY = 0
                for a in whitePieces:
                    if a.name == "whiteKing":
                        kingX = a.x
                        kingY = a.y
                        break

                if i.name == "whiteKing":
                    possibleMoves = copy.deepcopy(checkLimit(possibleMoves, [i.x, i.y], turn, i.x, i.y, True))
                else:
                    possibleMoves = copy.deepcopy(checkLimit(possibleMoves, [i.x, i.y], turn, kingX, kingY, False))

            for j in possibleMoves:
                newBoard = copy.deepcopy(board)
                newWhitePieces = copy.deepcopy(whitePieces)
                newBlackPieces = copy.deepcopy(blackPieces)
                newerInCheck = 0

                if j[2]:
                    #kill
                    for a in newWhitePieces:
                        if a.x == i.x and a.y == i.y:
                            a.x = j[0]
                            a.y = j[1]
                            a.moved = True
                            break
                        
                    for b in range(len(newBlackPieces)):
                        if newBlackPieces[b].x == j[0] and newBlackPieces[b].y == j[1]:
                            newBlackPieces.pop(b)
                            break

                    newBoard = copy.deepcopy(updateBoard2(newBlackPieces, newWhitePieces))

                    temp = 0
                    for a in newWhitePieces:
                        if a.name == "whiteKing":
                            temp = checkCheck(copy.deepcopy(newBoard), turn, a.x, a.y)
                    if temp != 0:
                        newerInCheck = temp

                else:
                    #move

                    for a in newWhitePieces:
                        if a.x == i.x and a.y == i.y:
                            a.x = j[0]
                            a.y = j[1]
                            a.moved = True

                            if a.name == "whiteKing":
                                newWhitePieces, newBlackPieces = checkCastle2(newBoard, newBlackPieces, newWhitePieces, turn)

                            break

                    newBoard = copy.deepcopy(updateBoard2(newBlackPieces, newWhitePieces))

                    temp = 0
                    for a in newWhitePieces:
                        if a.name == "whiteKing":
                            temp = checkCheck(copy.deepcopy(newBoard), turn, a.x, a.y)
                    if temp != 0:
                        newerInCheck = temp
                
                score = minimax(newBoard, newWhitePieces, newBlackPieces, newerInCheck, turn*-1, depth-1, alpha, beta)

                maxScore = max(score, maxScore)

                alpha = max(alpha, score)
                if beta <= alpha:
                    breakAll = True
                    break
            if breakAll:
                break

        return maxScore

def aiMoveMax(board, whitePieces, blackPieces, inCheck):
    #AI is the maximizing player, white
    maxScore = float('-inf')
    bestBoard = []
    bestWhitePieces = []
    bestBlackPieces = []
    currentPossibleMoves = []
    turn = -1
    depth = 3

    for i in whitePieces:
        possibleMoves = copy.deepcopy(i.findMoves(board, blackPieces, whitePieces))
        if i.name == "whiteKing":
            possibleMoves = copy.deepcopy(addCastle(board, blackPieces, whitePieces, turn, [i.x,i.y], possibleMoves))
            possibleMoves = pieceLimit(board, possibleMoves, [i.x,i.y], turn)
            #print(possibleMoves)
        if inCheck != 0:
            kingX = 0
            kingY = 0
            for a in whitePieces:
                if a.name == "whiteKing":
                    kingX = a.x
                    kingY = a.y
                    break
            
            if i.name == "whiteKing":
                possibleMoves = copy.deepcopy(checkLimit(possibleMoves, [i.x, i.y], turn, i.x, i.y, True))
            else:
                possibleMoves = copy.deepcopy(checkLimit(possibleMoves, [i.x, i.y], turn, kingX, kingY, False))

        for j in possibleMoves:
            newBoard = copy.deepcopy(board)
            newWhitePieces = copy.deepcopy(whitePieces)
            newBlackPieces = copy.deepcopy(blackPieces)
            newerInCheck = 0

            if j[2]:
                #kill
                for a in newWhitePieces:
                    if a.x == i.x and a.y == i.y:
                        a.x = j[0]
                        a.y = j[1]
                        a.moved = True
                        break
                    
                for b in range(len(newBlackPieces)):
                    if newBlackPieces[b].x == j[0] and newBlackPieces[b].y == j[1]:
                        newBlackPieces.pop(b)
                        break

                newBoard = copy.deepcopy(updateBoard2(newBlackPieces, newWhitePieces))

                temp = 0
                for a in newWhitePieces:
                    if a.name == "whiteKing":
                        temp = checkCheck(copy.deepcopy(newBoard), turn, a.x, a.y)
                if temp != 0:
                    newerInCheck = temp

            else:
                #move
                for a in newWhitePieces:
                    if a.x == i.x and a.y == i.y:
                        a.x = j[0]
                        a.y = j[1]
                        a.moved = True
                        if a.name == "whiteKing":
                            newWhitePieces, newBlackPieces = checkCastle2(newBoard, newBlackPieces, newWhitePieces, turn)
                        break

                newBoard = copy.deepcopy(updateBoard2(newBlackPieces, newWhitePieces))

                temp = 0
                for a in newWhitePieces:
                    if a.name == "whiteKing":
                        temp = checkCheck(copy.deepcopy(newBoard), turn, a.x, a.y)
                if temp != 0:
                    newerInCheck = temp
            
            score = minimax(newBoard, newWhitePieces, newBlackPieces, newerInCheck, turn*-1, depth-1, float('-inf'), float('inf'))

            previousMaxScore = copy.deepcopy(maxScore)
            maxScore = max(score, maxScore)

            if maxScore >= previousMaxScore:
                bestBoard = copy.deepcopy(newBoard)
                bestBlackPieces = copy.deepcopy(newBlackPieces)
                bestWhitePieces = copy.deepcopy(newWhitePieces)

    print(maxScore)
    return bestBoard, bestWhitePieces, bestBlackPieces




def pieceDraw(drawnPiece):
    if drawnPiece.name == 'blackPawn':
        screen.blit(blackPawn, (drawnPiece.x*100,drawnPiece.y*100))
    elif drawnPiece.name == 'blackKing':
        screen.blit(blackKing, (drawnPiece.x*100,drawnPiece.y*100))
    elif drawnPiece.name == 'blackQueen':
        screen.blit(blackQueen, (drawnPiece.x*100,drawnPiece.y*100))
    elif drawnPiece.name == 'blackRook':
        screen.blit(blackRook, (drawnPiece.x*100,drawnPiece.y*100))
    elif drawnPiece.name == 'blackKnight':
        screen.blit(blackKnight, (drawnPiece.x*100,drawnPiece.y*100))
    elif drawnPiece.name == 'blackBishop':
        screen.blit(blackBishop, (drawnPiece.x*100,drawnPiece.y*100))
    
    elif drawnPiece.name == 'whitePawn':
        screen.blit(whitePawn, (drawnPiece.x*100,drawnPiece.y*100))
    elif drawnPiece.name == 'whiteKing':
        screen.blit(whiteKing, (drawnPiece.x*100,drawnPiece.y*100))
    elif drawnPiece.name == 'whiteQueen':
        screen.blit(whiteQueen, (drawnPiece.x*100,drawnPiece.y*100))
    elif drawnPiece.name == 'whiteRook':
        screen.blit(whiteRook, (drawnPiece.x*100,drawnPiece.y*100))
    elif drawnPiece.name == 'whiteKnight':
        screen.blit(whiteKnight, (drawnPiece.x*100,drawnPiece.y*100))
    elif drawnPiece.name == 'whiteBishop':
        screen.blit(whiteBishop, (drawnPiece.x*100,drawnPiece.y*100))

def kingLimit():
    global board
    global blackPieces
    global whitePieces
    global turn
    global possibleMoves
    allPossibleEnemyMoves = []

    if turn == 1:
        for i in whitePieces:
            for j in i.findMoves(board, blackPieces, whitePieces):
                if i.name[5:] != 'Pawn':
                    allPossibleEnemyMoves.append(j)
                else:
                    if i.x-1 in range(0,8) and i.y-1 in range(0,8):
                        allPossibleEnemyMoves.append([i.x-1,i.y-1,True])
                    if i.x+1 in range(0,8) and i.y-1 in range(0,8):
                        allPossibleEnemyMoves.append([i.x+1,i.y-1,True])

    elif turn == -1:
        for i in blackPieces:
            if i.name[5:] != 'Pawn':
                for j in i.findMoves(board, blackPieces, whitePieces):
                    allPossibleEnemyMoves.append(j)
            if i.name[5:] == 'Pawn':
                if i.x-1 in range(0,8) and i.y+1 in range(0,8):
                    allPossibleEnemyMoves.append([i.x-1,i.y+1,True])
                if i.x+1 in range(0,8) and i.y+1 in range(0,8):
                    allPossibleEnemyMoves.append([i.x+1,i.y+1,True])

    limitedMoves = []

    newAllPossibleEnemeyMoves = []
    newPossibleMoves = []

    for i in allPossibleEnemyMoves:
        newAllPossibleEnemeyMoves.append(i[:2])

    for i in possibleMoves:
        newPossibleMoves.append(i[:2])


    for i in newPossibleMoves:
        if i in newAllPossibleEnemeyMoves:
            limitedMoves.append(i)


    updatedPossibleMoves = []
    for i in possibleMoves:
        if [i[0],i[1]] not in limitedMoves:
            updatedPossibleMoves.append(i)

    return updatedPossibleMoves
    #possibleMoves = updatedPossibleMoves[:]

def pieceLimit(board, possibleMoves, piecePosition, turn):
    #global board
    global blackPieces
    global whitePieces
    #global possibleMoves
    deathSpots = []

    if turn == 1:
        for i in possibleMoves:
            newBoard = []
            for j in board:
                temp = []
                for x in j:
                    temp.append(x)
                newBoard.append(temp)
            newBoard[i[0]][i[1]] = 1
            newBoard[piecePosition[0]][piecePosition[1]] = 0

            for j in whitePieces:
                for k in j.findMoves(newBoard, blackPieces, whitePieces):
                    if k[0] == i[0] and k[1] == i[1] and k[2] == True:
                        deathSpots.append(k[:2])

    elif turn == -1:
        for i in possibleMoves:
            newBoard = []
            for j in board:
                temp = []
                for x in j:
                    temp.append(x)
                newBoard.append(temp)
            newBoard[i[0]][i[1]] = -1
            newBoard[piecePosition[0]][piecePosition[1]] = 0

            for j in blackPieces:
                for k in j.findMoves(newBoard, blackPieces, whitePieces):
                    if k[0] == i[0] and k[1] == i[1] and k[2] == True:
                        deathSpots.append(k[:2])
    
    newDeathSpots = []
    for i in deathSpots:
        if i not in newDeathSpots:
            newDeathSpots.append(i)
    deathSpots = newDeathSpots

    #print(deathSpots)

    updatedPossibleMoves = []
    for i in possibleMoves:
        if [i[0],i[1]] not in deathSpots:
            updatedPossibleMoves.append(i)

    return updatedPossibleMoves

def addCastle(board, blackPieces, whitePieces, turn, selectedPiece, possibleMoves):
    '''
    global board
    global blackPieces
    global turn
    global whitePieces
    global selectedPiece
    global possibleMoves
    '''

    newPossibleMoves = copy.deepcopy(possibleMoves)

    if turn == 1:
        for i in blackPieces:
            if i.x == selectedPiece[0] and i.y == selectedPiece[1]:
                if i.moved == False:
                    if board[1][0] == 0 and board[2][0] == 0 and board[3][0] == 0:
                        rookGoodPosition = False
                        for j in blackPieces:
                            if j.name == 'blackRook' and j.x == 0 and j.y == 0 and j.moved == False:
                                rookGoodPosition = True
                                break
                        if rookGoodPosition == True:
                            newPossibleMoves.append([2,0,False])
                    if board[5][0] == 0 and board[6][0] == 0:
                        rookGoodPosition = False
                        for j in blackPieces:
                            if j.name == 'blackRook' and j.x == 7 and j.y == 0 and j.moved == False:
                                rookGoodPosition = True
                                break
                        if rookGoodPosition == True:
                            newPossibleMoves.append([6,0,False])
                break

    elif turn == -1:
        for i in whitePieces:
            if i.x == selectedPiece[0] and i.y == selectedPiece[1]:
                if i.moved == False:
                    if board[1][7] == 0 and board[2][7] == 0 and board[3][7] == 0:
                        rookGoodPosition = False
                        for j in whitePieces:
                            if j.name == 'whiteRook' and j.x == 0 and j.y == 7 and j.moved == False:
                                rookGoodPosition = True
                                break
                        if rookGoodPosition == True:
                            newPossibleMoves.append([2,7,False])
                    if board[5][7] == 0 and board[6][7] == 0:
                        rookGoodPosition = False
                        for j in whitePieces:
                            if j.name == 'whiteRook' and j.x == 7 and j.y == 7 and j.moved == False:
                                rookGoodPosition = True
                                break
                        if rookGoodPosition == True:
                            newPossibleMoves.append([6,7,False])
                            
                break
    return newPossibleMoves

def checkCastle():
    global board
    global blackPieces
    global turn
    global whitePieces
    global selectedPiece
    global possibleMoves
    if turn == 1:
        for i in blackPieces:
            if i.name == 'blackKing':
                if i.x == 2 and i.y == 0:
                    for j in blackPieces:
                        if j.name == 'blackRook' and j.x == 0 and j.y == 0:
                            j.x = 3
                            j.y = 0
                            j.moved = True
                if i.x == 6 and i.y == 0:
                    for j in blackPieces:
                        if j.name == 'blackRook' and j.x == 7 and j.y == 0:
                            j.x = 5
                            j.y = 0
                            j.moved = True
    elif turn == -1:
        for i in whitePieces:
            if i.name == 'whiteKing':
                if i.x == 2 and i.y == 7:
                    for j in whitePieces:
                        if j.name == 'whiteRook' and j.x == 0 and j.y == 7:
                            j.x = 3
                            j.y = 7
                            j.moved = True
                if i.x == 6 and i.y == 7:
                    for j in whitePieces:
                        if j.name == 'whiteRook' and j.x == 7 and j.y == 7:
                            j.x = 5
                            j.y = 7
                            j.moved = True

def checkCastle2(board, blackPieces, whitePieces, turn):

    newBlackPieces = copy.deepcopy(blackPieces)
    newWhitePieces = copy.deepcopy(whitePieces)

    if turn == 1:
        for i in newBlackPieces:
            if i.name == 'blackKing':
                if i.x == 2 and i.y == 0:
                    for j in newBlackPieces:
                        if j.name == 'blackRook' and j.x == 0 and j.y == 0:
                            j.x = 3
                            j.y = 0
                            j.moved = True
                            break
                if i.x == 6 and i.y == 0:
                    for j in newBlackPieces:
                        if j.name == 'blackRook' and j.x == 7 and j.y == 0:
                            j.x = 5
                            j.y = 0
                            j.moved = True
                            break
    elif turn == -1:
        for i in newWhitePieces:
            if i.name == 'whiteKing':
                if i.x == 2 and i.y == 7:
                    for j in newWhitePieces:
                        if j.name == 'whiteRook' and j.x == 0 and j.y == 7:
                            j.x = 3
                            j.y = 7
                            j.moved = True
                            break
                if i.x == 6 and i.y == 7:
                    for j in newWhitePieces:
                        if j.name == 'whiteRook' and j.x == 7 and j.y == 7:
                            j.x = 5
                            j.y = 7
                            j.moved = True
                            break
    
    return newWhitePieces, newBlackPieces
        
'''
def checkmateCheck(newboard, turn, selectedPiece):
    #global board
    global blackPieces
    #global turn
    global whitePieces
    #global selectedPiece

    if turn == -1:
        for i in blackPieces:
            if i.name == 'blackKing':
                if len(pieceLimit(newboard, i.findMoves(newboard, blackPieces, whitePieces), [i.x,i.y], turn*-1)) == 0:
                    return True
        
    elif turn == 1:
        for i in whitePieces:
            if i.name == 'whiteKing':
                if len(pieceLimit(newboard, i.findMoves(newboard, blackPieces, whitePieces), [i.x,i.y], turn*-1)) == 0:
                    return True
    return False
'''

def checkmateCheck2(board, turn, whitePieces, blackPieces, inCheck):
    #As if the player who just made the move says checkmate
    #global blackPieces
    #global whitePieces

    if turn == -1:
        for i in blackPieces:
            currentMoves = i.findMoves(board, blackPieces, whitePieces)
            if i.name == "blackKing":
                currentMoves = copy.deepcopy(addCastle(board, blackPieces, whitePieces, turn, [i.x,i.y], currentMoves))
                currentMoves = pieceLimit(board, currentMoves, [i.x,i.y], turn*-1)
            if inCheck != 0:
                for j in blackPieces:
                    if j.name == "blackKing" and i.name == "blackKing":
                        currentMoves = checkLimit(currentMoves, [i.x, i.y], turn*-1, j.x, j.y, True)
                    elif j.name == "blackKing":
                        currentMoves = checkLimit(currentMoves, [i.x, i.y], turn*-1, j.x, j.y, False)
            if len(currentMoves) > 0:
                return False

    elif turn == 1:
        for i in whitePieces:
            currentMoves = i.findMoves(board, blackPieces, whitePieces)
            if i.name == "whiteKing":
                currentMoves = copy.deepcopy(addCastle(board, blackPieces, whitePieces, turn, [i.x,i.y], currentMoves))
                currentMoves = pieceLimit(board, currentMoves, [i.x,i.y], turn*-1)
            if inCheck != 0:
                for j in whitePieces:
                    if j.name == "whiteKing" and i.name == "whiteKing":
                        currentMoves = checkLimit(currentMoves, [i.x, i.y], turn*-1, j.x, j.y, True)
                    elif j.name == "whiteKing":
                        currentMoves = checkLimit(currentMoves, [i.x, i.y], turn*-1, j.x, j.y, False)
            if len(currentMoves) > 0:
                return False
    return True

def checkCheck(newBoard, turn, kingX, kingY):
    #global board
    global blackPieces
    #global turn
    global whitePieces
    #global inCheck

    if turn == -1:
        for i in whitePieces:
            for j in i.findMoves(newBoard, blackPieces, whitePieces):
                if j[0] == kingX and j[1] == kingY:
                    #print(1)
                    return 1
        
    elif turn == 1:
        for i in blackPieces:
            for j in i.findMoves(newBoard, blackPieces, whitePieces):
                if j[0] == kingX and j[1] == kingY:
                    #print(-1)
                    return -1
    #print(0)
    return 0
    

def checkLimit(possibleMoves, piecePosition, turn, kingX, kingY, isKing):
    global board
    global blackPieces
    global whitePieces
    #global possibleMoves
    notSpots = []

    for i in possibleMoves:
        newBoard = []
        for j in board:
            temp = []
            for x in j:
                temp.append(x)
            newBoard.append(temp)

        copy = 0
        if newBoard[i[0]][i[1]] != turn:
            if turn == -1:
                for j in range(len(blackPieces)):
                    if blackPieces[j].x == i[0] and blackPieces[j].y == i[1]:
                        copy = blackPieces[j]
                        blackPieces.pop(j)
                        break
            elif turn == 1:
                for j in range(len(whitePieces)):
                    if whitePieces[j].x == i[0] and whitePieces[j].y == i[1]:
                        copy = whitePieces[j]
                        whitePieces.pop(j)
                        break

        newBoard[i[0]][i[1]] = turn
        newBoard[piecePosition[0]][piecePosition[1]] = 0
        
        if isKing:
            if checkCheck(newBoard, turn*-1, i[0], i[1]) != 0:
                notSpots.append(i[:2])
        else:
            if checkCheck(newBoard, turn*-1, kingX, kingY) != 0:
                notSpots.append(i[:2])
        
        #print(notSpots)

        if copy != 0:
            if copy.color == -1:
                whitePieces.append(copy)
            if copy.color == 1:
                blackPieces.append(copy)

    updatedPossibleMoves = []
    for i in possibleMoves:
        if [i[0],i[1]] not in notSpots:
            updatedPossibleMoves.append(i)
    return updatedPossibleMoves


def updateBoard():
    global board
    global blackPieces
    global whitePieces

    board = []
    for i in range(8):
        newLine = []
        for j in range(8):
            newLine.append(0)
        board.append(newLine)

    for i in blackPieces:
        board[i.x][i.y] = 1
    for i in whitePieces:
        board[i.x][i.y] = -1

def updateBoard2(blackPieces, whitePieces):
    newBoard = []
    for i in range(8):
        newLine = []
        for j in range(8):
            newLine.append(0)
        newBoard.append(newLine)

    for i in blackPieces:
        newBoard[i.x][i.y] = 1
    for i in whitePieces:
        newBoard[i.x][i.y] = -1
    
    return newBoard


def choosePosition(pos):
    global selectedPiece
    global possibleMoves
    global turn
    global blackPieces
    global whitePieces
    global inCheck
    x = -1
    y = -1
    for i in range(0,8):
        if pos[0] in range(i*100, i*100 + 100):
            x = i
        if pos[1] in range(i*100, i*100 + 100):
            y = i

    if selectedPiece == []:
        if board[x][y] != 0 and turn == board[x][y]:
            selectedPiece = [x,y]
            '''
            if turn == -1:
                for i in whitePieces:
                    if i.x == selectedPiece[0] and i.y == selectedPiece[1]:
                        possibleMoves = i.findMoves(board, blackPieces, whitePieces)
                        if i.name == "whiteKing":
                            possibleMoves = copy.deepcopy(addCastle(board, blackPieces, whitePieces, turn, selectedPiece, possibleMoves))
                            possibleMoves = pieceLimit(board, possibleMoves, selectedPiece, turn)
                            #print(possibleMoves)
                        if inCheck != 0:
                            for j in whitePieces:
                                if j.name == "whiteKing" and i.name == "whiteKing":
                                    possibleMoves = checkLimit(possibleMoves, [i.x, i.y], turn, j.x, j.y, True)
                                elif j.name == "whiteKing":
                                    possibleMoves = checkLimit(possibleMoves, [i.x, i.y], turn, j.x, j.y, False)
            '''    
            if turn == 1:
                for i in blackPieces:
                    if i.x == selectedPiece[0] and i.y == selectedPiece[1]:
                        possibleMoves = i.findMoves(board, blackPieces, whitePieces)
                        if i.name == "blackKing":
                            possibleMoves = copy.deepcopy(addCastle(board, blackPieces, whitePieces, turn, selectedPiece, possibleMoves))
                            possibleMoves = pieceLimit(board, possibleMoves, selectedPiece, turn)
                            #print(possibleMoves)
                        if inCheck != 0:
                            for j in blackPieces:
                                if j.name == "blackKing" and i.name == "blackKing":
                                    possibleMoves = checkLimit(possibleMoves, [i.x, i.y], turn, j.x, j.y, True)
                                elif j.name == "blackKing":
                                    possibleMoves = checkLimit(possibleMoves, [i.x, i.y], turn, j.x, j.y, False)

    else:
        if [x,y] == selectedPiece or ([x,y,False] not in possibleMoves and [x,y,True] not in possibleMoves):
            selectedPiece = []
            possibleMoves = []
            updateBoard()
        elif [x,y,False] in possibleMoves:
            '''
            if turn == -1:
                for i in whitePieces:
                    if i.x == selectedPiece[0] and i.y == selectedPiece[1]:
                        i.x = x
                        i.y = y
                        i.moved = True
                        if i.name == "whiteKing":
                            checkCastle()
                        break
                temp = 0
                for i in blackPieces:
                    if i.name == "blackKing":
                        temp = checkCheck(board[:], turn, i.x, i.y)
                if temp != 0:
                    inCheck = temp
            '''
            if turn == 1:
                for i in blackPieces:
                    if i.x == selectedPiece[0] and i.y == selectedPiece[1]:
                        i.x = x
                        i.y = y
                        i.moved = True
                        if i.name == "blackKing":
                            checkCastle()
                        break
                temp = 0
                for i in whitePieces:
                    if i.name == "whiteKing":
                        temp = checkCheck(board[:], turn, i.x, i.y)
                if temp != 0:
                    inCheck = temp

            
            updateBoard()
            if checkmateCheck2(board, turn, whitePieces, blackPieces, inCheck):
                print("Checkmate")
            #checkCheck()
            selectedPiece = []
            possibleMoves = []
            turn = turn*-1
            
        elif [x,y,True] in possibleMoves:
            '''
            if turn == -1:
                for i in whitePieces:
                    if i.x == selectedPiece[0] and i.y == selectedPiece[1]:
                        i.x = x
                        i.y = y
                        i.moved = True
                        for j in range(len(blackPieces)):
                            if blackPieces[j].x == x and blackPieces[j].y == y:
                                blackPieces.pop(j)
                                break
                        break
                temp = 0
                for i in blackPieces:
                    if i.name == "blackKing":
                        temp = checkCheck(copy.deepcopy(board), turn, i.x, i.y)
                if temp != 0:
                    inCheck = temp
            '''
            if turn == 1:
                for i in blackPieces:
                    if i.x == selectedPiece[0] and i.y == selectedPiece[1]:
                        i.x = x
                        i.y = y
                        i.moved = True
                        for j in range(len(whitePieces)):
                            if whitePieces[j].x == x and whitePieces[j].y == y:
                                whitePieces.pop(j)
                                break
                        break
                temp = 0
                for i in whitePieces:
                    if i.name == "whiteKing":
                        temp = checkCheck(board[:], turn, i.x, i.y)
                if temp != 0:
                    inCheck = temp

            
            updateBoard()
            if checkmateCheck2(board, turn, whitePieces, blackPieces, inCheck):
                print("Checkmate")
            #checkCheck()
            selectedPiece = []
            possibleMoves = []
            turn = turn*-1
    

updateBoard()

while True:

    
    if turn == -1:
        board, whitePieces, blackPieces = aiMoveMax(board, whitePieces, blackPieces, inCheck)

        temp = 0
        for i in blackPieces:
            if i.name == "blackKing":
                temp = checkCheck(board[:], turn, i.x, i.y)
        if temp != 0:
            inCheck = temp

        if checkmateCheck2(board, turn, whitePieces, blackPieces, inCheck):
            print("Checkmate")
        
        turn = turn*-1
    

    '''
    if turn == -1:
        board, whitePieces, blackPieces = aiMoveMax(board, whitePieces, blackPieces, inCheck)

        data = minimax2(board, whitePieces, blackPieces, inCheck, turn, 3, float('-inf'), float('inf'))
        board = copy.deepcopy(data[1])
        whitePieces = copy.deepcopy(data[2])
        blackPieces = copy.deepcopy(data[3])


        for i in board:
            print(i)
        print()

        for i in whitePieces:
            print(i.name)
        print()

        for i in blackPieces:
            print(i.name)
        print()


        temp = 0
        for i in blackPieces:
            if i.name == "blackKing":
                temp = checkCheck(board[:], turn, i.x, i.y)
        if temp != 0:
            inCheck = temp

        if checkmateCheck2(board, turn, whitePieces, blackPieces, inCheck):
            print("Checkmate")
        
        turn = turn*-1
    '''

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if turn == 1:
                choosePosition(pygame.mouse.get_pos())

    screen.fill((0, 0, 0))

    for i in range(0,8,2):
        for j in range(0,8,2):
            pygame.draw.rect(screen, WHITE, (i*100,j*100,100,100))

    for i in range(1,9,2):
        for j in range(1,9,2):
            pygame.draw.rect(screen, WHITE, (i*100,j*100,100,100))

    for i in blackPieces:
        pieceDraw(i)
    for i in whitePieces:
        pieceDraw(i)

    if selectedPiece != []:
        for i in possibleMoves:
            if i[2] == False:
                pygame.draw.rect(screen, BLUE, (i[0]*100, i[1]*100, 100, 100), 3)
            else:
                pygame.draw.rect(screen, RED, (i[0]*100, i[1]*100, 100, 100), 3)

        pygame.draw.rect(screen, GREEN, (selectedPiece[0]*100, selectedPiece[1]*100, 100, 100), 3)

    pygame.display.flip()
    fpsClock.tick(fps)


def inGame():
    setBoard()
    updateBoard()
    global turn
    global inCheck
    global whitePieces
    global blackPieces

    while True:

        if turn == -1:
            board, whitePieces, blackPieces = aiMoveMax(board, whitePieces, blackPieces, inCheck)

            temp = 0
            for i in blackPieces:
                if i.name == "blackKing":
                    temp = checkCheck(board[:], turn, i.x, i.y)
            if temp != 0:
                inCheck = temp

            if checkmateCheck2(board, turn, whitePieces, blackPieces, inCheck):
                print("Checkmate")
            
            turn = turn*-1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if turn == 1:
                    choosePosition(pygame.mouse.get_pos())

        screen.fill((0, 0, 0))

        for i in range(0,8,2):
            for j in range(0,8,2):
                pygame.draw.rect(screen, WHITE, (i*100,j*100,100,100))

        for i in range(1,9,2):
            for j in range(1,9,2):
                pygame.draw.rect(screen, WHITE, (i*100,j*100,100,100))

        for i in blackPieces:
            pieceDraw(i)
        for i in whitePieces:
            pieceDraw(i)

        if selectedPiece != []:
            for i in possibleMoves:
                if i[2] == False:
                    pygame.draw.rect(screen, BLUE, (i[0]*100, i[1]*100, 100, 100), 3)
                else:
                    pygame.draw.rect(screen, RED, (i[0]*100, i[1]*100, 100, 100), 3)

            pygame.draw.rect(screen, GREEN, (selectedPiece[0]*100, selectedPiece[1]*100, 100, 100), 3)

        pygame.display.flip()
        fpsClock.tick(fps)