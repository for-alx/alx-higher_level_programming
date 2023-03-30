#!/bin/bash
# Comment
curl -sL 0:5000/catch_me -X PUT "You got me!" -H "Origin: walla" -d "user_id=98"
