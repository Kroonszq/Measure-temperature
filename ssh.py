import paramiko
import socket

class SSH:

    def __init__(self) -> None:
        self.session = paramiko.client.SSHClient()
        self.connected = False


    def connect(self):
        try:
            # initiliaze paramiko 
            # add policiy default policy key
            # connect to raspberry pi with ssh
            self.session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.session.connect(
                "145.24.238.130", 
                username="pi", 
                password="raspberry")

        # catch errors if they occur
        except socket.error as e:
            return {"error": e}
        except paramiko.AuthenticationException as e:
            return {"error": e}
        except paramiko.SSHException as e:
            return {"error": e}
        else:
            self.connected = True
            return {"success": "connected to 145.24.238.130"}

    def disconnect(self):
        self.session.close()
        self.connected = False
        print("disconnected")

    def execCommand(self, command: str) -> None:    
        _stdin, _stdout,_stderr = self.session.exec_command(command)
            

