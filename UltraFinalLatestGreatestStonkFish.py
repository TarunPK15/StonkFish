# BIGCHESS
# Note that positions are always given/ taken in the form of list with the first item in the list being the column (1,2,3,) and the second being the row (1,2,3,4...)
import copy
import random
import math
import tkinter as tk
from tkinter import font as tkFont
from functools import partial
import csv
from PIL import Image, ImageTk

class Callback:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs
    def __call__(self):
        self.func(*self.args, **self.kwargs)

def Pawn(pawnType, initialPos, finalPos):
    global n
    if (finalPos[1] - initialPos[1]) == 1:
        if finalPos[0] == initialPos[0] and finalPos not in black.values() and finalPos not in white.values():
            if finalPos[1]==8 or finalPos[1]==1:
                n+=1
                del white[pawnType]
                temp101 = 'WQ'+str(n)
                white[temp101] = finalPos
            else:
                white[pawnType] = finalPos
            return True
        elif finalPos[0] == initialPos[0] - 1 or finalPos[0] == initialPos[0] + 1:
            if finalPos in black.values():
                
                for i in copy.deepcopy(black):
                    
                    if black[i] == finalPos:
                        del black[i]
                if finalPos[1]==8 or finalPos[1]==1:
                    n+=1
                    del white[pawnType]
                    temp101 = 'WQ'+str(n)
                    white[temp101] = finalPos
                else:
                    white[pawnType] = finalPos
                return True
    if initialPos[1] == 2:
        if finalPos[1] - initialPos[1] == 2:
            if finalPos[0] == initialPos[0] and finalPos not in black.values() and finalPos not in white.values() and [
                initialPos[0], initialPos[1] + 1] not in white.values() and [initialPos[0], initialPos[1] + 1] not in black.values():
                white[pawnType] = finalPos
                return True




def Rook(rookType, initialPos, finalPos):
    global black
    # Case 1- Rook goes vertically up
    if initialPos[0] == finalPos[0] and finalPos[1] > initialPos[1]:
        count = 0
        for i in range(initialPos[1] + 1, finalPos[1]):
            if [initialPos[0], i] in white.values() or [initialPos[0], i] in black.values():
                count += 1
        if count == 0:
            if finalPos in black.values():
                delblack = copy.deepcopy(black)
                for i in delblack:
                    if black[i] == finalPos:
                        del black[i]
                white[rookType] = finalPos
                return True
            elif finalPos in white.values():
                return False
            else:
                white[rookType] = finalPos
                return True
    # Case 2- Rook goes vertically down
    elif initialPos[0] == finalPos[0] and initialPos[1] > finalPos[1]:
        count = 0
        for i in range(finalPos[1]+1, initialPos[1]):
            if [initialPos[0], i] in white.values() or [initialPos[0], i] in black.values():
                count += 1
        if count == 0:
            if finalPos in black.values():
                delblack = copy.deepcopy(black)
                for i in delblack:
                    if black[i] == finalPos:
                        del black[i]
                white[rookType] = finalPos
                return True
            elif finalPos in white.values():
                return False
            else:
                white[rookType] = finalPos
                return True
    # Case 3- Rook goes horizontally right
    elif initialPos[1] == finalPos[1] and finalPos[0] > initialPos[0]:
        count = 0
        for i in range(initialPos[0] + 1, finalPos[0]):
            if [i, initialPos[1]] in white.values() or [i, initialPos[1]] in black.values():
                count += 1
        if count == 0:
            if finalPos in black.values():
                delblack = copy.deepcopy(black)
                for i in delblack:
                    if black[i] == finalPos:
                        del black[i]
                white[rookType] = finalPos
                return True
            elif finalPos in white.values():
                return False
            else:
                white[rookType] = finalPos
                return True
    # Case 4- Rook goes horizontally left
    elif initialPos[1] == finalPos[1] and initialPos[0] > finalPos[0]:
        count = 0
        for i in range(finalPos[0]+1, initialPos[0]):
            if [i, initialPos[1]] in white.values() or [i, initialPos[1]] in black.values():
                count += 1
        if count == 0:
            if finalPos in black.values():
                delblack = copy.deepcopy(black)
                for i in delblack:
                    if black[i] == finalPos:
                        del black[i]
                white[rookType] = finalPos
                return True
            elif finalPos in white.values():
                return False
            else:
                white[rookType] = finalPos
                return True


