#!/bin/bash
# Comment: sends a POST request to the passed URL, and displays the body
curl -s --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
