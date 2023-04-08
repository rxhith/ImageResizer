import cv2
source="snapchat-1961109027.jpg"
destination="flat_new.png"
image = cv2.imread(source)
#cv2.imshow("flat",src)
#cv2.destroyAllWindows() #closes all open windows
scale_percent=50
#shape[0] means height
#shape[1] means width
new_height=int(image.shape[0] * scale_percent/100 )
new_width=int(image.shape[1] * scale_percent/100 )
new_image=cv2.resize(image,(new_height,new_width))
cv2.imwrite(destination,new_image)
#cv2.waitKey(0) #waits for an event

#to just display image
""" image = cv2.imread(source)
    cv2.imshow("flat",image) #filename is imp
    cv2.waitKey(0)
    cv2.destroyAllWindows()
"""
