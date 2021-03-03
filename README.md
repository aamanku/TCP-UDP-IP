Porting Toolbox Downloaded from : https://www.mathworks.com/matlabcentral/fileexchange/345-tcp-udp-ip-toolbox-2-0-6 to work with matlab 2020b

Matlab command to compile:
mex -O pnet.c 'C:\Program Files\MATLAB\R2020b\sys\lcc64\lcc64\lib64\ws2_32.lib' -DWIN32

