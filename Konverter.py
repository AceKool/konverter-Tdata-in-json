import os
import json


def convert_tdata_to_session_json(tdata_dir, output_file):
    session = {}

    for file_name in os.listdir(tdata_dir):
        if file_name.endswith('.dat'):
            with open(os.path.join(tdata_dir, file_name), 'rb') as file:
                content = file.read()
                session[file_name] = content

    with open(output_file, 'w') as file:
        json.dump(session, file, indent=4)


tdata_dir = "C:\\Users\\fed64\\AppData\\Roaming\\Telegram Desktop\\tdata"
output_file = "C:\\Users\\fed64\\Desktop\\sessions.json"

convert_tdata_to_session_json(tdata_dir, output_file)