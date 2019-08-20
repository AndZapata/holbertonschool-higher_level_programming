#!/bin/bash
# Comment: sends a JSON POST request to a URL passed, and displays the body
curl -sH "Content-Type: application/json" -X POST --data "@$2" "$1"
