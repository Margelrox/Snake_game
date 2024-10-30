import tkinter as tk
import random


class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("snake")
        self.canvas = tk.Canvas(master, width=400, height = 400, bg="black")
        self.canvas.pack()

        self.snake=[(100,100),(90,100),(80,100)]
        self.snake_direction= "Right"
        self.food_position = self.place_food()

        self.score = 0
        self.game_running = True

        self.master.bind("<KeyPress>", self.change_direction)
        self.update()

    def place_food(self):
        x= random.randint(0,39)*10
        y=random.randint(0,39)*10
        return(x,y)
    
    def change_direction(self,event):
        if event.keysym in ["Up","Down","Left","Right"]:
            self.snake_direction = event.keysym

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.snake_direction == "Up":
            new_head = (head_x, head_y-10)
        elif self.snake_direction=="Down":
            new_head=(head_x,head_y + 10)
        elif self.snake_direction=="Left":
            new_head=(head_x-10,head_y)
        elif self.snake_direction=="Right":
            new_head=(head_x+10,head_y)

        else:
            return
        
        self.snake.insert(0, new_head)

        if new_head == self.food_position:
            self.food_position = self.place_food()
            self.score +=1
        else:
            self.snake.pop()

        if self.check_collision(new_head):
            self.game_running=False

    def check_collision(self,head):
        x,y=head
        return(
            x<0 or x>= 400 or 
            y<0 or y>= 400 or
            head in self.snake[1:]


        )
    def draw_elements(self):
        self.canvas.delete("all")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0],segment[1],segment[0]+10, segment[1]+10, fill="green")
            food_x,food_y= self.food_position
            self.canvas.create_oval(food_x, food_y, food_x+10, food_y+10, fill="red")

    def update(self):
        if self.game_running:
            self.move_snake()
            self.draw_elements()
            self.master.after(100,self.update)
        else:
            self.canvas.create_text(200,200,text="Game Over",fill="white",font=("Arial",24))
if __name__=="__main__":
    root=tk.Tk()
    game=SnakeGame(root)
    root.mainloop()