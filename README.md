# Parser-Facebook-Messages-JSON
Used on the Facebook archive download (JSON). 

This script parses the .json files for private messages located in the `messages/inbox`. 
The output provides 3 text files for `Generic`, `Call`, and `Share` messages. 
The initial inspiration for this project was to collate a clean `Call` log.

<h1>Step 0. Download the python script:</h1>
Download the ZIP file.
  
Contained within is the parse_fb_json.py file.
<img src="https://github.com/mjones-l/Parser-Facebook-Messages-JSON/blob/master/resources/Step0DownloadScript.JPG">

<h2>Step 1. Install Python 3.8 (Windows Store, or python[.]org)</h2>

<img src="https://github.com/mjones-l/Parser-Facebook-Messages-JSON/blob/master/resources/Step1Python.png">

<h2>Step 2. Open `Windows PowerShell`, type the following command and press ENTER.</h2>

`python --version`

<img src="https://github.com/mjones-l/Parser-Facebook-Messages-JSON/blob/master/resources/Step2aPowerShell.png">

<img src="https://github.com/mjones-l/Parser-Facebook-Messages-JSON/blob/master/resources/Step2bPythonVersion.png">

<h2>Step 3. Locate the desired messages folder and open `PowerShell` in this directory</h2>

Example:  C:\Users\\`{user}`\Downloads\\`{name_of_download}`\\messages\inbox\\`{PersonName}_{random numbers}`

Open the directory in `File Explorer`, `Hold SHIFT + Right Click` on empty space. (see below) You may need to try this a few times to get the PowerShell option to appear.

<h3>Troubleshooting:</h3>  

Some views in File Explorer provide no free space to SHIFT + Right Click, try a tiled view.
<img src="https://github.com/mjones-l/Parser-Facebook-Messages-JSON/blob/master/resources/Step3bTroubleshooting.JPG">

<img src="https://github.com/mjones-l/Parser-Facebook-Messages-JSON/blob/master/resources/Step3InboxFolderOpenPowerShell.png">

<h2>Step 5. Type the following `PowerShell` command and press ENTER: </h2>

`select-string “ called you.” *.json`

Note1: This is to find the name Facebook uses to identify your partner. In this case mine is `Ye`

<img src="https://github.com/mjones-l/Parser-Facebook-Messages-JSON/blob/master/resources/Step5FindFacebookName.png">

<h3>Troubleshooting</h3>: Below are all the lines that can be used to identify the name facebook is using to identify them in Call events. These are also referenced in `parse_fb_json.py`, lines 71-83: 

`You missed a call from `

`You missed a video chat from `

` can now see each other.`

` started sharing video.`

` stopped viewing your video.`

` stopped sharing video.`

`'s video has ended.`

` missed your video chat.`

` called you.`

<h2>Step 6. Place the python script in the message folder.</h2>

Refer back to Step 3, the desired message folder, and the ZIP file downloaded in Step 0.

Extract parser_fb_json.py from the ZIP file and place it in the desired message folder.

<h2>Step 7. Type the following PowerShell command and press ENTER: </h2>

Refer to the facebook name you found in Step 5.

`python parse_fb_json.py {name} output`

Example if the name found in Step 5 is `Ye`

`python parse_fb_json.py Ye output`


Note1: this command assumes `parse_fb_json.py` and all JSON files are in the same folder.

<img src="https://github.com/mjones-l/Parser-Facebook-Messages-JSON/blob/master/resources/Step6aRunScript.png">

Well Done! You can now see the additional 3 files in the directory. If you would like to import the data into Excel feel free to continue on to Step 8.

<img src="https://github.com/mjones-l/Parser-Facebook-Messages-JSON/blob/master/resources/Step6bSeeResultingFiles.png">

<h2>Step 8. The three files can be imported into Microsoft Excel (see Data tab).</h2>
  
Make sure to select the `delimiter` as `;` a semi-colon.

<img src="https://github.com/mjones-l/Parser-Facebook-Messages-JSON/blob/master/resources/Step7aImportSpreadsheet.png">

Note: All times recorded by Facebook are in UTC (0000).

<img src="https://github.com/mjones-l/Parser-Facebook-Messages-JSON/blob/master/resources/Step7bImportDelimiter.png">

Note1: I have noticed Facebook no longer records `Calls` as a separate type, post-15/05/2019 they’re recorded as a `Generic` message, there is no way to determine the `call duration` from this data.

Note2: `call duration` is measured in seconds.

<img src="https://github.com/mjones-l/Parser-Facebook-Messages-JSON/blob/master/resources/Step7cNoteStrange.png">



