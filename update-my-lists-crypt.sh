#!/bin/bash
# I want to version-control my lists, but i don't want them to be visible in case I ever decide to publicize this repository.
# So.... I guess I'll just check in encrypted versions, lol.

openssl enc -aes-256-cbc -pbkdf2 -in linklist-videos.yaml -out linklist-videos.yaml.crypt
openssl enc -aes-256-cbc -pbkdf2 -in linklist-music.yaml -out linklist-music.yaml.crypt
