clear;
cam = webcam;
buffer = {};
img = snapshot(cam);
images = {};
imshow(img);
step = 20;
buffsize = size(img,1)/step;
blocksize = size(img,1)/buffsize; %%yes, step and blocksize are the same val


for i = 1:buffsize
    images{i} = img;
end

for frame = 1:300
    img = snapshot(cam);
    
    output = [];
    
    for i = 0:buffsize-1
        current = images{i+1};
        block = current(1+i*blocksize:step+i*blocksize,:,:);
        output = vertcat(output,block);
        
        %cycle buffer
        if i ~= buffsize-1
            images{i+1} = images{i+2};
        end
        
        
    end
    images{buffsize} = img;
    imshow(output);
   
    
   %cycle buffer
%    for i = 1:buffsize-1
%         
%        images{i} = images{i+1};
%        
%    end
%    images{buffsize} = img;
    
end

clear;