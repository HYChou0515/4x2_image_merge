# 4x2_image_merge
resize image and merge 8 of them into 4x2 table of image

## Usage:
  1. If the file is png, please use png2jpg to transform them to jpg.
  ```
  python3 png2jpg.py
  ```
  2. Resize the images
  ```
  python3 resize.py
  ```
  It will rotate the straight (height > width) images, and then 
  resize them to a given size (WIDTH and HEIGHT) so that height<=HEIGHT and width<=WIDTH.
  Finally, it will have a white margin to those who has height<HEIGHT and width<WIDTH
  so that height=HEIGHT and width=WIDTH.
  
  The output image is named as
  ```
  "s%d.jpg" % image_id
  ```
  3. Merge the images
  ```
  python3 merge.py
  ```
  It will merge all the images in the current directory to 4x2 image table.
  As one merged image has 8 images inside, you are supposed to have a multiplication of 8 of images
  in the current directory.
  First the program check the image size is matched.
  If the size mismatch, error message 'SIZE_ERROR' shows.
  x/y_border means the seperating border width of x/y axis of the 8 images.
  x/y_space means the margin width of x/y axis of the image.
  BIGW and BIGH means the output image size.
  So the equation should hold:
  ```
  BIGW=WIDTH*2+x_border+2xspace
  BIGH=HEIGHT*4+3y_border+2yspace
  ```
  The output image is named as
  ```
  "t%d.jpg" % image_id
  ```
