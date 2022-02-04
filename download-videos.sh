yt-dlp \
-a linklist-videos.txt \
-c \
--merge-output-format mkv \
-o 'videos/%(uploader)s/%(title)s.%(ext)s' \
--extractor-args youtube:player_client=android \
--throttled-rate 100M \
--restrict-filenames \
--download-archive alreadydownloaded-videos.txt
