#!/bin/bash
# displays only the status code of the response
curl -so -w "%{http_code}" $*
