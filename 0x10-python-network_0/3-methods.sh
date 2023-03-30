#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -sI -X OPTIONS $* | grep "Allow:" | cut -d " " -f-
