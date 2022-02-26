# Youtube-Archiver
***Always** keep a local backup.*

This utility allows you to define a collection of links to youtube-channels and/or playlists, which you want to keep synced to your local storage.
All you have to do is to call `download.sh`, which will download all videos of your defined playlists that are not already saved locally.

This basically means, after doing the initial big download, you could run it as a cronjob, since it won't take long when it's only downloading newly uploaded videos.

## How does it work?
Pretty easily.

#### 1
First, you define the stuff you want to download, in yaml files. For more info on syntax, see the [example file](https://github.com/Leonetienne/Youtube-Archiver/blob/master/linklist-example.yaml).
```yaml
# linklist-music.yaml

# Eminem
-
  url: https://www.youtube.com/c/eminem/videos
  folder-name: Eminem

# DJ. S3RL
-
  url: https://www.youtube.com/channel/UCb6JTMjrHZCYFD9Y04CBk9g

# Snoop Dogg
-
  url: https://www.youtube.com/watch?v=zV-Xcy_bF2w&list=PL75C4B43E5F60A82C
  folder-name: Snoog Dogg
```

#### 2
Secondly, calling `download.sh` will invoke the two python scripts responsible for downloading.

#### 3
These python scripts will invoke [yt-dlp](https://github.com/yt-dlp/yt-dlp) for each link supplied. Yt-dlp runs in download-archive mode,
which basically means it won't download a video twice. It will save it's ID and check if it's already saved before downloading.

Files will be saved to `./videos/<folder>/` and `./music/<folder>`.
