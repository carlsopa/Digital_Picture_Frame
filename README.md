<h3><b>Digital Picture Frame</h3></b>

The idea for the project came when trying to figure out what to get my dad for Christmas last year. He loves to take photos and so I started to look for a digital photo frame. The only problem, is that they would only show one picture at a time, and not adjust for orientation. So, I set out to do better, and created my own digital picture frame.

<b>What it does:</b><br>
Using a Raspberry Pi for the brains, and a portable hard drive pictures are randomly selected and displayed on a 24" screen. The screen display is set to show three photos in landscape and two in portrait orientation at the same time. The program will also take into account any photos were the camera was held "upside down" (we have all done it), and will flip it right side up. Two ways to upload photos are either by USB or a simple web interface that can be used on either mobile or desktop.

<b>How it works:</b><br>
The main program is written in PYTHON utilizing the PYGAME module to create a full screen display. All files that are uploaded are saved to a portable harddrive to prevent constant read/writes against the SD card in side the Raspberry Pi. The program will scan over all the meta data of the pictures to determine size and orientation, this will determine which list it goes in. The software will then randomly choose a number between 0 and the max list size to select a photo to display. A simple fade in and out using opacity will shift between photos. The interface for managing photos is a basic HTML & PHP page that allows you to upload photos and delete them from the harddrive. This is served on the Raspberry Pi using a lightweight APACHE server.

<b>File Descriptions:</b><br>
<ul>
<li><i>PhotoDeletion.php</i><br>
Basic webpage that will allow for the deletion of photos from the harddrive.  It will display a table with a thumb nail version of the photo, name and size.  A third column has a button that will delete the corresponding photo when clicked.  Deletion is based on the name of the photo.</li>

<li><i>PhotoUpload.php</i><br>
Simple webpage for uploading photos.  Provides a button to click that will open a dialog box.  Once you select all the photos that you want to upload, it will show you the total amounts.  Click the upload button and it will upload them all to a temporary folder on the Raspberry Pi which will then get moved over by the main program to the main folder.

<li><i>USB_Upload.py</i><br>
Python script that will detect any media devices connected through USB and then transfer the photos over to the raspberry pi.
</ul>

View a video explanation & demonstartion <a href="https://www.youtube.com/watch?v=A6njWGrcZDk">Digital Picture Frame</a>