def King(kingType, initialPos, finalPos):
    global countking
    global countrook
    global black
    if (finalPos == [2, 1] or finalPos == [6, 1]) and initialPos == [4, 1]:
        if countking == 0 and countrook == 0:
            if finalPos == [2, 1]:
                if len(BLACKSquareControl([4,1])) == 0:
                    for i in range(2, 4):
                        if [i, 1] in white.values() or [i, 1] in black.values() or len(BLACKSquareControl([i,1])) != 0:
                            return False
                    white["WR1"] = [3, 1]
                    white['WK1'] = [2,1]
                    return True
            elif finalPos == [6, 1]:
                if len(BLACKSquareControl([4,1])) == 0:
                    for i in range(5, 8):
                        if [i, 1] in white.values() or [i, 1] in black.values() or len(BLACKSquareControl([i,1])) != 0:
                            return False
                    white["WR2"] = [5, 1]
                    white['WK1'] = [6,1]
                    return True
                
    if initialPos[0] == finalPos[0] and finalPos[1] - initialPos[1] == 1:
        if finalPos in black.values():
            delblack = copy.deepcopy(black)
            for i in delblack:
                if black[i] == finalPos:
                    del black[i]
            white[kingType] = finalPos
            return True
        elif finalPos in white.values():
            return False
        else:
            white[kingType] = finalPos
            return True
    elif initialPos[0] == finalPos[0] and initialPos[1] - finalPos[1] == 1:
        if finalPos in black.values():
            delblack = copy.deepcopy(black)
            for i in delblack:
                if black[i] == finalPos:
                    del black[i]
            white[kingType] = finalPos
            return True
        elif finalPos in white.values():
            return False
        else:
            white[kingType] = finalPos
            return True
    elif initialPos[1] == finalPos[1] and finalPos[0] - initialPos[0] == 1:
        if finalPos in black.values():
            delblack = copy.deepcopy(black)
            for i in delblack:
                if black[i] == finalPos:
                    del black[i]
            white[kingType] = finalPos
            return True
        elif finalPos in white.values():
            return False
        else:
            white[kingType] = finalPos
            return True
    elif initialPos[1] == finalPos[1] and initialPos[0] - finalPos[0] == 1:
        if finalPos in black.values():
            delblack = copy.deepcopy(black)
            for i in delblack:
                if black[i] == finalPos:
                    del black[i]
            white[kingType] = finalPos
            return True
        elif finalPos in white.values():
            return False
        else:
            white[kingType] = finalPos
            return True
    # Upward
    if finalPos[1] - initialPos[1] == 1:
        # Up-Right
        if finalPos[0] - initialPos[0] == 1:
            if finalPos in black.values():
                delblack = copy.deepcopy(black)
                for i in delblack:
                    if black[i] == finalPos:
                        del black[i]
                white[kingType] = finalPos
                return True
            elif finalPos in white.values():
                return False
            else:
                white[kingType] = finalPos
                return True
        # Up-Left
        elif finalPos[0] - initialPos[0] == (-1):
            if finalPos in black.values():
                delblack = copy.deepcopy(black)
                for i in delblack:
                    if black[i] == finalPos:
                        del black[i]
                black = delblack
                white[kingType] = finalPos
                return True
            elif finalPos in white.values():
                return False
            else:
                white[kingType] = finalPos
                return True
    # Downward
    elif finalPos[1] - initialPos[1] == (-1):
        # Down-Right
        if finalPos[0] - initialPos[0] == 1:
            if finalPos in black.values():
                delblack = copy.deepcopy(black)
                for i in delblack:
                    if black[i] == finalPos:
                        del black[i]
                white[kingType] = finalPos
                return True
            elif finalPos in white.values():
                return False
            else:
                white[kingType] = finalPos
                return True
        # Down-left
        elif finalPos[0] - initialPos[0] == (-1):
            if finalPos in black.values():
                delblack = copy.deepcopy(black)
                for i in delblack:
                    if black[i] == finalPos:
                        del black[i]
                white[kingType] = finalPos
                return True
            elif finalPos in white.values():
                return False
            else:
                white[kingType] = finalPos
                countking += 1
                return True
        # Case 6- Castling
    



def Bishop(bishopType, initialPos, finalPos):
    if finalPos in white.values():
            return False
    # Case where bishop moves up (left or right)
    if finalPos[0] > initialPos[0]:
        # Up-Right
        if finalPos[1] > initialPos[1]:
            if (finalPos[0] - initialPos[0]) / (finalPos[1] - initialPos[1]) == 1:
                y = initialPos[0]
                for i in range(initialPos[1] + 1, finalPos[1]):
                    y += 1
                    if y < 9:
                        if [y,i] in white.values() or [y,i] in black.values():
                            return False
                for i in copy.deepcopy(black):
                    if black[i] == finalPos:
                        del black[i]
                white[bishopType] = finalPos
                return True
        # Up-Left
        elif finalPos[1] < initialPos[1]:
            if (finalPos[0] - initialPos[0]) / (initialPos[1] - finalPos[1]) == 1:
                y = initialPos[0]
                for i in range(initialPos[1] - 1, finalPos[1], -1):
                    y += 1
                    if y < 9:
                        if [y,i] in white.values() or [y,i] in black.values():
                            return False
                for i in copy.deepcopy(black):
                    if black[i] == finalPos:
                        del black[i]
                white[bishopType] = finalPos
                return True
                # Case where bishop moves down (left or right)
    elif finalPos[0] < initialPos[0]:
        # Down-Right
        if finalPos[1] > initialPos[1]:
            if (initialPos[0] - finalPos[0]) / (finalPos[1] - initialPos[1]) == 1:
                y = initialPos[0]
                for i in range(initialPos[1] + 1, finalPos[1]):
                    y = y - 1
                    if y > 0:
                        if [y,i] in white.values() or [y,i] in black.values():
                            return False
                for i in copy.deepcopy(black):
                    if black[i] == finalPos:
                        del black[i]
                white[bishopType] = finalPos
                return True
                # Down-Left
        elif finalPos[1] < initialPos[1]:
            if (initialPos[0] - finalPos[0]) / (initialPos[1] - finalPos[1]) == 1:
                y = initialPos[0]
                for i in range(initialPos[1] - 1, finalPos[1], -1):
                    y = y - 1
                    if y > 0:
                        if [y, i] in white.values() or [y,i] in black.values():
                            return False
                for i in copy.deepcopy(black):
                    if black[i] == finalPos:
                        del black[i]
                white[bishopType] = finalPos
                return True


def Queen(queenType, initialPos, finalPos):
    global white
    global black
    whitecopy = copy.deepcopy(white)
    blackcopy = copy.deepcopy(black)
    if Rook(queenType, initialPos, finalPos) or Bishop(queenType, initialPos, finalPos):
        white = copy.deepcopy(whitecopy)
        black = copy.deepcopy(blackcopy)
        white[queenType] = finalPos
        for i in copy.deepcopy(black):
            if black[i] == finalPos:
                del black[i]
        return True


