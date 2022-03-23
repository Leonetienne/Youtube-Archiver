#!/bin/zsh

REMOTE_LOCATION=/media/family_nas/Leon/Mediafarm/Youtube-Archive

cp -u alreadydownloaded.txt $REMOTE_LOCATION
rsync -auv --remove-source-files music/ "$REMOTE_LOCATION"/music
rsync -auv --remove-source-files videos/ "$REMOTE_LOCATION"/videos

