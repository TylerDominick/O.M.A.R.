from __future__ import print_function
from __future__ import division
from builtins import input
import line_sensor
import time
import gopigo
import atexit
from gopigo import *
from time import sleep


fwd_speed= 35                                                                                   
poll_time=0.01


slight_turn_speed=int(.60*fwd_speed)
turn_speed=int(.8*fwd_speed)

last_val=[0]*5                                          
curr=[0]*5                                                      

gopigo.set_speed(fwd_speed)

line_pos=[0]*5
white_line=line_sensor.get_white_line()
black_line=line_sensor.get_black_line()
range_sensor= line_sensor.get_range()
threshold=[a+b/2 for a,b in zip(white_line,range_sensor)]

mid     =[0,0,1,0,0]    # Middle Position.
small_r =[0,1,1,0,0]    # Slightly to the left.
small_r1=[0,1,0,0,0]    # Slightly to the left.
small_l =[0,0,1,1,0]    # Slightly to the right.
small_l1=[0,0,0,1,0]    # Slightly to the right.
all_black =[1,1,1,1,1]  # Sensor reads stop.
all_white =[0,0,0,0,0]  # Sensor reads stop.
stop2   =[1,0,0,0,1]
bigturn   =[1,0,0,0,0]
bigturn2   =[0,0,0,0,1]
rightcorner   =[0,0,1,1,1]
leftcorner   ={1,1,1,0,0}
smolturn   =[1,1,0,0,0]
smolturn2   =[0,0,0,1,1]
condition1 = [0,1,0,0,0]

def absolute_line_pos():
        raw_vals=line_sensor.get_sensorval()
        for i in range(5):
                if raw_vals[i]>threshold[i]:
                        line_pos[i]=1
                else:
                        line_pos[i]=0
        return line_pos


def turn_left():
  set_right_speed(80)
  set_left_speed(0)
  enc_tgt(0,1,15)
  fwd()
  time.sleep(0.53)


def turn_right():
  set_right_speed(0)
  set_left_speed(80)
  enc_tgt(1,0,15)
  fwd()
  time.sleep(0.50)

def go_straight():
                gopigo.set_speed(fwd_speed)
                gopigo.fwd()
                
def turn_slight_left():
                gopigo.set_right_speed(slight_turn_speed)
                gopigo.set_left_speed(fwd_speed)
                gopigo.fwd()

def turn_bigger_left():
        gopigo.set_right_speed(turn_speed)
        gopigo.set_left_speed(fwd_speed)
        gopigo.fwd()
                        
def turn_slight_right():
                gopigo.set_right_speed(fwd_speed)
                gopigo.set_left_speed(slight_turn_speed)
                gopigo.fwd()

def turn_bigger_right():
        gopigo.set_right_speed(fwd_speed)
        gopigo.set_left_speed(turn_speed)
        gopigo.fwd()

def stop_now():
        gopigo.stop()



def run_gpg(curr):
        
        if  curr==mid:
                go_straight()
                
        
        elif curr==small_l1 or  curr==small_l:
                turn_slight_right()
                 
        
        elif curr==small_r1 or curr==small_r:
                turn_slight_left()
                
        elif curr== all_black:
                stop_now()
                
                

        elif curr== all_white:
                stop_now()
                
                

        #elif curr== leftcorner:
                #stop_now()

        #elif curr== smolturn or curr == bigturn:
                #turn_bigger_left()

        #elif curr== smolturn2 or curr == bigturn2:
                #turn_bigger_right()



Line_list = ["Forward", "Right", "Forward", "Right", "Forward"]


def command_handler(Line_list):
        print (Line_list)
        for command in Line_list:
                print (command)
                if command == "Forward":
                        curr=absolute_line_pos()
                        while True:
                                curr=absolute_line_pos()
                                if curr == mid or curr==small_l1 or  curr==small_l or curr == small_r or curr == small_r1:
                                        run_gpg(curr)
                                if curr == all_white:
                                        gopigo.stop()
                                        time.sleep(1)
                                        temp = absolute_line_pos()
                                        temp = absolute_line_pos()
                                        if temp == all_white:
                                                print ("White found")
                                                break
                                        else:
                                                gopigo.forward()
                                if curr == all_black:
                                        break
                                print(curr)
                elif command == "Left":
                        turn_left()
                        time.sleep(1)
                elif command == "Right":
                        turn_right()
                        time.sleep(1)
                elif command == "Turn Around":
                        turn_around()
                        time.sleep(1)

        


command_handler(Line_list);














                 


        
        





