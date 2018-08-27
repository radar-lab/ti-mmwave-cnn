data = csvread('./output/pred.csv');
plot(data)
ylim([-.5,1.5])
legend('Nothing','Walking','Waving hands')