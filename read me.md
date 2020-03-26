* This repo has the code with the help of which we can directly get labels for an image from its url.
* We dont have to save the image to our local storage.
* This can be used to analyze labels from the files we are uploading in our cloud or some other cloud.
* It can also be used to control the uploads based on the labels.
* If we are using cloudinary as our cloud provider to store our media files then this could result as a good option.
* This repo has another file `util.py` which has a function to resize and convert thee image into bytes. We can use that as well.<br>
  But here better option is `io.ByteIO()`
