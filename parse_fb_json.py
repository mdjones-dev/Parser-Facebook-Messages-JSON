import json
import datetime
import sys
import glob
import argparse

try:

    main_desc = """
This program processes the JSON output of the Facebook 
download for messages, located in the 
messages/inbox/{example_person} folder.

All JSON files in the directory of this script will be 
identified and processed sequentially, appended to the 
same output files.

The output consists of 3 files separated into each type 
of message Facebook records:
    Generic - Messaging / sending photos / videos
    Call - Call events pre-2019 May 16 are recorded as a 
            type:Call and a call_duration is logged in 
            seconds. Call events after this date are 
            recorded by Facebook as type:Generic without 
            call_duration.
    Share - Example: links to websites.
        
        
    """

    parser = argparse.ArgumentParser(
        description=main_desc,
        formatter_class=argparse.RawTextHelpFormatter
        )

    # Temporary assignment for help message (python parse.py --help)
    temp_facebook_name_id = "Bob"
    
    temp_call_strings_copy = ["The video chat ended.",
    f"You missed a call from {temp_facebook_name_id}.",
    f"You missed a video chat from {temp_facebook_name_id}.",
    "Your video has ended."
    "You started sharing video.",
    "You stopped sharing video.",
    f"You and {temp_facebook_name_id} can now see each other.",
    f"{temp_facebook_name_id} started sharing video.",
    f"{temp_facebook_name_id} stopped viewing your video.",
    f"{temp_facebook_name_id} stopped sharing video.",
    f"{temp_facebook_name_id}'s video has ended.",
    f"{temp_facebook_name_id} missed your video chat.",
    f"{temp_facebook_name_id} called you."]
    
    newlinetab = "\n\t"
    
    parser.add_argument('name', type=str, help=f"""Provide the name Facebook uses to identify the person you're talking to 
regarding call messages.
Example of the strings where you can find this:
{newlinetab.join([n for n in temp_call_strings_copy if temp_facebook_name_id in n])}""")
    parser.add_argument('output', type=str, help="Provide a name for the output file.")
    parser.add_argument('--delimiter', type=str, default=';', help="""Provide a delimiter for the output, a single character 
that is unlikely to appear in any messages.""")

    args = parser.parse_args()
    
    DELIMITER = args.delimiter
    facebook_name_id = args.name
    output_name = args.output       
    # Arguments / Inputs for the program have been assigned
    
    # Define the strings used to recognise calls
    call_strings = ["The video chat ended.",
    f"You missed a call from {facebook_name_id}.",
    f"You missed a video chat from {facebook_name_id}.",
    "Your video has ended."
    "You started sharing video.",
    "You stopped sharing video.",
    f"You and {facebook_name_id} can now see each other.",
    f"{facebook_name_id} started sharing video.",
    f"{facebook_name_id} stopped viewing your video.",
    f"{facebook_name_id} stopped sharing video.",
    f"{facebook_name_id}'s video has ended.",
    f"{facebook_name_id} missed your video chat.",
    f"{facebook_name_id} called you."]
    
    # Find all json files in this directory
    json_files = glob.glob("message_*.json")

    # Read in each json file and append to a list
    all_messages_list = []
    for file in json_files:
        with open(file, "r") as f:
            all_messages_list.append(json.load(f))
        
    # Name of the output files
    fname_generic = "{}_messages_generic.txt".format(output_name)
    fname_call = "{}_messages_call.txt".format(output_name)
    fname_share = "{}_messages_share.txt".format(output_name)
        
    # Create each empty file for now
    with open(fname_generic, "w") as f:
        pass

    with open(fname_call, "w") as f:
        pass
        
    with open(fname_share, "w") as f:
        pass
            
    # Headers (determined from manual inspection of the JSON files)
    # sender_name, timestamp_ms, content, reactions [ reaction, actor, type ] type
    messages_generic = []
    # sender_name, timestamp_ms, content, call_duraction, type
    messages_call = []
    # sender_name, timestamp_ms, content, share [link], type
    messages_share = []

    # Define the first line in each file, spreadsheet headers
    messages_generic.append("timestamp_ms{0}type{0}sender_name{0}content".format(DELIMITER))
    messages_call.append("timestamp_ms{0}type{0}sender_name{0}content{0}call_duration".format(DELIMITER))
    messages_share.append("timestamp_ms{0}type{0}sender_name{0}share [link]".format(DELIMITER))

    # When reading a value, replace newlines and occurances of the delimiter with a space to ensure they do not interfere with the output/CSV files.
    def return_safe_value(item, key):
        if key in item:
            return "{}".format(item[key]).replace("\r\n", " ").replace("\r", " ").replace("\n", " ").replace(DELIMITER, " ")
        
        return -1
    
    # This function reads in each JSON file separately, then sorts each line into one of the 3 files Generic/Call/Share. 
    # It also converts the timestamp into a readable format.
    def process_file(json_data):
        
        # Print headers
        #for header in json_data:
            #print(header)

        try:
            for item in json_data["messages"]:
            
                # Add items to this line until it's ready to append to a list
                line = []
                
                keys = []
                
                # STEP 1 out of 3 - Find out all the keys stored for this line.
                for key, value in item.items():
                    keys.append(key)
                        
                
                # STEP 2 out of 3 - If the keys exist append them to a line
                if "timestamp_ms" in keys:
                    value = "{}".format(datetime.datetime.utcfromtimestamp(item["timestamp_ms"]/1000))
                    line.append(value)
                    
                if "type" in keys:
                    value = return_safe_value(item, "type")
                    line.append(value)
                
                if "sender_name" in keys:
                    value = return_safe_value(item, "sender_name")
                    line.append(value)
                    
                # Through manual inspection of the JSON file, this key only occurs for Call events.
                # Messages post 2019 May 15 Call events that are recorded as type:Generic can be 
                # determined from the existence of the content key.
                if "content" in keys:
                    value = return_safe_value(item, "content")
                    line.append(value)
                    if value in call_strings:
                        item["type"] = "Call"
                    
                if "gifs" in keys:
                    value = return_safe_value(item, "gifs")
                    line.append("GIF Sent: {}".format(value))
                    
                if "call_duration" in keys:
                    value = return_safe_value(item, "call_duration")
                    line.append(value)
                    
                if "share" in keys:
                    value = return_safe_value(item, "share")
                    line.append("Link Sent: {}".format(value))
                    
                if "photos" in keys:
                    value = return_safe_value(item, "photos")
                    line.append("Photo Sent: {}".format(value))

                #reactions = item["reactions"]
                
                # STEP 3 out of 3 - Every line has a key called type. 
                # This determines which of the 3 output files this line is written to.
                if item["type"] == "Call":
                    csv_line = DELIMITER.join(line)
                    if csv_line not in messages_call:
                        messages_call.append(csv_line)
                        
                if item["type"] == "Generic":
                    csv_line = DELIMITER.join(line)
                    if csv_line not in messages_generic:
                        messages_generic.append(csv_line)
                        
                if item["type"] == "Share":
                    csv_line = DELIMITER.join(line)
                    if csv_line not in messages_share:
                        messages_share.append(csv_line)
                    
        except Exception as ex:
            print("Error: {}".format(ex))
            
    # Process the messages from Facebook (JSON)
    print(f"Processing json file(s) {json_files}")
    for message in all_messages_list: # All JSON files are processed here
        process_file(message)
    print("Finished processing file.")

    # Write to files
    print(f"Writing to files:\n   {fname_generic}\n   {fname_call}\n   {fname_share}")
    try:
        with open(fname_generic, "a", encoding="utf-8") as f:
            for line in messages_generic:
                f.write("{}\n".format(line))
        with open(fname_call, "a", encoding="utf-8") as f:
            for line in messages_call:
                f.write("{}\n".format(line))
        with open(fname_share, "a", encoding="utf-8") as f:
            for line in messages_share:
                f.write("{}\n".format(line))
    except Exception as ex:
        print(ex)
        
    print("Finished.")
    
except Exception as ex:

    print(f"Error occured: {ex}")
    

    