def Knight(knightType, initialPos, finalPos):
    if finalPos not in white.values():
        # 2 steps up or down
        if finalPos[1] - initialPos[1] == 2 or finalPos[1] - initialPos[1] == -2:
            # Then left
            if finalPos[0] - initialPos[0] == -1:
                for i in (copy.deepcopy(black)).keys():
                    if black[i] == finalPos:
                        del black[i]
                white[knightType] = finalPos
                return True
            # Then right
            elif finalPos[0] - initialPos[0] == 1:
                for i in (copy.deepcopy(black)).keys():
                    if black[i] == finalPos:
                        del black[i]
                white[knightType] = finalPos
                return True
        # 2 steps right or left
        elif finalPos[0] - initialPos[0] == 2 or finalPos[0] - initialPos[0] == -2:
            # Then up
            if finalPos[1] - initialPos[1] == 1:
                for i in (copy.deepcopy(black)).keys():
                    if black[i] == finalPos:
                        del black[i]
                white[knightType] = finalPos
                return True
            # Then down
            if finalPos[1] - initialPos[1] == -1:
                for i in (copy.deepcopy(black)).keys():
                    if black[i] == finalPos:
                        del black[i]
                white[knightType] = finalPos
                return True

def createboard():
    
    global unics
    btns={}
    for x in range(8):
        buttonframe.columnconfigure(x,weight=1)
    for i in range(1,9):
        for j in range(1,9):
            if [i,j] in white.values():
                for x in white:
                    if white[x]==[i,j]:
                        #print(0)
                        for y in unics:
                            if y in x:
                                #print(1)
                                text1=unics[y][0]#tk.PhotoImage(file=unics2[y][1])
            elif [i,j] in black.values():
                for x in black:
                    if black[x]==[i,j]:
                        #print(3)
                        for y in unics:
                            if y in x:
                                #print(4)
                                text1=unics[y][0]#tk.PhotoImage(file=unics2[y][1])
            else:
                text1="\u3164"

            newmove=False
            for new in white:
                if new in white2:
                    if white[new]!=white2[new]:
                        newmove=white[new]
                        
            for old in white2:
                if old in white:
                    if white[old]!=white2[old]:
                        oldmove=white2[old]

            
                        
                        
            if newmove:
                if (i,j)==tuple(newmove):
                    btn=tk.Button(win,text=text1,bg="blanchedalmond",font=v28,command=Callback(findpiece, i,j))
                    btns[btn]=[j,i]
            
                elif (i,j)==tuple(oldmove):
                    btn=tk.Button(win,text=text1,bg="blanchedalmond",font=v28,command=Callback(findpiece, i,j))
                    btns[btn]=[j,i]
                elif (i+j)%2==0:
                    
                    btn=tk.Button(win,text=text1,bg="aliceblue",font=v28,command=Callback(findpiece, i,j))
                    
                    
                    btns[btn]=[j,i]
                    
                else:
                    findpiece1=partial(findpiece,(i,j))
                    btn=tk.Button(win,text=text1,bg="lightsteelblue",font=v28,command=Callback(findpiece, i,j))
                    
                    
                    btns[btn]=[j,i]
            
            else:
                if (i+j)%2==0:
                    
                    btn=tk.Button(win,text=text1,bg="aliceblue",font=v28,command=Callback(findpiece, i,j))
                    
                    
                    btns[btn]=[j,i]
                    
                else:
                    findpiece1=partial(findpiece,(i,j))
                    btn=tk.Button(win,text=text1,bg="lightsteelblue",font=v28,command=Callback(findpiece, i,j))
                    
        
                    btns[btn]=[j,i]

        
    for i in btns:
        if btns[i][0]<10 and btns[i][1]<10:
            i.grid(row=btns[i][0],column=btns[i][1],sticky="WE")

    win.mainloop()

def setb():
    global root
    root.destroy()
    setboard()


def setboard():
    global white
    global black
    global unics
    global win
    global variant_ref
    while variant_ref<16:
        win=tk.Tk()
        v28 = tkFont.Font(family='Arial', size=28)
        win.title("StonkFish Set Chessboard")
        win.geometry("568x640")
        buttonframe=tk.Frame(win)
    
        btns={}
        for x in range(8):
            buttonframe.columnconfigure(x,weight=1)
        for i in range(1,9):
            for j in range(1,9):
                if [i,j] in white.values():
                    for x in white:
                        if white[x]==[i,j]:
                            for y in unics:
                                if y in x:
                                    text1=unics[y][0]
                                    #print("here3")
                                    
                elif [i,j] in black.values():
                    for x in black:
                        if black[x]==[i,j]:
                            for y in unics:
                                if y in x:
                                    text1=unics[y][0]
                                    #print("here4")                    
                                    
                else:
                    text1="\u3164"

                if (i+j)%2==0:
                    
                    btn=tk.Button(win,text=text1,bg="aliceblue",font=v28,command=Callback(update, i,j))
                    
                    btns[btn]=[j,i]
                    
                else:
                    btn=tk.Button(win,text=text1,bg="lightsteelblue",font=v28,command=Callback(update, i,j))
                    
                    
                    btns[btn]=[j,i]
        txtlab=tk.Label(win,text="Set the position of: {}".format(vardict[variant_ref]),font=v28)
                
        for i in btns:
            i.grid(row=btns[i][0],column=btns[i][1],sticky="WE")

        txtlab.place(x=0,y=592)

        win.mainloop()
    else:
        #print("here8")
        covercode()


def update(i,j):
    global variant_ref
    global vardict
    global black
    global white
    global win
    win.destroy()
    if variant_ref%2==1 and [i,j] not in white.values() and [i,j] not in black.values() and j>6:
        white[vardict[variant_ref]]=[i,j]
        variant_ref+=1
        #print("hereeee1")
        #print(white)
    elif variant_ref%2==0 and [i,j] not in white.values() and [i,j] not in black.values() and j<3:
        black[vardict[variant_ref]]=[i,j]
        variant_ref+=1
        #print("hereeeee")
        #print(black)
    return setboard()

