Rem Quick script to sync the downloads, and important files, to a network storage
Rem These are the important files to move, btw.

robocopy music\ Y:\Leon\Mediafarm\Youtube-Archive\music\ /e /z /j /xo /move
robocopy videos\ Y:\Leon\Mediafarm\Youtube-Archive\videos\ /e /z /j /xo /move
robocopy . Y:\Leon\Mediafarm\Youtube-Archive\ alreadydownloaded*.txt /z /im

