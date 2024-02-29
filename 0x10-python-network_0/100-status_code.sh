#!/bin/bash
#script for displaying the code of the response
curl -s "$1" -o /dev/null -w "%{http_code}"
