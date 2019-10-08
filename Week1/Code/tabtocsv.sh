#!/bin/bash
# Author: Your name you.login@imperial.ac.uk
# Script: tabtocsv.sh
# Desc: substitute the tabs in the files with commas saves the output into a .csv file
# Arguments: 1-> tab delimited file
# Date: 1st Oct 2019

echo "Creating a comma delimited version of $1 ..."
cat $1 | tr -s "\t" "," >> $1.csv
echo "Done!"
exit


#sudo apt update && sudo apt upgrade§