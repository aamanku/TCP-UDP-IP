clear all
close all
lport=6969;
sock=pnet('udpsocket',lport);
i=0;
try
    while i==0
        i=i;
        raw=pnet(sock,'readpacket');
        % if packet larger then 1 byte then read maximum of 1000 doubles in network byte order
        data=typecast(pnet(sock,'read',1000,'uint8'),'double');
        disp(data)
    end
end
