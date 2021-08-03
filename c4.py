from tkinter import *
import tkinter.font as font

window    = Tk()


slot      =  "O"
player_1  =  "❅"
player_2  =  "✪"
board     =  [[slot for _ in range(7)] for _ in range(6)]
turn      =  False
font_c4   = font.Font(size=25)

def preview():
  t=1
  for row in board:
      cabinet   = Label(window,text=row)
      cabinet['font'] = font_c4
      cabinet.config(text=row)
      cabinet.grid(row=t,column=1)
      t+=1

p_turn         = Label(window,text="Player 1 Goes First!!!")
p_turn['font'] = font.Font(size=13)
p_turn.grid(row=0,column=1)
preview()
def ply(t,  choose,tur):
  global turn
  turn = t
  print(choose)

  whose_turn  = "It is Player 1's turn" if turn==False else "It is Player 2's turn"
  

    
  choice  = choose  
    
  if choice!=None:
      game=True
      i=-1
      while game:
          try:
            if board[i][choice]==slot:
                board[i][choice]= player_1 if turn==False else player_2
                game=False
                turn = not turn
                print(turn) 
 
            i-=1
          except:
              print(choose)
              i=-1
              game=False
  whose_turn  = "It is Player 1's turn" if turn==False else "It is Player 2's turn"
  global p_turn
  p_turn.config(text=whose_turn)
  
  preview()
      


slot_0   =  Button(window, text=f"slot - 0",command=lambda: ply(turn, 0,p_turn)).grid(row=1,column=2)
slot_1   =  Button(window,text=f"slot 1",command=lambda: ply(turn,1,p_turn)).grid(row=1,column=3)
slot_2   =  Button(window,text=f"slot 2",command=lambda: ply(turn,2,p_turn)).grid(row=1,column=4)
slot_3   =  Button(window,text=f"slot 3",command=lambda: ply(turn,3,p_turn)).grid(row=2,column=2)
slot_4   =  Button(window,text=f"slot 4",command=lambda: ply(turn,4,p_turn)).grid(row=2,column=3)
slot_5   =  Button(window,text=f"slot 5",command=lambda: ply(turn,5,p_turn)).grid(row=2,column=4)
slot_6   =  Button(window,text=f"slot 6",command=lambda: ply(turn,6,p_turn)).grid(row=3,column=2)








window.mainloop()
