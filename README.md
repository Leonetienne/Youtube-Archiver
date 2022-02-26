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
which basically means it won't download a video twice. It will save it's video ID and check if it's already saved before downloading.

Files will be saved to `./videos/<folder>/` and `./music/<folder>/`.

## Installing / Setup
1) Clone this repository
2) Create `linklist-videos.yaml` and `linklist-music.yaml` and populate these to your linking.
3) Make sure you have Python3 and [yt-dlp](https://github.com/yt-dlp/yt-dlp) installed.
4) Done.

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