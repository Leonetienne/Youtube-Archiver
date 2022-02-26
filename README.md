# Youtube-Archiver
***Always** keep a local backup.*

This utility allows you to define a collection of links to youtube-channels and/or playlists, which you want to keep synced to your local storage.
All you have to do is to call `download.sh`, which will download all videos and mp3's of your defined playlists that are not already saved locally.

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
  folder-name: Snoop Dogg
```

#### 2
Secondly, calling `download.sh` will invoke the two python scripts responsible for downloading.

These python scripts will invoke [yt-dlp](https://github.com/yt-dlp/yt-dlp) for each link supplied. Yt-dlp runs in download-archive mode,
which basically means it won't download a video twice. It will save video IDs and check if a video already saved before downloading.

Files will be saved to `./videos/<folder>/` and `./music/<folder>/`.

## Installation / Setup
1) Clone this repository
2) Create `linklist-videos.yaml` and `linklist-music.yaml` in repository-root and populate these to your liking.
3) Make sure you have Python3 and [yt-dlp](https://github.com/yt-dlp/yt-dlp) installed. (The commands `python3` and `yt-dlp` should be available!)
4) Done.

## Other noteworthy utilities
### Download once
You can create a `once.yaml` [(See example)](https://github.com/Leonetienne/Youtube-Archiver/blob/master/once-example.yaml), which is of the same structure as all the other linklists (except it needs a `type`=[`video`/`music`]), and `folder-name` is a required attribute.  
You can download this linklist with `python3 download-once.py`.  
What's the purpose of this? If you find a nice playlist, which won't ever update, why would you want to fetch it every time running the cronjob?  
Just adding it to a download list and running the cronjob is shit aswell, because fetching all the other items still takes time.  
This allows you to bypass ALL your other lists, to quickly and cleanly download a playlist (or multiple) **once**.

### sync-to-nas.bat
Since i use WSL, and like to store my archives on my nas, i made a quick script to move downloads from my local instance to my nas.
Without saying, you would have to adjust your nas drive-letter and target paths...

## Idea
This project is building upon [Backup Script with yt-dlp](https://igel.hostedbymyself.de/s/C77Zj-PBL#), [@xaverruss](https://github.com/xaverruss).

# LICENSE
```
BSD 2-Clause License

Copyright (c) 2022, Leon Etienne
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
```
