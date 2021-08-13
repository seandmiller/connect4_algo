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

def define_winner():
  for row in board:
    
      i         = 0
      for element in row:
        
        if element != slot:
          counter   = 0
          the_element = element
          for el in row[i:len(row)]:
            if el != the_element:
              counter = 0
            if el == player_1:
              counter+=1
            
            elif el == player_2:
              counter-=1
            if counter >= 4 or counter <= -4:
            
              return counter          
          i+=1  
  chip_num   = 0
  
  for row in range(len(board[0])): 

   i=-1
   for _ in range(len(board)): 
    for chip in board[i][chip_num]:
      
      if chip != slot:
       z=i
       
       counter_v  = 0
       
       for _ in range(len(board) - abs(z)):
        
        for piece in board[z][chip_num]: 
         
         
         if piece == player_1:
           counter_v+=1
           
        
         elif piece == player_2:
           counter_v-=1
          
         z-=1  
      
        if counter_v >= 4 or counter_v <= -4:
           print("vertical win" ,counter_v)
           return counter_v      
    i-=1
    
    
   chip_num+=1

def ply(t,  choose,tur):
  global turn
  turn = t
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
 
            i-=1
          except:
              i=-1
              game=False
  whose_turn  = "It is Player 1's turn" if turn==False else "It is Player 2's turn"
  global p_turn
  p_turn.config(text=whose_turn)
  if define_winner() == 4:
    p_turn.config(text="Player 1 has won the game")
    end_game()
  elif define_winner() == -4:
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

slot_0.grid(row=1,column=2)
slot_1.grid(row=1,column=3)
slot_2.grid(row=1,column=4)
slot_3.grid(row=2,column=2)
slot_4.grid(row=2,column=3)
slot_5.grid(row=2,column=4)
slot_6.grid(row=3,column=2)

def end_game():
  slot_0.destroy()
  slot_1.destroy()
  slot_2.destroy()
  slot_3.destroy()
  slot_4.destroy()
  slot_5.destroy()
  slot_6.destroy()

window.mainloop()
