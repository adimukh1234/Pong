from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


sc= Screen()
sc.bgcolor("black")
sc.setup(width=800,height=600)
sc.title("PONG")
sc.tracer(0)

l_pd= Paddle((-350,0))
r_pd= Paddle((350,0))
ball1= Ball()
score= Scoreboard()



sc.listen() 
sc.onkey(r_pd.go_up, "Up")
sc.onkey(r_pd.go_down, "Down")
sc.onkey(l_pd.go_up, "w")
sc.onkey(l_pd.go_down, "s")


game_on = True

while game_on:
    time.sleep(ball1.movespeed)
    sc.update()
    ball1.move()

    #detect collission with wall
    if ball1.ycor() > 275 or ball1.ycor() < -275:
        ball1.bounce_y() 

    #detect collission with paddle
    if ball1.distance(r_pd) < 50 and ball1.xcor() > 320 or ball1.distance(l_pd) < 50 and ball1.xcor() < -320:
        ball1.bounce_x()


    #detect if r paddle misses
    if ball1.xcor() > 380:
        ball1.reset_position()
        score.l_point()

        # le paddle misses
    if ball1.xcor() < -380:
        ball1.reset_position()
        score.r_point()
    
sc.exitonclick()

