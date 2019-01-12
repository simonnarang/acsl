clear

for c = 1:5
in=input('enter your number and digit rate: ','s')

in=strsplit(in,' ');
n=str2num(in{2});
in=in{1};

mySum=0;

for i=1:length(in)-n+1

current=in(i:i+n-1);
mySum = mySum + str2num(current);

end

disp(num2str(mySum))
end