def PieceMovement(piece_notation, finalPos):
    # This function allows you to automatically pass the notation of a piece, along with the final position, and it will detect which piece type it is and accordingly perform the function of that piece as defined.
    # This will be useful for for loop iteration and also for when we input values from the user
    if piece_notation[1] == 'P' and piece_notation[0] == 'W':
        if Pawn(piece_notation, white[piece_notation], finalPos) == True:
            return True
        else:
            return False
    elif piece_notation[1] == 'Q' and piece_notation[0] == 'W':
        if Queen(piece_notation, white[piece_notation], finalPos):
            return True
        else:
            return False
    elif piece_notation[1] == 'R' and piece_notation[0] == 'W':
        if Rook(piece_notation, white[piece_notation], finalPos):
            return True
        else:
            return False
    elif piece_notation[1] == 'N' and piece_notation[0] == 'W':
        if Knight(piece_notation, white[piece_notation], finalPos):
            return True
        else:
            return False
    elif piece_notation[1] == 'B' and piece_notation[0] == 'W':
        if Bishop(piece_notation, white[piece_notation], finalPos):
            return True
        else:
            return False
    elif piece_notation[1] == 'K' and piece_notation[0] == 'W':
        if King(piece_notation, white[piece_notation], finalPos) == True:
            return True
        else:
            return False
    elif piece_notation[0] == 'B':
        if UserMove(piece_notation, finalPos) == True:
            black[piece_notation] = finalPos
            for i in tuple(white):
                if white[i] == finalPos:
                    if i == 'WK1':
                        break
                    del white[i]
                    break
            return True
        else:
            return False

def WHITESquareControl(sqr):
    global white
    global black
    squareControlList = []
    blackcopy = copy.deepcopy(black)
    blackcopy2 = copy.deepcopy(black)
    whitecopy2 = copy.deepcopy(white)
    whitecopy = copy.deepcopy(white)
    black['dummypiece'] = sqr
    blackcopy['dummypiece'] = sqr
    for i in tuple(white):
        if white[i] == sqr:
            del white[i]
            del whitecopy[i]

    for i in whitecopy:
        if PieceMovement(i, sqr):
            squareControlList.append(i)
            black = copy.deepcopy(blackcopy)
            white = copy.deepcopy(whitecopy)
            black['dummypiece'] = sqr
    if 'dummypiece' in blackcopy:
        del blackcopy['dummypiece']

    white = copy.deepcopy(whitecopy2)
    black = copy.deepcopy(blackcopy2)
    return squareControlList

def BLACKSquareControl(sqr):
    global white
    global black
    global Megalist
    MegalistCopy = copy.deepcopy(Megalist)
    blackcopy2 = copy.deepcopy(black)
    whitecopy2 = copy.deepcopy(white)

    l1 = []
    whiteDuplicate = copy.deepcopy(black)
    d1 = {}
    for i in whiteDuplicate:
        key = 'W' + i[1] + i[2]
        val = [whiteDuplicate[i][0], 9 - whiteDuplicate[i][1]]
        d1[key] = val
    blackDuplicate = copy.deepcopy(white)
    d2 = {}
    for i in blackDuplicate:
        key = 'B' + i[1] + i[2]
        val = [blackDuplicate[i][0], 9 - blackDuplicate[i][1]]
        d2[key] = val
    try:
        sqr = [sqr[0], 9 - sqr[1]]
    except:
        global playerwin
        Megalist = []
        playerwin = True
        playerwins()


    black = copy.deepcopy(d2)
    white = copy.deepcopy(d1)

    for i in tuple(white):
        if white[i] == sqr:
            del white[i]
    
    for i in tuple(white):
        black['dummypiece'] = sqr
        if PieceMovement(i, sqr):
            l1.append(i)
            white = copy.deepcopy(d1)
            black = copy.deepcopy(d2)
    if 'dummypiece' in black:
        del black['dummypiece']
    squareControlList = []

    for i in l1:
        val = 'B' + i[1] + i[2]
        squareControlList.append(val)

    white = copy.deepcopy(whitecopy2)
    black = copy.deepcopy(blackcopy2)
    Megalist = copy.deepcopy(MegalistCopy)
    sqr[1] = 9 - sqr[1]
    return squareControlList


def anotherGoodMove(piece_notation, finalPos):
        global white
        global black
        global w123
        global b123
        global movecounter
        whiteDuplicate2 = copy.deepcopy(white)
        blackDuplicate2 = copy.deepcopy(black)
        netGain = 0
        worksout2=False
        whitePieces = WHITESquareControl(finalPos)
        for i in black:
            if black[i] == finalPos:
                worksout = True
                netGain += notation[i[1]][1]
                break
            else:
                worksout = False
        PieceMovement(piece_notation, finalPos)
        if 'BK1' in black:
            if piece_notation in WHITESquareControl(black['BK1']):
                worksout2=True
        l1 = []
        depth = 0
        flagvar = False
        while True:
            depth += 1
            #BLACK's Move
            blackPieces = BLACKSquareControl(finalPos)
            
            if len(blackPieces) == 0:
                if netGain < 0:
                    flagvar = True
                    break
                else:
                    l1.append(netGain)
                    break
            blackPieceValue = []
            for i in blackPieces:
                blackPieceValue.append(notation[i[1]][1])
            temp1 = blackPieceValue.index(min(blackPieceValue))
            for i in tuple(white):
                if white[i] == finalPos:
                    del white[i]
            black[blackPieces[temp1]] = finalPos
            netGain -= notation[piece_notation[1]][1]
            if netGain >= 0:
                l1.append(netGain)
            #WHITE's Move
            whitePieces = WHITESquareControl(finalPos)
            if len(whitePieces) == 0:
                if netGain < 0:
                    flagvar = True
                    break
                else:
                    break
            else:
                whitePieceValue = []
                for i in whitePieces:
                    whitePieceValue.append(notation[i[1]][1])
                temp1 = whitePieceValue.index(min(whitePieceValue))
                PieceMovement(whitePieces[temp1], finalPos)
                netGain += notation[piece_notation[1]][1]
            if netGain < 0:
                Megalist.remove((piece_notation, finalPos))
                break

        white = copy.deepcopy(whiteDuplicate2)
        black = copy.deepcopy(blackDuplicate2)

        if not flagvar:
            netGain = min(l1)

        if worksout:
            netGain += 0.01

        if piece_notation[1]=="K":
            if movecounter < 15:
                netGain -= 0.01

        if movecounter < 8:
            if (piece_notation, finalPos) == ('WP5',[5,4]) or (piece_notation, finalPos) == ('WP4',[4,4]):
                netGain += 0.1

        if piece_notation[1] == 'R':
            if movecounter < 15:
                netGain -= 0.01

        if piece_notation[1] == 'P' or piece_notation[1] == 'K':
            if movecounter > 35:
                netGain += 0.001

        if piece_notation[1] == 'K':
            if finalPos == [2,1]:
                if white[piece_notation] == [4,1]:
                    netGain += 0.5
            if finalPos == [6,1]:
                if white[piece_notation] == [4,1]:
                    netGain += 0.4

        if piece_notation[1] == "B" or piece_notation[1] == "N":
            if white[piece_notation] == w123[piece_notation]:
                netGain += 0.09

        if worksout2:
            if movecounter>15:
                netGain+=0.9
            elif movecounter>25:
                netGain+=1
            else:
                netGain+=0.1
        
        
        #print("\nAnother good move determines", piece_notation, finalPos, netGain) 
        return netGain

