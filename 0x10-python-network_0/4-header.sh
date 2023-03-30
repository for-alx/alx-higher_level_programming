#!/bin/bash
# Displays all HTTP methods the server will accept.
curl -sX GET -H "X-HolbertonSchool-User-Id: 98" "$*"
