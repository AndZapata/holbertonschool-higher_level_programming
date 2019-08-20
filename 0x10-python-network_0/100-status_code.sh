#!/bin/bash
# Comment: sends a request to a URL passed, and displays only the status code
curl -so /dev/null -w "%{http_code}" "$1"
