# A car game
 
command = ''
started = False

while True:
    command = input('> ')
    if command == 'help':
        print('start - to start the car\n\n stop - to stop the car\n\n quit - to exit\n\n\n')
        
    if command =='start':
        if started:
         
            print('car is already started!!!\n\n')
        else:
         
            started = True

            print('car has started...ready to move\n\n')
        
        
    elif command =='stop':
        if not started:
            print('car is already stopped!!\n\n')
        else:
            started = False
        print('car has stopped\n\n')
        
    elif command == 'quit':
        print('goodbye')
        exit(0)
    else:
      print('invalid command, you have to type start, stop, or quit') 