#/usr/bin/env python

'''
Run a message board from the terminal
'''

###########
# Imports #
###########

import datetime
import os

#############
# Functions #
#############

# Terminal dimension functions from
# http://blog.taz.net.au/2012/04/09/getting-the-terminal-size-in-python/

def get_terminal_size(fd=1):
    """
    Returns height and width of current terminal. First tries to get
    size via termios.TIOCGWINSZ, then from environment. Defaults to 25
    lines x 80 columns if both methods fail.

    :param fd: file descriptor (default: 1=stdout)
    """
    try:
        import fcntl, termios, struct
        hw = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
    except:
        try:
            hw = (os.environ['LINES'], os.environ['COLUMNS'])
        except:
            hw = (25, 80)

    return hw

def get_terminal_height(fd=1):
    """
    Returns height of terminal if it is a tty, 999 otherwise

    :param fd: file descriptor (default: 1=stdout)
    """
    if os.isatty(fd):
        height = get_terminal_size(fd)[0]
    else:
        height = 999

    return height

def get_terminal_width(fd=1):
    """
    Returns width of terminal if it is a tty, 999 otherwise

    :param fd: file descriptor (default: 1=stdout)
    """
    if os.isatty(fd):
        width = get_terminal_size(fd)[1]
    else:
        width = 999

    return width

# TODO make this a function?
#def printheader(header_message):

################
# Main Program #
################

if __name__ == "__main__":

    # Message for the top half of the screen
    header_message =  (
     '   __     __     ______     __     ______   ______        __    __     _____ \n'
     '  /\ \  _ \ \   /\  == \   /\ \   /\__  _\ /\  ___\      /\ "-./  \   /\ ___\ \n'
     '  \ \ \/ ".\ \  \ \  __<   \ \ \  \/_/\ \/ \ \  __\      \ \ \-./\ \  \ \___\__ \n'
      '   \ \__/".~\_\  \ \_\ \_\  \ \_\    \ \_\  \ \_____\     \ \_\ \ \_\  \ \_____\ \n'
       '    \/_/   \/_/   \/_/ /_/   \/_/     \/_/   \/_____/      \/_/  \/_/   \/_____/'
                  )

    message_width = 80

    #Get the terminal size for setting print dimensions
    t_height = get_terminal_height()
    t_width = get_terminal_width()

    ##############
    # Print Loop #
    ##############

    narf = 49
    message_list = list()
    datetime_list = list()
    while narf < 50:

        # Refresh the screen
        os.system('cls' if os.name=='nt' else 'clear')

        # Print my message
        num_message_lines = int(len(header_message)/message_width)
        num_buffer_lines = int(((t_height*.3)-num_message_lines)/2.)
        print '\n' * num_buffer_lines
        print header_message
        print '\n' * num_buffer_lines
        print '=' * t_width

        # Print messages
        for i in range(len(message_list)):
            idx = (len(message_list) - 1) - i # print in reverse order
            print datetime_list[idx], '-', message_list[idx]

        # Fill in spaces to move user promt to bottom of screen
        print '\n' * (int(t_height*.7)-len(message_list)-1)

        # Process user input
        input_message = 'Write Message and Press <Enter>:'
        input_len = 80
        cont_bool = False
        while cont_bool == False:

            input_str = raw_input(input_message)
            if len(input_str) > input_len:
                print 'Error !$#$ Only',input_len,'characters allowed.'
            else:
                # Save the message
                cont_bool = True
                message_list.append(input_str)
                datetime_list.append((datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S"))


