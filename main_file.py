from ArabicOcr import arabicocr
import pandas as pd
import numpy as np 
import math 
import matplotlib.pyplot as plt
import cv2

# image path ( change the name of the file )
image_path='images/image1.jpeg'

# output image file
out_image='output_image/out11.jpeg'
results=arabicocr.arabic_ocr(image_path,out_image)


# read the extracted image
img = cv2.imread('output_image/out11.jpeg', cv2.IMREAD_UNCHANGED)

extracted_text = []
ser_number = []

# seperate out the extracted text with the serial number

for i in range(len(results)): 
  # org 
  org = results[i][0][1]
  org = [int(x) for x in org]
  #font  
  font = cv2.FONT_HERSHEY_SIMPLEX 

  # fontScale 
  fontScale = 1
    
  # Blue color in BGR 
  color = (255, 0, 0) 
    
  # Line thickness of 2 px 
  thickness = 1
    
  #text
  text = str(i+1)

  # save the result in a list 
  extracted_text.append(results[i][1])
  ser_number.append(int(text))
  # Using cv2.putText() method 
  image = cv2.putText(img, text, org, font,  
                    fontScale, color, thickness, cv2.LINE_AA) 

plt.figure(figsize=(10,10))
plt.imshow(img)


# converting the text (arabic) and the serial numbers of annotation into dataframe 
# which is to be saved in csv format
Data = pd.DataFrame(np.array([ser_number,extracted_text]).T,columns=['AnnotationNum',
                                                                     'ExtractedText'])

# daving the dataframe into csv file 
Data.to_csv('output_csv/output_file.csv')
