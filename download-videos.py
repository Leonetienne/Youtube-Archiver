import yaml
import os

with open("linklist-videos.yaml", "r") as yamlfile:
    try:
        config = yaml.safe_load(yamlfile)

        for entry in config:
            print(f"\033[92mGrabbing '{entry['url']}':\033[0m")

            folderName = entry["folder-name"] if "folder-name" in entry else "%(uploader)s"

            os.system(f"""
                yt-dlp
                -c
                --merge-output-format mkv
                -o 'videos/{folderName}/%(title)s.%(ext)s'
                --extractor-args youtube:player_client=android
                --throttled-rate 100M
                --restrict-filenames
                --download-archive alreadydownloaded-videos.txt
                '{entry['url']}'
                """.replace('\n', " ")
            )

    except yaml.YAMLError as exc:
        print("You fucked up the yaml format.")

