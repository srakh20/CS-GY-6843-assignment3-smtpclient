from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope
    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver,port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print("After connect", recv) #You can use these print statement to validate return codes from the server.
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024).decode()
    #print("After HELO", recv)
    if recv[:3] != '250':
        print('250 reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mailFrom='MAIL FROM: <alice@gmail.com> \r\n'
    clientSocket.send(mailFrom.encode())
    recv = clientSocket.recv(1024).decode()
    #print("After MAIL FROM command: " +recv)
    if recv[:3] != '250':
        print('250 reply not received from server.')

    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptto = 'RCPT TO: <bob@gmail.com> \r\n'
    clientSocket.send(rcptto.encode())
    recv = clientSocket.recv(1024).decode()
    #print("After recptto command: " +recv)
    if recv[:3] != '250':
        print('250 reply not received from server.')
    # Fill in end

    # Send DATA command and handle server response.
    # Fill in start
    data = 'DATA\r\n'
    clientSocket.send(data.encode())
    recv = clientSocket.recv(1024).decode()
    #print("After DATA command: " +recv)
    if recv[:3] != '354':
        print('354 reply not received from server.')

    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())

    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv = clientSocket.recv(1024).decode()
    #print("End message response:"+ recv) 
    if recv[:3] != '250':
        print('250 reply not received from server.')

    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv = clientSocket.recv(1024).decode()
    #print(f"QUIT response: {recv}")
    if recv[:3] != '221':
        print('221 reply not received from server.')
    clientSocket.close()

    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')