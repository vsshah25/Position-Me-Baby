clear all;
clc;
s1=serial('COM7');
set(s1,'BaudRate',115200,'DataBits',8);
fopen(s1);
flushinput(s1);
 
  
 for i=1:1000
%      temp_RSSI=char(fread(s1,9));
%      vect_RSSI(i,:)=temp_RSSI(1:9)
     vect_RSSI(i,:)=fread(s1,9);
     b=char(vect_RSSI)
%     a(i,:)=c(1:9)
    i
 end
fclose(s1);