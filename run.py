from app.sniffer import start_sniffer

def run_manager(inp:str):
    commands = [
        " 1.'drymode' : shows you the changes beforehand without actually making the changes",
        " 2.'organize': only oranizes the files if any organization needed",
        " 3.'manager' : manages and observes / creates files if any changes needed"
    ]
    
    try:
        print('Running the Manager: ...')
        if inp == "drymode":
            print("Running the Manager on DryMode!")
            
        elif inp == "organize":
            if __name__ == "__main__":
                path_to_sniff = "." 
                start_sniffer(path_to_sniff)
            print("Running the Manager on Organizer Mode!")
            
        elif inp == "--help":
            print("Welcome to the Manager (File Manager): ")
            print("Commands:")
            for command in commands:
                print(command)
        else:
            print("Invalid Command: Command doesnot exist!")
            print('Try --help for further info')
            
    except Exception as e: 
        print(e, 'Manager has been stopped!')

while True:
    command = str(input('Enter the command: '))
    if command == "exit":
        print("Exiting the Manager Lobby!")
        break
    else:
        run_manager(command)