def HangingPiece(piece_notation, finalPos):
    global white
    global black
    global Megalist
    #print("HANGING PIECE")
    temp20 = 0
    for i in black:
        if black[i] == finalPos:
            temp20 += notation[i[1]][1]
    PieceMovement(piece_notation,finalPos)
    
    
    MegalistCopy = copy.deepcopy(Megalist)
    blackcopy2 = copy.deepcopy(black)
    whitecopy2 = copy.deepcopy(white)

    l1 = []
    whiteDuplicate = copy.deepcopy(black)
    d1 = {}
    for i in whiteDuplicate:
        key = 'W' + i[1] + i[2]
        val = [whiteDuplicate[i][0], 9 - whiteDuplicate[i][1]]
        d1[key] = val
    blackDuplicate = copy.deepcopy(white)
    d2 = {}
    for i in blackDuplicate:
        key = 'B' + i[1] + i[2]
        val = [blackDuplicate[i][0], 9 - blackDuplicate[i][1]]
        d2[key] = val

    black = copy.deepcopy(d2)
    white = copy.deepcopy(d1)
    

    #Creating Black Megalist

    BMegalist = []
    for i in tuple(white):
        for j in range(1, 9):
            for k in range(1, 9):
                if PieceMovement(i, [j, k]) == True:
                    white = copy.deepcopy(d1)
                    black = copy.deepcopy(d2)
                    netGain = anotherGoodMove(i,[j,k])
                    if netGain < 1: #or [j,9-k]==finalPos:
                        netGain = 0
                    BMegalist.append((i, [j, k], netGain))
                    white = copy.deepcopy(d1)
                    black = copy.deepcopy(d2)

    t1 = []
    for i in BMegalist:
        t1.append(i[2])

    netLoss = max(t1) - temp20

    white = copy.deepcopy(whitecopy2)
    black = copy.deepcopy(blackcopy2)
    Megalist = copy.deepcopy(MegalistCopy)

    return netLoss


def leads():
    global root
    root.destroy()
    fh=open('players.csv','r')
    fh.seek(0)
    csvr=csv.reader(fh)
    
    main=tk.Tk()
    v11 = tkFont.Font(family='Arial', size=11)
    main.title("StonkFish Scoreboard")
    main.geometry("532x592")
    frm=tk.Frame(main)
    
    listcsv=[]
    for i in csvr:
        listcsv.append(i)
    fh.close()
    for x in range(len(listcsv)):
        frm.columnconfigure(x,weight=1)
    for i in range(len(listcsv)):
        for j in range(len(listcsv[i])):
            if i==0:
                text=tk.Label(text=listcsv[i][j],font=v11,bg='Yellow')
                text.grid(row=i,column=j,sticky="WE")
            else:
                text=tk.Label(text=listcsv[i][j],font=v11)
                text.grid(row=i,column=j,sticky="WE")
    main.mainloop()

countrook = 0
countking = 0
Hcountrook = 0
Hcountking = 0

def updateusername():
    global txtin
    global usrn
    global usrpop
    usrn=txtin.get(1.0,"end-1c")
    if usrn=="":
        usrpop.destroy()
        takeusername()
    else:
        usrpop.destroy()
        usrn=usrn[:21]
        return usrn
    
def exitnow():
    exit(0)

def takeusername():
    global root
    global usrpop
    global txtin
    root.destroy()
    usrpop=tk.Tk()
    usrpop.title("Username")
    usrpop.geometry("400x400")
    txt1=tk.Label(usrpop,text="Enter your username:")
    txtin=tk.Text(usrpop,height=5,width=20)
    btnin=tk.Button(usrpop,text="Confirm",command=Callback(updateusername))
    txt1.pack()
    txtin.pack()
    btnin.pack()

def updatecsv():
    global playerwin
    flagxyz=False
    fcsv=open('players.csv','r')
    csvr=csv.reader(fcsv)
    for i in csvr:
        if i!=[]:
            if i[0]==usrn:
                
                flagxyz=True
    fcsv.seek(0)
    if flagxyz:
        for i in csvr:
            if i!=[]:
                if i[0]==usrn:
                    
                    Game_num= int(i[1])
                    Wins= int(i[2])
                    Total_moves=int(i[4])
    else:
        Game_num=0
        Wins=0
        Total_moves=0
    randlst=[]
    fcsv.seek(0)
    for i in csvr:
        if i!=[]:
            if usrn not in i and i[0]!="Username":
                randlst.append(i)
    Game_num+=1
    if playerwin:
        Wins+=1
    Total_moves+=movecounter
    Avg_moves=round((Total_moves/Game_num),2)
    x=[usrn,Game_num,Wins,Avg_moves,Total_moves]
    randlst.append(x)
    x2=["Username","Number_of_Games","Wins","Moves_Avg","Moves_Total"]
    fcsv.close()
    fcsv2=open('players.csv','w')
    csvw=csv.writer(fcsv2)
    csvw.writerow(x2)
    csvw.writerows(randlst)
    fcsv2.close()
            
