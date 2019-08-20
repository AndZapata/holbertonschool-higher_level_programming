#!/bin/bash
# Comment: displays all HTTP methods the server will accept
curl -sD - "$1" | grep Allow: | cut -d " " -f2-
