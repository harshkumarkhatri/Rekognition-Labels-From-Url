# Rekognition Labels from URL
* This repo has the code with the help of which we can directly get labels for an image from its url.
* We dont have to save the image to our local storage.
* This can be used to analyze labels from the files we are uploading in our cloud or some other cloud.
* It can also be used to control the uploads based on the labels.
* If we are using cloudinary as our cloud provider to store our media files then this could result as a good option.
* This repo has another file `util.py` which has a function to resize and convert thee image into bytes. We can use that as well.<br>
  But here better option is `io.ByteIO()`.
  ___
I have used this as a part of another project to detect whether the images which are uploaded are offensive or inappropriate or not. If thy are then they won't be uploaded and if they are not they will be uploaded to the webapp in the S3 bucket.
  ___
Built using
  * Flask
  * AWS rekognition
  * Boto
  * PIL
  * Requests
  ___
  Amazon Rekognition API used<br>
  ![Amazon Rekognition](https://res.cloudinary.com/harshkumarkhatri/image/upload/v1593625581/readme%20images/rekognition%20lables%20from%20url/Screenshot_at_2020-07-01_23-10-40_bc7yze.png)
  <br>
  A snap from the similar usage<br>
  ![A snap from the similar usage](https://res.cloudinary.com/harshkumarkhatri/image/upload/v1593625583/readme%20images/rekognition%20lables%20from%20url/Screenshot_at_2020-07-01_23-11-13_clvntc.png)

