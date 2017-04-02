A=160;
B=120;
a=3;
b=4;
N=a+b+1;
so=cell(N,1);
xa=cell(N,1);
ya=cell(N,1);
vxa=cell(N,1);
vya=cell(N,1);
Va=cell(N,1);
ha=cell(N,1);
xl=cell(N,1);
yl=cell(N,1);
vxl=cell(N,1);
vyl=cell(N,1);
Vl=cell(N,1);
ts=cell(N,1);
t_r=cell(N,1);
Ts=cell(N,1);
dist_l=cell(N,1);
d_temp=cell(N,1);
 fclose(sp);
bot_id=[]
sl=cell(N,1);
for i=1:N
    if (size(p_data{i},1)>100)
    bot_id=[bot_id; i]
    end
sl{i}=[];

end



for i=1:2
so{i}=0;%+(i-1)*pi/(a*b)+2*pi-(pi/b);
%P_init=[P_init; [A*cos(a*sa) B*sin(b*sa)]];
end
for i=3:N-2
so{i}=0+pi/(a*b)+(i-2)*(pi/(a*b)-pi/((2*a*b)*(a+b-2)))+2*pi-pi/b;
%P_init=[P_init; [A*cos(a*sa) B*sin(b*sa)]];
end
for i=N-1:N
so{i}=0+(i-1)*pi/(a*b)-pi/(2*a*b)+2*pi-(pi/b);
%P_init=[P_init; [A*cos(a*sa) B*sin(b*sa)]];
end

for i=1:size(bot_id,1)
     id=bot_id(i)
in=1:size(p_data{id})-1;
d_temp{id}=p_data{id}((sqrt((p_data{id}(in,1)-p_data{id}(in+1,1)).^2+(p_data{id}(in,2)-p_data{id}(in+1,2)).^2)<15),:)
in=1:size(d_temp{id})-1;
d_temp{id}=d_temp{id}((sqrt((d_temp{id}(in,1)-d_temp{id}(in+1,1)).^2+(d_temp{id}(in,2)-d_temp{id}(in+1,2)).^2)<15),:)
in=1:size(d_temp{id})-1;
d_temp{id}=d_temp{id}((sqrt((d_temp{id}(in,1)-d_temp{id}(in+1,1)).^2+(d_temp{id}(in,2)-d_temp{id}(in+1,2)).^2)<15),:)
end

tmax=[];
tmin=[];
for i=1:size(bot_id,1)
    id=bot_id(i)

 K=13/sqrt(A^2*a^2+b^2*B^2);

xa{id}=d_temp{id}(:,1);
ya{id}=d_temp{id}(:,2);
ha{id}=d_temp{id}(:,3);
ts{id}=p_data{id}(:,6);
t_r{id}=d_temp{id}(:,7);
ns=ts{id}(1);



for(it=1:size(ts{id},1))
    ns=ns+ts{id}(it);
%      s_l=s_l+ts(i)*K;
    Ts{id}=[Ts{id} ;ns];
%     sl=[sl s_l];
end

% for(tl=t_r{id}(1):0.1:t_r{id}(end))
% 
% s_l=s_l+0.1*K;
% sl{id}=[sl{id} s_l];
% end





% 
% xl{id}=A*cos(a*sl{id});
% yl{id}=B*sin(b*sl{id});
% for(j=1:size(xa{id},1)-1)
%     vxa{id}=[vxa{id} ;(xa{id}(j+1)-xa{id}(j))/ts{id}(j)];
% end
% for(j=1:size(ya{id},1)-1)
%     vya{id}=[vya{id} ;(ya{id}(j+1)-ya{id}(j))/ts{id}(j)];
% end
% Va=sqrt(vxa.*vxa+vya.*vya);

tl=t_r{id}(1):0.1:t_r{id}(end);
tmax=[tmax t_r{id}(end)];
tmin=[tmin  t_r{id}(1) ];
end
tl=min(tmin):0.1:max(tmax)

for i=1:size(bot_id,1)
    id=bot_id(i)
    s_l=so{id};
for(tl=min(tmin):0.1:max(tmax))

s_l=s_l+0.1*K;
sl{id}=[sl{id} s_l];
end
xl{id}=A*cos(a*sl{id});
yl{id}=B*sin(b*sl{id});
vxl{id}=-A*a*sin(a*sl{id})*K;
vyl{id}=B*b*cos(b*sl{id})*K;
Vl{id}=sqrt(vxl{id}.^2+vyl{id}.^2);
end

