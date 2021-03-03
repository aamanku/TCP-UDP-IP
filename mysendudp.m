clear all
close all

data= typecast(rand([50,1]),'uint8'); %send uint8
host = '192.168.2.2';
port = '9000';
sock = pnet('udpsocket',1111);
if sock~=-1
    try
        pnet(sock,'write',data); % Write to write buffer
        pnet(sock,'writepacket',host,port); %send buffer as udp packet
    end
    pnet(sock,'close');
end