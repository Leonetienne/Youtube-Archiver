Rem Since i use WSL, and like to store my archives on my nas, i made a quick script to move downloads from my local instance to my nas.
Rem These are the important files to move, btw.

robocopy music\ Y:\Leon\Mediafarm\Youtube-Archive\music\ /e /z /j /xo /move
robocopy videos\ Y:\Leon\Mediafarm\Youtube-Archive\videos\ /e /z /j /xo /move
robocopy . Y:\Leon\Mediafarm\Youtube-Archive\ alreadydownloaded*.txt /z /im

