#!/usr/bin/env python3
#Name: Wyatt Bechtle
#Date: 4/4/2023
#Project: Week Day Finder GUI
#--------------------------------------------------------------------------------------------
from tkinter import *
from tkinter.messagebox import *

#Class is used to generate a GUI that finds the week day of a give date.
class Week_Day_Finder:

    #Init method creates the main window and all its widgets.
    def __init__(self):

        #Create the main window.
        self.main_window = Tk()

        #Set geometry to appropiate size.
        self.main_window.geometry("500x250")

        #Add a title.
        self.main_window.title('Week Day Finder')

        #Create the needed frames to position all widgets desirably.
        self.program_explanation_frame = Frame(self.main_window)
        self.input_year_and_month_frame = Frame(self.main_window)
        self.input_day_frame = Frame(self.main_window)

        #Create and pack a text widget to display a program explanation.
        self.program_explanation_label = Label(self.program_explanation_frame,
                                             text = 'This program finds the week day of any ' +
                                                    'date after 1582.')
        self.program_explanation_label.pack(padx = 10, pady = 10)

        #Create and pack description Label widget for Entry widget.
        self.discription_label_year = Label(self.input_year_and_month_frame, 
                                            text = 'Enter the year(after 1582):')
        self.discription_label_year.pack(side = 'left', padx = (10, 0), pady = 10)

        #Create and pack Entry widget.
        self.user_input_year = Entry(self.input_year_and_month_frame, width = 4)
        self.user_input_year.pack(side = 'left', padx = (0, 10), pady = 10)

        #Create and pack description Label widget for Entry widget.
        self.discription_label_month = Label(self.input_year_and_month_frame, 
                                            text = 'Enter the month number(1-12):')
        self.discription_label_month.pack(side = 'left', padx = (10, 0), pady = 10)

        #Create and pack Entry widget.
        self.user_input_month = Entry(self.input_year_and_month_frame, width = 2)
        self.user_input_month.pack(side = 'left', padx = (0, 10), pady = 10)

        #Create and pack a button widget for entering the day.
        self.proceed_to_day_button = Button(self.input_day_frame, 
                                            text = 'Enter Day', 
                                            command = self.validate_year_and_month) 
        self.proceed_to_day_button.pack(padx = 10, pady = 10)

        #Pack all frames.
        self.program_explanation_frame.pack()
        self.input_year_and_month_frame.pack()
        self.input_day_frame.pack()

        #Enter the main loop.
        mainloop()

    #This method is used to validate the year and month input by user. 
    def validate_year_and_month(self):

        #Retrieve the user input for year and month.
        self.year = self.user_input_year.get()
        self.month = self.user_input_month.get()

        #Try statement used to avoid throughing an exception.
        try:
            
            #determine if year is after 1582.
            if int(self.year) > 1582:

                #Determine if month is within 1 to 12 inclusive.
                if 0 < int(self.month) < 13:

                    self.input_day()    #All is good.
                
                else:
                    showinfo('ERROR', 'Invalid Month Entry.')

            else:
                showinfo('ERROR', 'Invalid Year Entry.')

        except:
            showinfo('ERROR', 'Invalid Entry.')

    #This method is used to validate the day input by user. 
    def validate_day(self):

        #try block used to avoid throughing exception.
        try:

            #Retrieve the user input for day.
            self.day = self.user_input_day.get()

            #Decision statement detemines what the month is and validates the day based on the
            #month and if it was a leap year.
            #
            #January scenario.
            if self.month == '1':

                #If in range, . Else, Display error.
                if 0 < int(self.day) < 32:
                    self.find_day_of_week()
                else:
                    showinfo('ERROR', 'Invalid Entry. Must be 31 or less')

            #February scenario.
            elif self.month == '2':

                #Test if leap year.
                if (int(self.year) % 4) == 0:
                    if (int(self.year) % 100) == 0:
                        if (int(self.year) % 400) == 0:

                            #Leap year scenario.
                            #If in range, . Else, Display error.
                            if 0 < int(self.day) < 30:
                                self.find_day_of_week()
                            else:
                                showinfo('ERROR', 'Invalid Entry Must be 29 or less')
                        else:
                            #Non-Leap year scenario.
                            if 0 < int(self.day) < 29:
                                self.find_day_of_week()
                            else:
                                showinfo('ERROR', 'Invalid Entry Must be 28 or less')
                    else:
                        #Non-Leap year scenario.
                            if 0 < int(self.day) < 29:
                                self.find_day_of_week()
                            else:
                                showinfo('ERROR', 'Invalid Entry Must be 28 or less')
                else: 
                    #Non-Leap year scenario.
                            if 0 < int(self.day) < 29:
                                self.find_day_of_week()
                            else:
                                showinfo('ERROR', 'Invalid Entry Must be 28 or less')
            #March scenario.
            elif self.month == '3':

                #If in range, . Else, Display error.
                if 0 < int(self.day) < 32:
                    self.find_day_of_week()
                else:
                    showinfo('ERROR', 'Invalid Entry Must be 31 or less')

            #April scenario.
            elif self.month == '4':

                #If in range, . Else, Display error.
                if 0 < int(self.day) < 31:
                    self.find_day_of_week()
                else:
                    showinfo('ERROR', 'Invalid Entry Must be 30 or less')

            #May scenario.
            elif self.month == '5':

                #If in range, . Else, Display error.
                if 0 < int(self.day) < 32:
                    self.find_day_of_week()
                else:
                    showinfo('ERROR', 'Invalid Entry Must be 31 or less')

            #June scenario.
            elif self.month == '6':

                #If in range, . Else, Display error.
                if 0 < int(self.day) < 31:
                    self.find_day_of_week()
                else:
                    showinfo('ERROR', 'Invalid Entry Must be 30 or less')

            #July scenario.
            elif self.month == '7':

                #If in range, . Else, Display error.
                if 0 < int(self.day) < 32:
                    self.find_day_of_week()
                else:
                    showinfo('ERROR', 'Invalid Entry Must be 31 or less')

            #August scenario.
            elif self.month == '8':

                #If in range, . Else, Display error.
                if 0 < int(self.day) < 32:
                    self.find_day_of_week()
                else:
                    showinfo('ERROR', 'Invalid Entry Must be 31 or less')

            #September scenario.
            elif self.month == '9':

                #If in range, . Else, Display error.
                if 0 < int(self.day) < 31:
                    self.find_day_of_week()
                else:
                    showinfo('ERROR', 'Invalid Entry Must be 30 or less')

            #October scenario.
            elif self.month == '10':

                #If in range, . Else, Display error.
                if 0 < int(self.day) < 32:
                    self.find_day_of_week()
                else:
                    showinfo('ERROR', 'Invalid Entry Must be 31 or less')

            #November scenario.
            elif self.month == '11':

                #If in range, . Else, Display error.
                if 0 < int(self.day) < 31:
                    self.find_day_of_week()
                else:
                    showinfo('ERROR', 'Invalid Entry Must be 30 or less')

            #December scenario.
            else:

                #If in range, . Else, Display error.
                if 0 < int(self.day) < 32:
                    self.find_day_of_week()
                else:
                    showinfo('ERROR', 'Invalid Entry Must be 31 or less')
        except:
            showinfo('ERROR', 'Invalid Entry')

    #This method is used to get the day of the week via provided algorithm.
    def find_day_of_week(self):

        #If month is Jan. or Feb. change to 13th or 14th month of prev. year.
        if self.month == '1' or self.month == '2':
            self.month = str(int(self.month) + 12)
            self.year = str(int(self.year) - 1)

        #Use provided algorithm to find day of week.
        self.total_weeks =  int(self.day) + 2 * int(self.month) + int(0.6 * (int(self.month) 
                            + 1 )) + int(self.year) + int(int(self.year) / 4) - int(
                            int(self.year) / 100) + int(int(self.year) / 400) + 2

        self.day_of_week = self.total_weeks % 7

        #If month is Jan. or Feb. change to 1st or 2nd month add one to year.
        if self.month == '13' or self.month == '14':
            self.month = str(int(self.month) - 12)
            self.year = str(int(self.year) + 1)

        #Create lists for output.
        self.week_days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday',
                          'Thursday', 'Friday']

        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 
                       'July', 'August', 'September', 'October', 'November', 'December']
        
        #Create a neat formatted output for label.
        self.formatted_output = str(self.months[int(self.month) - 1] + ' ' + self.day + ', ' 
                                    + self.year + ' is a ' + self.week_days[self.day_of_week])
        
        #Clear the proceed to day button.
        self.find_day_week_button.destroy()

        #Create another frame to hold the 'find another week day' and 'quit' button.
        self.reset_or_quit_button_frame = Frame(self.main_window)

        #Create and pack description Label widget for Entry widget.
        self.discription_label_week_day = Label(self.find_week_day_button_frame, 
                                            text = self.formatted_output)
        self.discription_label_week_day.pack(padx = 10, pady = 10)
        
        #Create and pack Button widget.
        self.reset_button = Button(self.reset_or_quit_button_frame,
                                           text = 'Reset',
                                           command = self.reset_gui)
        self.reset_button.pack(side = 'left', padx = 10, pady = 10)

        #Create and pack Button widget.
        self.quit_button = Button(self.reset_or_quit_button_frame,
                                           text = 'Quit',
                                           command = self.main_window.destroy)
        self.quit_button.pack(side = 'left', padx = 10, pady = 10)

        #Pack button frame.
        self.reset_or_quit_button_frame.pack()

    #This method is used to get the day from the user.
    def input_day(self):

        #Clear the proceed to day button.
        self.proceed_to_day_button.destroy()

        #Create another frame to hold the 'find week day' button.
        self.find_week_day_button_frame = Frame(self.main_window)

        #Create and pack description Label widget for Entry widget.
        self.discription_label_day = Label(self.input_day_frame, 
                                            text = 'Enter the day:')
        self.discription_label_day.pack(side = 'left', padx = (10, 0), pady = 10)

        #Create and pack Entry widget.
        self.user_input_day = Entry(self.input_day_frame, width = 2)
        self.user_input_day.pack(side = 'left', padx = (0, 10), pady = 10)

        #Create and pack Button widget.
        self.find_day_week_button = Button(self.find_week_day_button_frame,
                                           text = 'Find Week Day',
                                           command = self.validate_day)
        self.find_day_week_button.pack(padx = 10, pady = 10)

        #Pack the associated frames.
        self.input_day_frame.pack()
        self.find_week_day_button_frame.pack()

    #This method is used to reset the gui.
    def reset_gui(self):

        #Clear entry fields of input.
        self.user_input_month.delete(0, END)
        self.user_input_year.delete(0, END)

        #Reset the frames.
        self.reset_or_quit_button_frame.destroy()
        self.find_week_day_button_frame.destroy()

        #Destroy not needed widgets.
        self.discription_label_day.destroy()
        self.user_input_day.destroy()

        #Create and pack a button widget for entering the day.
        self.proceed_to_day_button = Button(self.input_day_frame, 
                                            text = 'Enter Day', 
                                            command = self.validate_year_and_month) 
        self.proceed_to_day_button.pack(padx = 10, pady = 10)

#If ran as main create an instance of Week_Day_Finder().
if __name__ == '__main__':
    Week_Day_Finder()