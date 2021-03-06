
clc;
close all;
clear all;
delete(instrfindall);

% im=imread('geniusimg.png');
N=10;
cam=webcam('Logitech HD Webcam C270');
set(cam,'Resolution','1280x960')
set(cam,'WhiteBalance',6000)
set(cam,'Contrast',50)
 set(cam,'BacklightCompensation',0)
set(cam,'Brightness',100)
origin_pixel=[0 683];
scale_x=0.1442;
scale_y=0.1442;
load('cameraparameters.mat')
tic
T=0;
p_data=cell(1,N);
dt=0;
fl_start=1
zigbeeFlag = input('Enter "0" to disable zigbee else "1": ');
pos_cor_x=0;
pos_cor_y=0;
%Error string to send in case of error
errorString = char('z'.*ones(1,12));
if (zigbeeFlag)
    sp = serial('COM7','BaudRate',57600,'DataBits',8);
    % fp.Timeout=3
    fopen(sp);
end

% sp = serial('COM10','BaudRate',115200,'DataBits',8);
% sp.Timeout=3

% fopen(sp);

P_init=zeros(10,2);
h_init=zeros(10,1);
A=80;B=80; a=3 ;b=2;
N=a+b+1;
for i=8
    sa=0;%+(i-1)*pi/(a*b);%+2*pi-(pi/b);
    P_init(i,:)=[A*cos(a*sa) B*sin(b*sa)];
    h_init(i)=atan2( B*b*cos(b*sa),-A*a*sin(a*sa))
end
for i=9
    sa=2*2*pi/(a+b);
    P_init(i,:)=[A*cos(a*sa) B*sin(b*sa)];
    h_init(i)=atan2( B*b*cos(b*sa),-A*a*sin(a*sa))
end
for i=N-1:N
    sa=0+(i-1)*pi/(a*b)-pi/(2*a*b)+2*pi-(pi/b);
    P_init(i,:)=[A*cos(a*sa) B*sin(b*sa)];
    h_init(i)=atan2( B*b*cos(b*sa),-A*a*sin(a*sa))
end
% tic
T_o=clock;
T_init=clock;

%imr=snapshot(cam);
%imshow(imr);

while(1)
    im=snapshot(cam);
    % imtool(im)
    %     im=imcrop(im,[263.5 76.5 650 439]);orig
    % im=imcrop(im,[255.75 73.25 666 465]);
im=imcrop(im,[309.5 183.5 690 684]);
     %im = undistortImage(im, cameraParams);
     %imshow(im)
    im_gr=rgb2gray(im);
    %         im_gr=imadjust(im_gr);
    
    l_th = graythresh(im_gr);
    
    im_bw=im2bw(im_gr, 0.15);
     %imshow(im_bw)
    
    im_bw_1 = ~bwareaopen(~im_bw, 1500);
    im_bw_2 = bwareaopen(im_bw_1, 1200);
    %         subplot(121)
              %imshow(im_bw_2)
%             imtool(im)
%             keyboard
%         imshow(im)
CC_m=bwconncomp(~im_bw_2);
ss_m=regionprops(CC_m);
% s= ss_m.Centroid

% a=ss_m.Area;
    s=regionprops(~im_bw_2,'centroid');
    a=regionprops(~im_bw_2,'Area');
 
    %
%     data_pos=[cat(1,s.Centroid) cat(1,a.Area)];
data_pos=[round(cat(1,ss_m.Centroid)) cat(1,ss_m.Area)];
%    hold on 0

%  plot(data_pos(:,1),data_pos(:,2),'b*')
%  hold off

    centers=[];
    if size(data_pos,1)~=0
        data_pos=data_pos(data_pos(:,3)<15000,:);
        data_pos=data_pos(data_pos(:,3)>10000,:);
        centers=[data_pos(:,1) data_pos(:,2)];
    end
%     hold on
%     if size(centers,1)~=0
%         plot(centers(:,1),centers(:,2),'*')
%     end

%     hold off
    Xbee_data=[];
    for i=1:size(centers,1)
        %     im_ch=imcrop(~im_bw_2,[centers(i,1)-25 centers(i,2)-25 50 50]);
        %     [centers_ch,radii_1] = imfindcircles(im_ch,[10 18]);
        
        if (T>3)
            im_c=imcrop(im,[centers(i,1)-70 centers(i,2)-70 140 140]);
            gr_c=rgb2gray(im_c);
            gr_c2=imadjust(gr_c);
            bw_c=im2bw(gr_c2,0.2);
           gray= graythresh(gr_c2);
            bk_c=bwareaopen(bw_c,1200);
            bk_g=bwareaopen(~bk_c,1000);
            bw_c=bw_c+~bk_g;
            bw_c=bw_c.*bk_g;
            
