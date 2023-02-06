# BBDownEasyGUI

Simple interface that facilitates downloads from BiliBili.com, using the BBDown Tool as an intermediary. (Check out their repo: https://github.com/nilaoda/BBDown)

Non-profit and only to automate downloads. 👍

# DOCS

* English: https://docs.google.com/document/d/1H-UZlhf1KnoLo1C0FrkkUy3B1jNyVCgHoErziogNJ84
* Spanish: https://docs.google.com/document/d/1XcQ9lzWzLcbDGTV6IsACja0arwLurvx_x1vhgBE9-Ng

# USAGE

Before you can start using the GUI you need to have FFmpeg installed, visit one of the guides above to install it (depending on your language).

Once installed you can follow the steps here or in the doc, they are the same.

The first thing is to unzip the .rar in a folder (Important to have BBDownEasyGUI in the same folder as BBDown.exe).

We proceed to open BBDownEasyGUI:

![3](https://user-images.githubusercontent.com/106907367/216889199-d4319b1e-6817-4af0-940c-a8d4e66c236f.PNG)

We should see something like this. Important NOT to close the CMD that opens in the background, that's where we will see the download progress.

After that, we will load our executable (which in this case is the BBDown from the same folder)

![5](https://user-images.githubusercontent.com/106907367/216889256-4c5a9819-291f-41e8-a091-4e6fdcb305e1.PNG)

![66](https://user-images.githubusercontent.com/106907367/216889266-a47bf33f-d0c5-4ac3-9123-988458ef861c.PNG)

Once the console displays "Executable loaded!", the BBDown is ready to be executed.

Now we have 2 parameters to add. In the first one we are going to enter the ULR of the video.
* The url input format is filtering after "/video/". 
* Example: "https://www.bilibili.com/video/BV1U84y1s71t/?vd_source=25b47ea4aaceb21f75a622726184c4c8". From this link the only thing we are interested in is "BV1U84y1s71t" to enter in the box of parameter 1.

![7](https://user-images.githubusercontent.com/106907367/216889615-85077d2f-9356-4ca1-8e25-3e5e5e7bf57f.PNG)

And in the second parameter, we have to enter the available commands that the tool has.

![8](https://user-images.githubusercontent.com/106907367/216889662-ccaf06ee-2063-4455-a014-f4dbdfd2a401.PNG)

* To download in 1080p you only need to add the -tv. 
* Here are some of the parameters that I have personally tested and have worked correctly for me (will be updated as I discover more BiliBili)

![screenshot-docs google com-2023 02 06-02_20_31](https://user-images.githubusercontent.com/106907367/216889859-3a863204-ed64-48a8-b161-197167211705.png)

Thank you Snowy for recommending the subtitles parameter.
 
 Once the 2 parameters are ready, just click on the "Download Video!" button.
 
 If you followed everything to the letter, you should be seeing something like this:
 
![9](https://user-images.githubusercontent.com/106907367/216889917-1cf034be-d636-476a-a25c-f7396a7a6eb2.PNG)

Once the weird characters stop coming out, you can go back to the folder where you left the .exe's and bam! You should have a 1080 video 👍

![00](https://user-images.githubusercontent.com/106907367/216890000-4dea2532-8e02-422c-b142-97401d68c821.PNG)

* Most likely if you downloaded a VERY large file, it will take a while for it to appear in mp4 format and in your case you will have a folder with loose files. You just have to wait a while (depending on your PC) for the .MP4 file to appear with everything (Ty Zhika for the warning).

# Errors and Updates

* I will try to keep the guide updated both this and the DOCS guide (the latter is a bit more detailed, visit it).
* You may suffer or feel the pc lags after making a very large download (+ 2GB), it is normal since the post processing is being done in the back.

* In case of bugs with the interface or other doubts or suggestions, you can contact me via Discord: Jaruna#2496

I am not a programmer, but I will be accepting feedback and working to improve 👍.