def helpfun():
    ftext=open("helptext.txt","r")
    content = ftext.read()
    ftext.close()
    global root
    root.destroy()
    window=tk.Tk()
    window.geometry("800x400")
    window.title("Help")
    v15 = tkFont.Font(family='Arial', size=15)
    txt_help=tk.Label(window,text=content,font=v15)
    txt_help.pack()

    
def menu(): #main
    global root
    global usrn
    root=tk.Tk()
    v28 = tkFont.Font(family='Arial', size=28)
    v15 = tkFont.Font(family='Arial', size=15)
    root.title("StonkFish Menu")
    root.geometry("568x592")

    text_wlcm=tk.Label(root,text="Welcome to... \nStonkFish!\n",font=v28)
    loadimg = Image.open("stonkfish_logo.png")
    renderimg = ImageTk.PhotoImage(loadimg)
    img = tk.Label(root, image=renderimg)
    btn_usrn= tk.Button(root,text="Change User",font=v15,command=Callback(takeusername))
    btn_lb= tk.Button(root,text='Scoreboard',font=v15,command= Callback(leads))
    btn_play= tk.Button(root,text='Start Standard Chess Match',font=v15,command= Callback(play))
    btn_variant= tk.Button(root,text='Start Variant Chess Match',font=v15,command= Callback(setb))
    btn_exit= tk.Button(root,text='Exit',font=v15,command= Callback(exitnow))
    txt_user=tk.Label(root,text="User: {}\n".format(usrn),font=v15)
    btn_about= tk.Button(root,text='Help',font=v15,command= Callback(helpfun))
    
    text_wlcm.pack()
    txt_user.pack()
    btn_lb.pack()
    btn_usrn.pack()
    btn_play.pack()
    btn_variant.pack()
    btn_about.pack()
    btn_exit.pack()
    img.pack()
    
    root.mainloop()

def findpiece(i,j):
    global randooo
    if randooo==0:
        win.destroy()
    elif randooo==1:
        global bref
        global bpos
        if not bref:
            if [i,j] in black.values():
                for piece in black.keys():
                    if black[piece]==[i,j]:
                        bref=piece
            else:
                bref="lol"
            randooo=2
            win.destroy()
            
    else:
        bpos=[i,j]
        win.destroy()
        
# Initial State
unics = {'WP': ["\u2659",r"D:\Tarun\Class 11\Computer\Projects\WPawn.png"],
         'BP': ["\u265F",r"D:\Tarun\Class 11\Computer\Projects\BPawn.png"],
         'WR': ["\u2656",r"D:\Tarun\Class 11\Computer\Projects\WRook.png"],
         'BR': ["\u265C",r"D:\Tarun\Class 11\Computer\Projects\BRook.png"],
         'WN': ["\u2658",r"D:\Tarun\Class 11\Computer\Projects\WKnight.png"],
         'BN': ["\u265E",r"D:\Tarun\Class 11\Computer\Projects\BKnight.png"],
         'WB': ["\u2657",r"D:\Tarun\Class 11\Computer\Projects\WBishop.png"],
         'BB': ["\u265D",r"D:\Tarun\Class 11\Computer\Projects\BBishop.png"],
         'WQ': ["\u2655",r"D:\Tarun\Class 11\Computer\Projects\WQueen.png"],
         'BQ': ["\u265B",r"D:\Tarun\Class 11\Computer\Projects\BQueen.png"],
         'WK': ["\u2654",r"D:\Tarun\Class 11\Computer\Projects\WKing.png"],
         'BK': ["\u265A",r"D:\Tarun\Class 11\Computer\Projects\BKing.png"]}

white={}
black={}
variant_ref=0
root = 1
vardict={1:'WK1',
         0:'BK1',
         3:'WQ1',
         2:'BQ1',
         5:'WN1',
         4:'BN1',
         7:'WN2',
         6:'BN2',
         9:'WB1',
         8:'BB1',
         11:'WB2',
         10:'BB2',
         13:'WR1',
         12:'BR1',
         15:'WR2',
         14:'BR2'}



def play():
    global white
    global black
    global root
    root.destroy()
    white = {
        'WP1': [1, 2],
        'WP2': [2, 2],
        'WP3': [3, 2],
        'WP4': [4, 2],
        'WP5': [5, 2],
        'WP6': [6, 2],
        'WP7': [7, 2],
        'WP8': [8, 2],
        'WR1': [1, 1],
        'WR2': [8, 1],
        'WN1': [2, 1],
        'WN2': [7, 1],
        'WB1': [3, 1],
        'WB2': [6, 1],
        'WQ1': [5, 1],
        'WK1': [4, 1]
    }

    black = {
        'BP1': [1, 7],
        'BP2': [2, 7],
        'BP3': [3, 7],
        'BP4': [4, 7],
        'BP5': [5, 7],
        'BP6': [6, 7],
        'BP7': [7, 7],
        'BP8': [8, 7],
        'BR1': [1, 8],
        'BR2': [8, 8],
        'BN1': [2, 8],
        'BN2': [7, 8],
        'BB1': [3, 8],
        'BB2': [6, 8],
        'BQ1': [5, 8],
        'BK1': [4, 8]
    }
    covercode()

notation = {
    'P': ['Pawn', 1],
    'R': ['Rook', 5],
    'N': ['Knight', 3],
    'B': ['Bishop', 3],
    'Q': ['Queen', 9],
    'K': ['King',1000000000]
}

# Important information for looping
rows = [1, 2, 3, 4, 5, 6, 7, 8]
columns = [1, 2, 3, 4, 5, 6, 7, 8]
n = 1


