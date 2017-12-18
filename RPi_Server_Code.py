#!/usr/bin/env python
###############################################################################################################                                                          
# Program Name: Browser_Client_Coder.html                                     
# ================================     
# This code is for controlling a robot by a web browser using web sockets                            
# http://www.dexterindustries.com/                                                                
# History
# ------------------------------------------------
# Author     Comments
# Joshwa     Initial Authoring
#                                                                  
# These files have been made available online through a Creative Commons Attribution-ShareAlike 3.0  license.
# (http://creativecommons.org/licenses/by-sa/3.0/)           
#
###############################################################################################################

# CONNECTIONS-
#   Left Motor  - Port A
#   Right Motor - Port D
#
# PREREQUISITES
# Tornado Web Server for Python
#
# TROUBLESHOOTING:
# Don't use Ctrl+Z to stop the program, use Ctrl+c.
# If you use Ctrl+Z, it will not close the socket and you won't be able to run the program the next time.
# If you get the following error:
#   "socket.error: [Errno 98] Address already in use "
# Run this on the terminal:
#   "sudo netstat -ap |grep :9093"
# Note down the PID of the process running it
# And kill that process using:
#   "kill pid"
# If it does not work use:
#   "kill -9 pid"
# If the error does not go away, try changin the port number '9093' both in the client and server code

#import BrickPi.py file to use BrickPi operations
import tornado
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import time
import pathfinder
import StraightLineFollow
import threading

#Initialize TOrnado to use 'GET' and load index.html
class MainHandler(tornado.web.RequestHandler):
  def get(self):
    loader = tornado.template.Loader(".")
    self.write(loader.load("index.html").generate())

#Code for handling the data sent from the webpage
class WSHandler(tornado.websocket.WebSocketHandler):
  
  def open(self):
    print ('connection opened...')
  def check_origin(self,origin):
    return True
  def on_message(self, message):      # receives the data from the webpage and is stored in the variable message
    print 'received:', message # prints the revived from the webpage
    nodes.append(message)
    if message == "gotodest":
      g = pathfinder.build_map()
      print nodes[1]
      print nodes[2]
      path = pathfinder.shortest_path(g, nodes[1], nodes[2])
      pathfinder.robot_commands(g, path)
      
      
  def on_close(self):
    print ('connection closed...')

application = tornado.web.Application([
  (r'/ws', WSHandler),
  (r'/', MainHandler),
  (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
])

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("Ready")
        while running:
                 # Ask BrickPi to update values for sensors/motors
            time.sleep(.2)              # sleep for 200 ms

if __name__ == "__main__":
             #Send the properties of sensors to BrickPi
  nodes = []
  running = True
  thread1 = myThread(1, "Thread-1", 1)
  thread1.setDaemon(True)
  thread1.start()
  application.listen(9093)            #starts the websockets connection
  tornado.ioloop.IOLoop.instance().start()
  