tl=min(tmin):0.1:max(tmax)


for  i=1:size(bot_id,1)
id=bot_id(i);
 ya{id} = interp1(t_r{id},ya{id},tl);
 xa{id} = interp1(t_r{id},xa{id},tl);

  
dist_l{id}=sqrt((xa{id}-xl{id}).^2+(ya{id}-yl{id}).^2);

end
 for(j=1:size(xa{id},2)-1)
    vxa{id}=[vxa{id} ;(xa{id}(j+1)-xa{id}(j))/0.1];
end
for(j=1:size(ya{id},2)-1)
    vya{id}=[vya{id} ;(ya{id}(j+1)-ya{id}(j))/0.1];
end
%   vxa{id} = interp1(t_r{id}(1:size(vxa{id},1)),vxa{id},tl);
%   vya{id} = interp1(t_r{id}(1:size(vya{id},1)),vya{id},tl);
Va{id}=sqrt(vxa{id}.^2+vya{id}.^2)


hold on
% plot(xl{1},yl{1},'k',xa{1},ya{1},xa{2},ya{2},xa{3},ya{3},xa{4},ya{4},xa{5},ya{5},xa{6},ya{6},xa{7},ya{7},xa{8},ya{8})
% figure;
%  plot(tl-t_r{1}(1),dist_l{1},tl-t_r{2}(1),dist_l{2},tl-t_r{3}(1),dist_l{3},tl-t_r{1}(4),dist_l{4},tl-t_r{5}(1),dist_l{5},tl-t_r{6}(1),dist_l{6},tl-t_r{7}(1),dist_l{7},tl-t_r{1}(8),dist_l{8})
% figure
% plot(tl-t_r{6}(1),dist_l{6},'b');
% 
%  
 
 
 % subplot(2,1,1)
% hold on
% plot(tl-t_r{6}(1),xa{6},'b');
% xlabel('time (seconds) -->');
% ylabel('distance (cm) -->');
% title('Position tracking (X coordinate)')
% subplot(2,1,2)
% hold on
% plot(tl-t_r{6}(1),ya{6},'b');
% xlabel('time (seconds) -->');
% ylabel('distance (cm) -->');
% title('Position tracking (Y coordinate)');
% subplot(2,1,1)
% hold on
% plot(tl-t_r{2}(1),dist_l{2},'b');
% xlabel('time (seconds) -->');
% ylabel('distance (cm) -->');
% title('Distance between the virtual leader and the agent');
% subplot(2,1,2)
% hold on     
% plot(tl(1:size(Va{6},1))-t_r{6}(1),Va{6},'b');
%      xlabel('time (seconds) -->');
% ylabel('Velocity (cm) -->');
% title('leader and agent velocities');





% 
%   mov = avifile(strcat('trial','.avi'));
% mov.quality = 100;
% mov.fps = 10;%was 20 initially
% F = getframe(gcf); mov = addframe(mov,F);
  for j=1:size(tl',1)
      
      for i=1:size(bot_id,1)
     id=bot_id(i);
     plot(xl{id},yl{id},'k')
     hold on
     str=[ num2str(id)];
     text(xa{id}(j)+2,ya{id}(j)+10,str); 
     scatter(xa{id}(j),ya{id}(j),30,[0 0 1],'filled'); 
     scatter(xl{id}(j),yl{id}(j),30,[1 0 0],'filled'); 

%    legend('lissajous curve','Robot','Leader','Location','SouthOutside');
    

      end
 F=getframe(gcf);
%       mov = addframe(mov,F); 

    %pause(0.001)
 hold off
  end

%   mov = addframe(mov,F(i)); 
  %mov = close(mov);

  
  
  % % %
%  
% %  
% %  
 
 
 
 
 
 
 
 
 
 %  plot(tl,yl,'k',tl,ya,'r')
  
% plot(Ts(1:size(ts,1)-1),vxa,'k', Ts(1:size(ts,1)-1),vya,'g',Ts(1:size(ts,1)-1),Va,'b')
% plot(xl,yl,'k')
%
%  hold on
%  axis([-235 190 -140 155])
% axis([-50 50 -50 50])
% plot(xl,yl,'k',p_data{id}(:,1),p_data{id}(:,2),'r')
% comet(p_data{2}(:,1),p_data{2}(:,2))
grid on
%  axis equal