def UserMove(piece_notation,finalPos):
    global Hcountrook
    global Hcountking
    global white
    global black
    global Megalist
    global n
    global flagv
    initialPos = black[piece_notation]

    if finalPos[1]==1 and piece_notation[1]=="P":
        flagv=True
        n+=1
        del black[piece_notation]
        promo_temp = 'BQ'+str(n)
        black[promo_temp] = finalPos

    
    elif piece_notation[1]=="K" and (finalPos == [2, 8] or finalPos == [6, 8]) and initialPos == [4, 8]:
        if Hcountking == 0 and Hcountrook == 0:
            if finalPos == [2, 8]:
                if len(WHITESquareControl([4,8])) == 0:
                    for i in range(2, 4):
                        if [i, 8] in white.values() or [i, 8] in black.values() or len(WHITESquareControl([i,8])) != 0:
                            return False
                    black["BR1"] = [3,8]
                    black['BK1'] = [2,8]
                    return True

            elif finalPos == [6, 8]:
                if len(WHITESquareControl([4,8])) == 0:
                    for i in range(5, 7):
                        if [i, 8] in white.values() or [i, 8] in black.values() or len(WHITESquareControl([i,8])) != 0:
                            return False
                    black["BR2"] = [5,8]
                    black['BK1'] = [6,8]
                    return True

    else:       
        MegalistCopy = copy.deepcopy(Megalist)
        blackcopy2 = copy.deepcopy(black)
        whitecopy2 = copy.deepcopy(white)

        l1 = []
        whiteDuplicate = copy.deepcopy(black)
        d1 = {}
        for i in whiteDuplicate:
            key = 'W' + i[1] + i[2]
            val = [whiteDuplicate[i][0], 9 - whiteDuplicate[i][1]]
            d1[key] = val
        blackDuplicate = copy.deepcopy(white)
        d2 = {}
        for i in blackDuplicate:
            key = 'B' + i[1] + i[2]
            val = [blackDuplicate[i][0], 9 - blackDuplicate[i][1]]
            d2[key] = val
        
        black = copy.deepcopy(d2)
        white = copy.deepcopy(d1)
        finalPosDuplicate = finalPos
        finalPos = [finalPos[0], 9-finalPos[1]]
        piece_notationDuplicate = piece_notation
        piece_notation = 'W' + piece_notation[1] + piece_notation[2]
        if PieceMovement(piece_notation,finalPos) == True:
            var = True
        else:
            var = False

        white = copy.deepcopy(whitecopy2)
        black = copy.deepcopy(blackcopy2)
        finalPos = finalPosDuplicate
        piece_notation = piece_notationDuplicate
        Megalist = copy.deepcopy(MegalistCopy)

        return var


def checkorstale():
    if Megalist == []:
        if inCheck():
            return "Checkmate"
        else:
            return "Stalemate"

def inCheck():
    if len(BLACKSquareControl(white['WK1'])) != 0:
        return True

def HinCheck():
    if len(BLACKSquareControl(white['WK1'])) != 0:
        return True

def Check():
    global white
    global black
    global Megalist
    if inCheck():
        wc = copy.deepcopy(white)
        bc = copy.deepcopy(black)
        for i in Megalist:
            PieceMovement(i[0],i[1])
            if inCheck():
                Megalist.remove(i)
            white = copy.deepcopy(wc)
            black = copy.deepcopy(bc)
        white = copy.deepcopy(wc)
        black = copy.deepcopy(bc)

def playerwins():
    global win
    global playerwin
    playerwin = True
    updatecsv()
    if 'WK1' in white:
        del white['WK1']

def CompWon():
    global white
    global black
    global Megalist
    MegalistCopy = copy.deepcopy(Megalist)
    blackcopy2 = copy.deepcopy(black)
    whitecopy2 = copy.deepcopy(white)

    l1 = []
    whiteDuplicate = copy.deepcopy(black)
    d1 = {}
    for i in whiteDuplicate:
        key = 'W' + i[1] + i[2]
        val = [whiteDuplicate[i][0], 9 - whiteDuplicate[i][1]]
        d1[key] = val
    blackDuplicate = copy.deepcopy(white)
    d2 = {}
    for i in blackDuplicate:
        key = 'B' + i[1] + i[2]
        val = [blackDuplicate[i][0], 9 - blackDuplicate[i][1]]
        d2[key] = val

    black = copy.deepcopy(d2)
    white = copy.deepcopy(d1)
    

    #Creating Black Megalist

    BMegalist = []
    for i in white:
        for j in range(1, 9):
            for k in range(1, 9):
                if PieceMovement(i, [j, k]) == True:
                    white = copy.deepcopy(d1)
                    black = copy.deepcopy(d2)
                    netGain = anotherGoodMove(i,[j,k])
                    try:
                        if netGain < 1 or [j,9-k] == finalPos:
                            netGain = 0
                    except:
                        playerwins()
                    BMegalist.append((i, [j, k], netGain))
                    white = copy.deepcopy(d1)
                    black = copy.deepcopy(d2)

    if HinCheck():
        wc = copy.deepcopy(white)
        bc = copy.deepcopy(black)
        for i in BMegalist:
            PieceMovement(i[0],i[1])
            if HinCheck():
                BMegalist.remove(i)
            white = copy.deepcopy(wc)
            black = copy.deepcopy(bc)
        white = copy.deepcopy(wc)
        black = copy.deepcopy(bc)
        
    if Megalist == []:
        print("Game Over")
        if BLACKSquareControl(white['WK1']) != 0:
            print("Checkmate, you won")
            closing=tk.Tk()
            closing.geometry("200x100")
            closing.title("Result")
            v28 = tkFont.Font(family='Arial', size=28)
            t1=tk.Label(text="You Won",font=v28)
            t1.pack()
        else:
            print("Stalemate, it is a draw")
            closing=tk.Tk()
            closing.geometry("200x100")
            closing.title("Result")
            v28 = tkFont.Font(family='Arial', size=28)
            t1=tk.Label(text="Match Drawn",font=v28)
            t1.pack()
        return True

    return False

