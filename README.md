README

**Flood Map downloader script using selenium and Edge Webdriver in Python**
----------------------------------------------------------------------------

What this does
**************
This script automates downloading flood maps from https://maps.cyfoethnaturiolcymru.gov.uk/ (Natural Resources Wales' Flood Risk Map Viewer)

How to use
***********
You need to download msedgedriver.exe . One is included in the package but you might need to download another corresponding to  edge browser version. Use the link 
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/ 
to download your driver.

There are so many dependencies that you would need for this script to work.

Main being selenium (prefferably 3.xx version as I don't know whether 4.xx will work or not. I have not tested)

Other main dependencies are given below. There might be other dependencies. Please follow python instruction to install it accordingly

1. pyautogui
2. pandas
3. openpyxl

An excel template is provided with. You need to fill in the locations you need your flood maps for. The columns Structure Name and Location Coords are mandatory. Structure name need not be in the given format, but it should be unique to each Location Coords as these are used to name the PDF Files. (i.e, no two Structure Name shall be same)
Location Coords can be anything that map accepts as an address. For eg: Grid Reference, Post Code etc.

Steps to be followed
********************
1. Fill in the cordinates sheet, place it in a folder
2. Give the path to the excel fil in line 8.
3. Make a folder where you want to download your PDF's
4. Give the path to download folder in line line 55 (keep the last portion %s.pdf intact)
5. Press run.

Note
****
Sometimes the website doesn't load because of network issues or if the site itself is down and the script will fail. You have to wait for the site to be back online or network to be restored before running again.

I have given timeouts in several stages for the smooth running of the script. If the timeout is exceeded for any stage, the script may give undesired results or throw an error. Please check all PDF's once the script completes running and make sure everything is all right. If you are getting erroneous maps for some structures, run the script again after making necessary changes in the excel sheet. (Remember to delete the existing erroneous PDF files before running the script again).

On average, it takes 30 seconds to download and save single PDF. Please don't do anything else on the computer while the script is running. This might hinder the functioning of pyautogui while saving the file. Run the script and wait for it to complete before you do anything else in the computer (I know this doesn't make sense for an automation script but I couldn't find a way to save the file using selenium. You are welcome to contribute)

Contact
*******
Sreejith Parippayi
sreejith.parippayi@atkinsglobal.com
sreejithpro@gmail.com
https://github.com/sreejithpro



