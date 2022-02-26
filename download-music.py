import yaml
import os

with open("linklist-music.yaml", "r") as yamlfile:
    try:
        config = yaml.safe_load(yamlfile)

        for entry in config:
            print(f"\033[92mGrabbing '{entry['url']}':")

            folderName = entry["folder-name"] if "folder-name" in entry else "/\%(uploader)s"  
            
            os.system(f"""
                yt-dlp
                -c
                --extract-audio
                --audio-format mp3
                --merge-output-format mkv
                -o 'music/{folderName}/%(title)s.%(ext)s'
                --extractor-args youtube:player_client=android
                --throttled-rate 100M
                --restrict-filenames
                --download-archive alreadydownloaded-music.txt
                '{entry['url']}'
                """.replace('\n', " ")
            )
                

    except yaml.YAMLError as exc:
        print("You fucked up the yaml format.")

