# Parser-Facebook-Messages-JSON
Used on the Facebook archive download (Format: JSON). 
Please see the following link for help downloading your facebook data https://www.facebook.com/help/212802592074644

This script parses the .json files for private messages located in `messages/inbox`. 
The output provides 3 text files for `Generic`, `Call`, and `Share` messages. 
The initial inspiration for this project was to collate a clean `Call` log.

<h2>0. Download the python script:</h1>
Download this project to a ZIP file.
  
Contained within is the parse_fb_json.py file.

<h2>1. Install Python 3.8 (Windows Store, or python[.]org)</h2>

<h2>2. Open `Windows PowerShell`, type the following command and press ENTER.</h2>

`python --version`

Just make sure the version is 3.8 or greater. Last tested with Python 3.8.5.

<h2>3. Locate the desired Facebook messages folder and open PowerShell</h2>

Example:  C:\Users\\`{user}`\Downloads\\`{name_of_download}`\\messages\inbox\\`{PersonName}_{random numbers}`

Open the directory in `File Explorer`, `Hold SHIFT + Right Click` on empty space. You may need to try this a few times to get the PowerShell option to appear.

<h3>Troubleshooting:</h3>  

Some views in File Explorer provide no free space to SHIFT + Right Click, try a tiled view.

<h2>5. Type the following `PowerShell` command and press ENTER: </h2>

`select-string “ called you.” *.json`

Note1: This is to find the name Facebook uses to identify the other user.

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

<h2>6. Place the python script in the message folder.</h2>

Refer back to Step 3, the desired message folder, and the ZIP file downloaded in Step 0.

Extract parser_fb_json.py from the ZIP file and place it in the desired message folder.

<h2>7. Type the following PowerShell command and press ENTER: </h2>

Refer to the facebook name you found in Step 5.

`python parse_fb_json.py {name} output`

Example if the name found in Step 5 is `XX`

`python parse_fb_json.py XX output`

This command assumes `parse_fb_json.py` and all JSON files are in the same folder.

**Well Done!**

You can now see the additional 3 files in the directory. If you would like to import the data into Excel feel free to continue on to Step 8.

<h2>8. The three files can be imported into Microsoft Excel from the Data tab.</h2>
  
Make sure to select the `delimiter` as `;` a semi-colon.

**Notes:**

All times recorded by Facebook are in UTC (0000).

I have noticed Facebook no longer records `Calls` as a separate type, post-15/05/2019 they’re recorded as a `Generic` message, there is no way to determine the `call duration` from this data.

Edit: I downloaded another copy of my data a few months later and found the call_duraction was back for those missing calls. I can't explain this magic, I just have to accept what Facebook gives me. So if you find that your latest calls are saved as a 'Generic' type, try and redownload in a week or so.

`call duration` is measured in seconds.

