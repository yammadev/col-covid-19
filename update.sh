#!/bin/bash

# Print
print () {
  echo -e "\n[RUN] $1"
}

# -------------------------------
# [1] Configure
# -------------------------------
# Remove old generated data
print "Remove old generated data"

rm -rf data/csv/* daya/imgs/* resources/data/*

# Configure
print "Configure"

# Move to data
cd data

# Get python virtual environment
py -m venv venv

# Install
venv/scripts/pip.exe install -U -r requirements.txt

# -------------------------------
# [2] Generate new data
# -------------------------------
print "Generate new data"

# Export
venv/scripts/python generate.py

# Check
echo ""
read -p ">> Please check generated data and press [ENTER] when ready to continue building. Otherwise press [CTRL+C] "

# -------------------------------
# [3] Build
# -------------------------------
# Move to base
cd ..

print "Prepare"
echo ""

# Install
npm install

print "Remove old compiled"

# Clean old
rm -rf docs/*

print "Build"

# Build
grunt

# Updated at
updated=`date "+%d-%m-%Y %H:%M"`

# -------------------------------
# [4] Push
# -------------------------------
# Confirm
print "Push"
read -p ">>> Please check generated files and press [ENTER] when ready to push. Otherwise press [CTRL+C] "

# Commit
print "Data updated $updated"

git status
git add --all
git commit -m "Data updated $updated"
git push
