annotations = glob('train/*.xml')
data = pd.DataFrame()
df = []
cnt = 0
for file in annotations:
    prev_filename = file.split('\\')[-1].split('.')[0] + '.jpg'
    #filename = str(cnt) + '.jpg'
    #print(prev_filename)
    row = []
    parsedXML = ET.parse(file)
    for node in parsedXML.getroot().iter('object'):
        class_type = node.find('name').text
        xmin = int(node.find('bndbox/xmin').text)
        xmax = int(node.find('bndbox/xmax').text)
        ymin = int(node.find('bndbox/ymin').text)
        ymax = int(node.find('bndbox/ymax').text)
        
        
        row = [prev_filename + ',' + str(xmin) + ',' + str(ymin) + ',' + str(xmax) + ',' + str(ymax) + ',' + class_type]
        df.append(row)
        cnt += 1
        

data = pd.DataFrame(df, columns=['format'])

data.to_csv('annotate.txt', header=None, index=None, sep=' ')

