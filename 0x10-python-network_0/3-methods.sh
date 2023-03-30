#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -s -X OPTIONS $* | grep "Allow:" | cut -d " " -f 2,3,4
