# SpyderChat

[TOC]

## 0. Description

*SpyderChat* is a scrapper tool to analyze the data from chat groups in whatsapp. After you run the code you will get plots showing data about the users and interactions.

## 1. Installation

### Installing python 3

Make sure you have python 3.x.x installed in your computer. You can get the latest release from the official website: 

https://www.python.org/downloads/

- Windows: https://www.python.org/downloads/windows/
- Linux/UNIX: https://www.python.org/downloads/source/
- Mac OS X: https://www.python.org/downloads/mac-osx/



If you want to check your python version installed you can type the following codes in your computer:

- Windows:

  1. WinKey + R

  2. Type 'cmd'  and press ENTER

  3. Type 'python3 --version' in the console and press ENTER

     ```
     python3 --version
     output: Python 3.6.9
     ```

- Linux/UNIX:

  1. Press CTRL + ALT + T

  2. Type $ python3 --version and press ENTER

     ```
     $ python3 --version
     output: Python 3.6.9
     ```

     

- Mac OS X: 

  1. Go to Applications/Utilities

  2. Click Terminal

  3. Type $ python3 --version and press ENTER

     ```
     $ python3 --version
     output: Python 3.6.9
     ```



### Downloading SpyderChat

Download the release or download the SpyderChat.py file and save it in a new folder.



## 2. Usage

### Phone instructions:

1. Open WhatsApp
2. Open the chat group to analyze
3. Open the chat options '...' (The 3 vertical dots) and press *more*
4. Press *Export chat* (select *Without files*)
5. Send the file to your computer and save it in the same folder you downloaded the SpyderChat.py

### PC instructions:

Before continue make sure you have the txt file generated from WhatsApp and the SpyderChat.py in the same folder.

- Windows:

  1. New content

     ```
     $ python3 SpyderChat.py
     Please type the file to analyze. Ex: chat.txt  >>>MyChat.txt
     ```

     

- Linux/UNIX:

  1. Open Linux console in the folder (right click in the folder and select *Open in terminal*)

  2. Type $ *python3 SpyderChat.py* and press ENTER

  3. Follow the instructions and enter the file name you want to analyze 'Example.txt' and press ENTER

  4. Open the new *SpyderResults* folder generated and enjoy the plots

     ```
     $ python3 SpyderChat.py
     Please type the file to analyze. Ex: chat.txt  >>>MyChat.txt
     ```

     

- Mac OS X:

  1. New content

     ```
     $ python3 SpyderChat.py
     Please type the file to analyze. Ex: chat.txt  >>>MyChat.txt
     ```

     

##  3. Troubleshooting

By default the words analyzed are manually inserted in the raw code, you could modify this words manually or just run the code and discard this plot. I expect to fix this in the next update.

## 4. Disclaimer

This is a proof of concept showcasing how conversations from whatsapp can be analyzed. This is intended for educational purpose only.

Do not use this for any commercial nor redistribution purpose. Actually, the use of such tool might be allowed for private read-only use, as this is what happens when crawling Whatsapp, but not beyond. I do not take responsibility for any use of this tool.

## 5. Help Wanted

This repository does provide the required python version, you should install it by your own

## 6. Other links

To find more projects, resources, articles and more you can visit my site http://carlosgrande.me/