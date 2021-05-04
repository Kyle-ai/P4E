#Change your socket program so that it counts the number of characters it has
#recived and stops displaying any text after is has shown 3000 characters.The
#program should retrive the entire document and count the total number of
#characters at the end of the document.

import socket   #test with: http://data.pr4e.org/romeo.txt *len(received) = 536
try:
    url = input('Enter URL: ')
    host = url.split('/')[2]

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = 'GET ' + url + ' HTTP/1.0\r\n\r\n'
    cmd = cmd.encode()
    mysock.send(cmd)


    received = b''
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        received += data
    received = received.decode()
    print(received[:3000])
    print(len(received))



    mysock.close()
except:
    print('Please enter in the proper format')