%                         subplot(221)
%                         imshow(gr_c)
%                         subplot(222)
%                         imshow(bw_c)
%                         subplot(223)
%                         imshow(bk_c)
%                         subplot(224)
%                         imshow(bk_g)
            CC=bwconncomp(bw_c);
            SS=regionprops(CC);
            data_c=[];
            
            data_c=[round(cat(1,SS.Centroid)) cat(1,SS.Area)];
            
           
            %size(data_c,1)
            if (size(data_c,1)>=2)
                data_c=sortrows(data_c,-3);
                %data_c(1,3) 
                %data_c(2,3)
                if(data_c(1,3)<800  && data_c(2,3)<450)%check
                    D=dist(data_c(1,1:2),data_c(2,1:2)');
                    
                    if(D<=45 )%check
                        
                        ID=1;
                        Heading= atan2(-data_c(1,2)+data_c(2,2),data_c(1,1)-data_c(2,1))*180/pi
                        %                         plot(data_c(2,1),data_c(2,2),'*',data_c(1,1),data_c(1,2),'g*')
                        % ID= hd*3+ld+1;
                        pos_cor_y=(data_c(1,2)+data_c(2,2))/2-70;
                        pos_cor_x=(data_c(1,1)+data_c(2,1))/2-70;
% [pos_cor_x pos_cor_y]

                          


                        Position=[(centers(i,1)-origin_pixel(1))*scale_x -(centers(i,2)-origin_pixel(2))*scale_y]
                          [Position(1) Position(2) Heading T dt_cpu];
                          

                          [pac1,pac2] = xbee_send(10);
                          %pac1(9)
                       if( ID==1)
                        if (fl_start==1)
                            p_data{ID}=[p_data{ID}; [T Position Heading ID dt_cpu ] ];
                        end
                        Xbee_data=[Xbee_data; [Position Heading ID ] ];
                       end
                    else
                        ID= 999;
                        Heading= 999;
                        Position=[999 999];
                        
                    end
%                             hold off
%                                     getframe()
%                                                     subplot(122)
%                                                     imshow(im_c);
%                                                     hold on
%                                                     plot(data_c(2,1),data_c(2,2),'*')
%                                                     plot(data_c(1,1),data_c(1,2),'g*')
                    if size(Xbee_data,2)~=0
                        Xbee_data=sortrows(Xbee_data,4);
                    end
                end
            end
            
        end
    end
    
    
    
    
    
    %     dt= toc
    %     T=T+dt;
    %     tic
    
  T_cpu=clock;
dt_cpu=etime(T_cpu,T_o);
T_o=T_cpu;
T_cpu=etime(T_cpu,T_init);
 T=T+dt_cpu;
    Timedisp=[T_cpu dt_cpu]
%     Timedisp=[T dt_cpu]
%     h=[999 999 999 999 999 999 999 999 999 T];
%     x=[999 999 999 999 999 999 999 999 999 999];
%     y=[999 999 999 999 999 999 999 999 999 999];
%     d_init=[];h_err=[];ag_active_id=[];
%     for i=1:size(Xbee_data,1)
%         ag_i=Xbee_data(i,4);
%         x(ag_i)= Xbee_data(i,1);%+ 10.*randn(1,1);
%         y(ag_i)= Xbee_data(i,2);%+ 10.*randn(1,1);
%         h(ag_i)= Xbee_data(i,3);%+5.*randn(1,1);
%         d_init(i)=sqrt((x(ag_i)-P_init(ag_i,1)).*(x(ag_i)-P_init(ag_i,1))+( y(ag_i)-P_init(ag_i,2)).*( y(ag_i)-P_init(ag_i,2)))
%         h_err(i)=atan2(tan(h_init(ag_i)-h(ag_i)*pi/180),1)*180/pi;
%         ag_active_id(i)=ag_i;
%     end
%     
% %     [ag_active_id d_init h_err  ]
%     
%     
%     if size(Xbee_data,1)~=0
%         if max(d_init)<20 && max(abs(h_err))<=20
%             %         if d_init(1)<12 && h_err(1)<=20
%             if fl_start==0
%                 fl_start=1;
%                 x_st=[911 912 913 914 915 916 917 918 919 920];
%                 y_st =[911 912 913 914 915 916 917 918 919 920];
%                 h_st=[911 912 913 914 915 916 917 918 919 T];
%                 [pkt_1,pkt_2]= xbee_send(h_st,x_st,y_st);
% %                 if (zigbeeFlag)
% %                     pause(0.1)
% %                     
% %                     fwrite(sp ,pkt_1);
% %                     pause(0.15)
% %                     fwrite(sp ,pkt_2);
% %                     pause(0.1)
% %                     %                                         fwrite(sp ,pkt_1);
% %                     %                                         pause(0.15)
% %                     %                                         fwrite(sp ,pkt_2);
% %                 end
%                 fl_start
%             end
%             
%         end
%         
%         
%         
%         
% %                 [x' y' h']
%         [pkt_1,pkt_2]= xbee_send(h,x,y);
%         if (zigbeeFlag)
%             fwrite(sp ,pkt_1);
%             tic;
%             while toc < 0.05
%             end
%             fwrite(sp ,pkt_2);
%             tic;
% %             while toc < 0.05
% %             end
% %             pause (0.5)
%         end
%     end
    
end







