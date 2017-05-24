Digital picture frame on the raspberry pi.

For Christmas this past year, I was trying to come up with something to get my parents who loves to take photos.  Which got me thinking about a digital photo frame.  Not a bad idea, except that it is only one photo at a time, and when he has literally thousands, not the best option.  And then it came to me, why not a digital collage photo frame!  Thus was born, my digital photo frame.

The whole system is powered and runs on a raspberry pi 3.  The screen of the frame is a 24" LCD monitor connected by HDMI to the pi.  To solve the issue of storage, I have a portable 500gb hard drive mounted to the pi.  All the peices are velcroed to the back of the monitor, to give it a clean look.  Toping it off, I had a local framer install a picture frame around the outside of the whole thing.  It will not set flush against a wall when hung, or can be used with the stand to set on a counter or display.

One concern I had from the start is about putting photos on.  Sure I can do that, and set it up easily enough for my parents, but what about in 2 months after their next vacation?  Taking that into concideration, I have set it up so that you can remotely add and delete photos.  An apache server running on the pi, allows you to connect and control the photos.  I also had a female USB extension on the side of it, that they can connect a flash drive to and upload photos that way as well.

All in all, the whole idea is built around simplicity, which I think i have accomplished here.
