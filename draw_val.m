clear all; close all;

color = [[0, 0.4470, 0.7410],
    [0.8500, 0.3250, 0.0980]];
data = csvread("mat.csv");
figure
hold on
plot(data(1:10),'-o','color',color(1,:),'LineWidth',2,'MarkerFace',color(1,:),'MarkerSize',5)
plot(data(11:20),'-o','color',color(2,:),'LineWidth',2,'MarkerFace',color(2,:),'MarkerSize',5)
grid on
ylim([.9,1])
xlim([0,10])
xlabel('Epoch Num')
ylabel('Accuracy')
title('Training and validation Accuracy')
legend('Training','Validation')

figure
hold on
plot(data(21:30),'-o','color',color(1,:),'LineWidth',2,'MarkerFace',color(1,:),'MarkerSize',5)
plot(data(31:40),'-o','color',color(2,:),'LineWidth',2,'MarkerFace',color(2,:),'MarkerSize',5)
grid on
ylim([0,.3])
xlim([0,10])
xlabel('Epoch Num')
ylabel('Loss')
title('Training and validation Loss')
legend('Training','Validation')