import sys
import threading
import subprocess
import numpy as np
import pyqtgraph as pg
from PyQt4 import QtCore, QtGui
from untitled import Ui_SlotcarTimer
import serial
import pygame
import random
 
class MyDialog(QtGui.QDialog):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_SlotcarTimer()
        self.ui.setupUi(self)
        try:
            self.ser = serial.Serial('/dev/ttyUSB0', 115200)
        except:
            print("Could not open serial port")
            exit(1)
        # Set up the Start Button
        self.ui.pushButton.clicked.connect(self.StartButton)
        self.ui.pushButton_2.clicked.connect(self.ResetButton)
       
        self.num_of_laps = 0
        self.new_time_0_avail = False
        self.new_time_1_avail = False
        self.time_list_0_x = np.zeros(1)
        self.time_list_1_x = np.zeros(1)
        self.time_list_0_y = np.zeros(1)
        self.time_list_1_y = np.zeros(1)

        self.jump_start_0 = False
        self.jump_start_1 = False

        self.best_lap_0 = 999.999
        self.best_lap_1 = 999.999
        self.average_0 = 0.000
        self.average_1 = 0.000
        self.average_of_5_0 = 0.000
        self.average_of_5_1 = 0.000
        self.best_average_of_5_0 = 999.999
        self.best_average_of_5_1 = 999.999

        thread = threading.Thread(target=self.read_serial_data)
        thread.daemon = True
        thread.start()

        plot_timer = QtCore.QTimer(self)
        self.connect(plot_timer, QtCore.SIGNAL("timeout()"), self.update_plot);
        plot_timer.start(500)
        
    def StartButton(self):
        
        self.num_of_laps = int(self.ui.lineEdit.text())
        self.ser.write("S")
        sound_thread = threading.Thread(target=self.play_start_sequence)
        sound_thread.daemon = True
        sound_thread.start()


    def ResetButton(self):
        self.close()
        subprocess.call("python" + " gui.py", shell=True)
    
    def update_plot(self):
        # Handle the JUMPED START
        if (self.jump_start_0):
            self.ui.listWidget.addItem("JUMP START P1")
        if (self.jump_start_1):
            self.ui.listWidget_2.addItem("JUMP START P2")
        # Process new time for player 0
        if (self.new_time_0_avail):
            if (self.lap_no_0 > 0):
                # Handle new improvment
                if (self.last_time_0 < self.best_lap_0):
                    self.best_lap_0 = self.last_time_0
                    self.ui.label_5.setText(str(self.best_lap_0))
                    sound_thread = threading.Thread(target=self.play_sound_0, args=(self.best_lap_0,))
                    sound_thread.daemon = True
                    sound_thread.start()
                self.average_0 = self.average_0 + (self.last_time_0 - self.average_0)/self.lap_no_0
                self.ui.label_6.setText(str(self.average_0))
            self.time_list_0_x = np.append(self.time_list_0_x, float(self.lap_no_0))
            self.time_list_0_y = np.append(self.time_list_0_y, self.last_time_0)
           
            # Handle average of 5
            if (self.lap_no_0 >= 5):
                self.average_of_5_0 = np.sum(self.time_list_0_y[-5:])/5
                self.ui.label_8.setText(str(self.average_of_5_0))
                if (self.average_of_5_0 < self.best_average_of_5_0):
                    self.best_average_of_5_0 = self.average_of_5_0
                    self.ui.label_11.setText(str(self.best_average_of_5_0))
            
            # Handle end of race
            if (self.lap_no_0 == self.num_of_laps):
                self.ui.label_22.setText(str(np.sum(self.time_list_0_y)))
                if (self.lap_no_1 < self.lap_no_0):
                    sound_thread = threading.Thread(target=self.play_win_0)
                    sound_thread.daemon = True
                    sound_thread.start()

            # Update list and plot
            self.ui.listWidget.addItem("LAP" + str(self.lap_no_0) + "\t\t" + str(self.last_time_0))
            self.ui.listWidget.scrollToBottom()
            self.ui.graphicsView.plot(self.time_list_0_x, self.time_list_0_y, pen=(1,3))
            self.ui.progressBar.setValue(100*self.lap_no_0/self.num_of_laps)
            self.new_time_0_avail = False
        
        # Process new time for player 1
        if (self.new_time_1_avail):
            if (self.lap_no_1 > 0):
                # Handle new improvement
                if (self.last_time_1 < self.best_lap_1):
                    self.best_lap_1 = self.last_time_1
                    self.ui.label_14.setText(str(self.best_lap_1))
                    sound_thread = threading.Thread(target=self.play_sound_1, args=(self.best_lap_1,))
                    sound_thread.daemon = True
                    sound_thread.start()
                self.average_1 = self.average_1 + (self.last_time_1 - self.average_1)/self.lap_no_1
                self.ui.label_18.setText(str(self.average_1))
            self.time_list_1_x = np.append(self.time_list_1_x, float(self.lap_no_1))
            self.time_list_1_y = np.append(self.time_list_1_y, self.last_time_1)

            # Handle average of 5
            if (self.lap_no_1 >= 5):
                self.average_of_5_1 = np.sum(self.time_list_1_y[-5:])/5
                self.ui.label_13.setText(str(self.average_of_5_1))
                if (self.average_of_5_1 < self.best_average_of_5_1):
                    self.best_average_of_5_1 = self.average_of_5_1
                    self.ui.label_19.setText(str(self.best_average_of_5_1))

            # Handle end of race
            if (self.lap_no_1 == self.num_of_laps):
                self.ui.label_23.setText(str(np.sum(self.time_list_1_y)))
                if (self.lap_no_0 < self.lap_no_1):
                    sound_thread = threading.Thread(target=self.play_win_1)
                    sound_thread.daemon = True
                    sound_thread.start()

            # Update list and plot
            self.ui.listWidget_2.addItem("LAP" + str(self.lap_no_1) + "\t\t" + str(self.last_time_1))
            self.ui.listWidget_2.scrollToBottom()
            self.ui.graphicsView_2.plot(self.time_list_1_x, self.time_list_1_y, pen=(1,3))
            self.ui.progressBar_2.setValue(100*self.lap_no_1/self.num_of_laps)
            self.new_time_1_avail = False

    def play_start_sequence(self):
        pygame.mixer.init(32000)
        pygame.mixer.music.load("./sound/intro_" + random.randint(1,5) + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

    def play_overall_best_0(self):
        pygame.mixer.init(32000)
        pygame.mixer.music.load("./sound/Dave_laprecord_" + random.randint(1,2) + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

    def play_overall_best_1(self):
        pygame.mixer.init(32000)
        pygame.mixer.music.load("./sound/Julie_laprecord_" + random.randint(1,2) + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue
    
    def play_personal_best_0(self):
        pygame.mixer.init(32000)
        pygame.mixer.music.load("./sound/Dave_personalbest.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

    def play_personal_best_1(self):
        pygame.mixer.init(32000)
        pygame.mixer.music.load("./sound/Julie_personalbest.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue
    
    def play_sound_0(self, time):
        if (time > 3.0 and time < 10.0):
            if (time < self.best_lap_1):
                self.play_overall_best_0()
            else:
                self.play_personal_best_0()
            self.play_seconds_0(int(time))
            self.play_mseconds_0(time - float(int(time)))
        return

    
    def play_sound_1(self, time):
        if (time > 3.0 and time < 10.0):
            if (time < self.best_lap_0):
                self.play_overall_best_1()
            else:
                self.play_personal_best_1()
            self.play_seconds_1(int(time))
            self.play_mseconds_1(time - float(int(time)))
        return

    def play_seconds_0(self, seconds):
        pygame.mixer.init(32000)
        pygame.mixer.music.load("./sound/d_sec_" + str(seconds) + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue
    
    def play_seconds_1(self, seconds):
        pygame.mixer.init(32000)
        pygame.mixer.music.load("./sound/j_sec_" + str(seconds) + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

    def play_mseconds_0(self, mseconds):
        pygame.mixer.init(32000)
        pygame.mixer.music.load("./sound/d_msec_" + str(int(mseconds*10)) + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue
    def play_mseconds_1(self, mseconds):
        pygame.mixer.init(32000)
        pygame.mixer.music.load("./sound/j_msec_" + str(int(mseconds*10)) + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

    def play_win_0(self):
        pygame.mixer.init(32000)
        pygame.mixer.music.load("./sound/Dave_win_" + str(random.randint(1,5)) + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

    def play_win_1(self):
        pygame.mixer.init(32000)
        pygame.mixer.music.load("./sound/Julie_win_" + str(random.randint(1,5)) + ".mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
                continue

    def read_serial_data(self):
        while True:
            input_line = ""
            try:
                input_line = self.ser.readline()
            except:
                print("Error Reading serial port.")
        
            if not input_line == "":
                if (input_line == "J0\r\n"):
                    self.jump_start_0 = True
                    print("JUMP START")
                if (input_line == "J1\r\n"):
                    self.jump_start_1 = True
                    print("JUMP START")
                try:
                    input_line = input_line.split(";")
                    player = input_line[0]
                    lap_sec = input_line[1]
                    lap_msec = input_line[2]
                    lap_no = input_line[3]
                    if (player == "S0"):
                        self.last_time_0 = float(lap_sec + "." + lap_msec)
                        self.lap_no_0 = int(lap_no)
                        self.new_time_0_avail = True
                    if (player == "S1"):
                        self.last_time_1 = float(lap_sec + "." + lap_msec)
                        self.lap_no_1 = int(lap_no)
                        self.new_time_1_avail = True
                    
                    print input_line
                except:
                    print("Error handling input.")
                    print input_line
         
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())

