#pip install matplotlib
import matplotlib.pyplot as plt

#name of items
lables = 'Python', 'Java' , 'C++', 'R', 'Ruby','C#'
#items percentage
percentage = [60.4,16.44,10.21,2.18,2.02,12.02]

patches , texts = plt.pie(percentage,labels=lables)

percentage_label = ["{}%".format(i) for i in percentage]

plt.legend( patches, percentage_label, loc = 'upper right')

plt.show()
