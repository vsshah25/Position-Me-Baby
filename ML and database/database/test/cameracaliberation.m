 close all
% clear all
clc; close all; clear all
cam=webcam('Logitech HD Webcam C270');
set(cam,'Resolution','640x480')
load('cameraparameters.mat')
im=snapshot(cam);
imc=cell(4,1);

im=imcrop(im,[228 271 144 415]);
% imshow(im);
unim = undistortImage(im, cameraParams);
% figure;
imshow(unim);

p1=[638 103];
p2=[605 71];
p3=[643 70];
p4=[638 103]
angle=(atan2(-(p1(2)-p2(2)),(p1(1)-p2(1)))-atan2(-(p3(2)-p2(2)),(p3(1)-p2(1))))*180/pi

% imtool(im);
% imwrite(im,'61.png')
