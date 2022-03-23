#!/bin/zsh

REMOTE_LOCATION = /media/family_nas/Leon/Mediafarm/Youtube-Archive

mv music/ $REMOTE_LOCATION
mv videos/ $REMOTE_LOCATION
mv alreadydownloaded*.txt $REMOTE_LOCATION

# robocopy music\ Y:\Leon\Mediafarm\Youtube-Archive\music\ /e /z /j /xo /move
# robocopy videos\ Y:\Leon\Mediafarm\Youtube-Archive\videos\ /e /z /j /xo /move
# robocopy . Y:\Leon\Mediafarm\Youtube-Archive\ alreadydownloaded*.txt /z /im

