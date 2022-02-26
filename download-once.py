# This script is for downloading stuff ONCE. This is for, let's say, playlists that will never change again that you want to download.
import yaml
import os

with open("once.yaml", "r") as yamlfile:
    try:
        config = yaml.safe_load(yamlfile)

        for entry in config:
            print(f"\033[92mGrabbing {entry['type']} '{entry['url']}':\033[1m")
            if entry["type"] == "music":

                os.system(f"""
                    yt-dlp
                    -c
                    --extract-audio
                    --audio-format mp3
                    -o 'music/{entry['folder-name']}/%(title)s.%(ext)s'
                    --extractor-args youtube:player_client=android
                    --throttled-rate 100M
                    --restrict-filenames
                    --download-archive alreadydownloadedonce-music.txt
                    '{entry['url']}'
                    """.replace('\n', " ")
                )

            elif entry["type"] == "video" or entry["type"] == "videos":
                os.system(f"""
                    yt-dlp
                    -c
                    --merge-output-format mkv
                    -o 'videos/{entry['folder-name']}/%(title)s.%(ext)s'
                    --extractor-args youtube:player_client=android
                    --throttled-rate 100M
                    --restrict-filenames
                    --download-archive alreadydownloadedonce-videos.txt
                    '{entry['url']}'
                    """.replace('\n', " ")
                )

    except yaml.YAMLError as exc:
        print("You fucked up the yaml format.")

