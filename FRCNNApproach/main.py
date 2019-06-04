# importing required libraries
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches

# read the csv file using read_csv function of pandas
train = pd.read_csv("annotate.txt", header=None)
print(train.head())


fig = plt.figure()

#add axes to the image
ax = fig.add_axes([0,0,1,1])

# read and plot the image
image = plt.imread('train/apple_11.jpg')
plt.imshow(image)

# iterating over the image for different objects
for _,row in train[train[0] == "train/apple_11.jpg"].iterrows():
    xmin = row[1]
    ymin = row[2]
    xmax = row[3]
    ymax = row[4]
    
    width = xmax - xmin
    height = ymax - ymin
    
    # assign different color to different classes of objects
    if row[5] == 'banana':
        edgecolor = 'r'
        ax.annotate('banana', xy=(xmax-40,ymin+20))
    elif row[5] == 'apple':
        edgecolor = 'b'
        ax.annotate('apple', xy=(xmax-40,ymin+20))
    elif row[5] == 'orange':
        edgecolor = 'g'
        ax.annotate('orange', xy=(xmax-40,ymin+20))
        
    # add bounding boxes to the image
    rect = patches.Rectangle((xmin,ymin), width, height, edgecolor = edgecolor, facecolor = 'none')
    
    ax.add_patch(rect)
plt.show()