def stalemate():
    global playerwin
    playerwin = False
    updatecsv()
    if 'WK1' in white:
        del white['WK1']
    


# Cover code
def checkmate():
    if 'BK1' not in black or 'WK1' not in white:
        return False
    else:
        return True

w123 = None
b123 = None
# We need to replace endgame with checkmate or stalemate
def covercode():
    global white
    global playerwin
    global countrook
    global countking
    global Hcountrook
    global Hcountking
    global black
    global Megalist
    global superlist
    global buttonframe
    global win
    global white2
    global v28
    global randooo
    global bref
    global bpos
    global movecounter
    global w123
    global b123
    w123 = copy.deepcopy(white)
    b123 = copy.deepcopy(black)
    
    endgame = 'n'
    #print(white)
    #print(black)
    while checkmate():
        
        
        # Megalist
        Megalist = []
        superlist = []
        whiteDuplicate123 = copy.deepcopy(white)
        blackDuplicate123 = copy.deepcopy(black)
        Megalist = []

        for i in white:
            for j in range(1, 9):
                for k in range(1, 9):
                    if PieceMovement(i, [j, k]) == True:
                        Megalist.append((i, [j, k]))
                        white = copy.deepcopy(whiteDuplicate123)
                        black = copy.deepcopy(blackDuplicate123)

        Check()
        white = copy.deepcopy(whiteDuplicate123)
        black = copy.deepcopy(blackDuplicate123)
        
        Megalistcopy = []
        maxval = -10000000
        if Megalist != []:
            #print("\n\n")
            for i in Megalist:
                #print("THE MOVE ANALYSING RIGHT NOW IS: ", i)
                tempvar1 = anotherGoodMove(i[0],i[1])
                if tempvar1 < 0:
                    s = round(tempvar1)
                    tempvar1 = s + tempvar1
                
                white = copy.deepcopy(whiteDuplicate123)
                #print("white: ", white)
                #print()
                black = copy.deepcopy(blackDuplicate123)
                #print("black", black)
                tempvar2 = HangingPiece(i[0],i[1])
                white = copy.deepcopy(whiteDuplicate123)
                black = copy.deepcopy(blackDuplicate123)
                tempvar = tempvar1 - tempvar2
                if maxval < tempvar:
                    maxval = tempvar
                Megalistcopy.append((i[0],i[1],tempvar))
                #if tempvar1 != 0 or tempvar2 != 0:
                #print(i, tempvar, "anothergoodmove: ", tempvar1, "hangingpieces: ", tempvar2)

            Megalist = copy.deepcopy(Megalistcopy)
            #print("\nMegalist: ", Megalistcopy)
            
            finalchoice = []
            for j in Megalist:
                if j[2] == maxval:
                    finalchoice.append(j)
            white2=copy.deepcopy(white)
            #print(finalchoice)
                
            if finalchoice!=[]:   
                temp1 = random.choice(finalchoice)
            else:
                print("Stalemate")
                stalemate()
                break
                
            '''
            randooo=0
            win=tk.Tk()
            bref=False
            v28 = tkFont.Font(family='Arial', size=28)
            win.title("StonkFish Chessboard")
            win.geometry("568x592")
            buttonframe=tk.Frame(win)
            createboard()
            '''

            
            PieceMovement(temp1[0],temp1[1])
            print()

            if temp1[0][1] == "R":
                countrook+=1
            if temp1[0][1] == "K":
                countrook+=1
            '''      
            print("White's Move:",temp1)
            print()
            print("Megalist: ", Megalist)
            print()
            print("Superlist: ", finalchoice)
            print()
            print("original white",white)
            print("original black",black)'''

        elif CompWon():
            break
        elif 'WK1' not in white or 'BK1' not in black:
            if 'WK1' not in white:
                print("You lost the game")
            elif 'BK1' not in black:
                print("You won the game")
        else:
            if checkorstale() == "Checkmate":
                print("Checkmate! You won the game.")
                break

            else:
                print("Stalemate! The game is a draw.")
                break
        '''else:
        if 'BK1' not in black:
            print("L's were taken")
        elif 'WK1' not in white:
        print("Big W")'''

        #Movecoutner
        
        print()
        #BLACK's move
        while checkmate():
            randooo=1
            bref=False
            bpos=False
            win=tk.Tk()
            v28 = tkFont.Font(family='Arial', size=28)
            win.title("StonkFish Chessboard")
            win.geometry("568x592")
            buttonframe=tk.Frame(win)
            createboard()
            
            blacksMove =  bref 
            if blacksMove == "resign":
                break
            win=tk.Tk()
            v28 = tkFont.Font(family='Arial', size=28)
            win.title("StonkFish Chessboard")
            win.geometry("568x592")
            buttonframe=tk.Frame(win)
            createboard()
            
            moveTo = bpos
            
            if blacksMove in black:
                if PieceMovement(blacksMove, moveTo) or flagv:
                    movecounter += 1
                    if blacksMove[1] == "R":
                        Hcountrook+=1
                    if blacksMove[1] == "K":
                        Hcountrook+=1
                    break
                else:
                    print("Invalid move")   
            else:
                print("Invalid move, please re-type a move")
        else:
            if 'BK1' not in black:
                closing=tk.Tk()
                closing.geometry("200x100")
                closing.title("Result")
                v28 = tkFont.Font(family='Arial', size=28)
                t1=tk.Label(text="You Lost",font=v28)
                t1.pack()
                playerwin=False
                updatecsv()
            elif 'WK1' not in white:
                closing=tk.Tk()
                closing.geometry("200x100")
                closing.title("Result")
                v28 = tkFont.Font(family='Arial', size=28)
                t1=tk.Label(text="You Won",font=v28)
                t1.pack()

usrn="anonymous"
movecounter=0
moveTo = None
blacksMove = None
flagv=False

while True:
    white={}
    black={}
    movecounter=0
    countrook=0
    countking=0
    Hcountrook = 0
    Hcountking = 0
    n = 1
    menu()
