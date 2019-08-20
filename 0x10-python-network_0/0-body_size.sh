#!/bin/bash
# Comment: sends a request to that URL, and displays the size of the body
curl -sD - "$1" | grep "Content-Length" | cut -d " " -f2
