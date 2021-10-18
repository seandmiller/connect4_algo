from tkinter import *
import tkinter.font as font

window    = Tk()

slot      =  "O"
player_1  =  "❅"
player_2  =  "✪"
board     =  [[slot for _ in range(7)] for _ in range(6)]
turn      =  False
font_c4   = font.Font(size=45)

def preview():
  t=1
  for row in board:
      cabinet   = Label(window,text=row)
      cabinet['font'] = font_c4
      cabinet.config(text=row)
      cabinet.grid(row=t,column=1, columnspan=50)
      t+=1
  layout = Label(window,text='0  1  2  3  4  5  6')
  line   = Label(window, text='--------------------------')
  line['font']  = font.Font(size=35)
  line.grid(row=t+1,column=1, columnspan=20)
  layout['font']    =  font.Font(size=35)
  layout.grid(row=t + 2,column=1, columnspan=20)  

p_turn         = Label(window,text="Player 1 Goes First!!!")
p_turn['font'] = font.Font(size=13)
p_turn.grid(row=0,column=0, columnspan=20)
preview()

def define_winner():
 
  for i, row in enumerate(board):
   
    for j, chip in enumerate(row):
        if chip != slot and j + 4 <= len(row):
           if board[i][j:j +4] == [chip for i in range(4)]:
             return chip
        if i + 4 <= len(board) and chip != slot:
           if board[i + 3][j] == chip and board[i + 2][j] == chip:
              if board[i+ 1][j] == chip:
                 return chip
        if i + 4 <= len(board) and j + 4 <= len(row) and chip != slot:
           if board[i+ 3][j+3] == chip and board[i +2][j + 2] == chip:
              if board[i + 1][j + 1]  == chip:
                return chip
        if (i + 4) <= len(board) and (j - 3) >= 0 and chip != slot:
           if board[i + 3][j - 3] == chip and board[i + 2][j- 2] == chip:
              if board[i + 1][j - 1] == chip:
                return chip       

                 

                      
              
            
        

      
      

def ply(t,  choose,tur):
  global turn
  turn = t
  whose_turn  = "It is Player 1's turn" if turn==False else "It is Player 2's turn"
   
  choice  = choose  
  game=True
  i=-1
  while game:
      
      if board[i][choice]==slot:
        board[i][choice]= player_1 if turn==False else player_2
        game = False
        turn = not turn 
      elif i < -5:
        print('slot out')
        game = False
          
      i-=1  

  whose_turn  = "It is Player 1's turn" if turn==False else "It is Player 2's turn"
  global p_turn
  p_turn.config(text=whose_turn)
  if define_winner() == player_1:
    p_turn.config(text="Player 1 has won the game")
    end_game()
  elif define_winner() == player_2:
    end_game()
    p_turn.config(text='Player 2 has won the game')  
  
  preview()
      
slot_0   =  Button(window, text=f"slot - 0",command=lambda: ply(turn, 0,p_turn))
slot_1   =  Button(window,text=f"slot 1",command=lambda: ply(turn,1,p_turn))
slot_2   =  Button(window,text=f"slot 2",command=lambda: ply(turn,2,p_turn))
slot_3   =  Button(window,text=f"slot 3",command=lambda: ply(turn,3,p_turn))
slot_4   =  Button(window,text=f"slot 4",command=lambda: ply(turn,4,p_turn))
slot_5   =  Button(window,text=f"slot 5",command=lambda: ply(turn,5,p_turn))
slot_6   =  Button(window,text=f"slot 6",command=lambda: ply(turn,6,p_turn))

slot_0.grid(row=7,column=2)
slot_1.grid(row=7,column=3 )
slot_2.grid(row=7,column=4)
slot_3.grid(row=7,column=5)
slot_4.grid(row=7,column=6 )
slot_5.grid(row=7,column=7)
slot_6.grid(row=7,column=8)

def end_game():
  slot_0.destroy()
  slot_1.destroy()
  slot_2.destroy()
  slot_3.destroy()
  slot_4.destroy()
  slot_5.destroy()
  slot_6.destroy()

window.mainloop()
