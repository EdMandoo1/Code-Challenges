#!/bin/bash

# Script Name:                  Clearing Logs  
# Author:                       Eduardo Ayala
# Date of latest revision:      06/05/2023
# Purpose:  Clear log files

Timestamp=$(date +%Y%m%d%H%M%S)

# Directory to store compressed log files
backup_dir="backup"

# Log files to compress
log_files=(
  "/var/log/syslog"
  "/var/log/wtmp"
)

# Make backup directory
mkdir $backup_dir
# Print file sizes before compression
for log_file in "${log_files[@]}"; do
  if [[ -f "$log_file" ]]; then
    file_size=$(du -h "$log_file" | awk '{print $1}')
    echo "File size of $log_file: $file_size"
  else
    echo "File $log_file does not exist."
  fi
done

# Compress log files to backup directory and clear the contents
for log_file in "${log_files[@]}"; do
  if [[ -f "$log_file" ]]; then
    base_name=$(basename "$log_file")
    compressed_file="$backup_dir/${base_name}-${timestamp}.gz"
    gzip -c "$log_file" > "$compressed_file"
    compressed_size=$(du -h "$compressed_file" | awk '{print $1}')
    echo "Compressed $log_file to $compressed_file"
    echo "Compressed file size: $compressed_size"

    original_size=$(du -h "$log_file" | awk '{print $1}')
    echo "Original file size: $original_size"

    if [[ "$compressed_size" == "$original_size" ]]; then
      echo "Compressed file size is the same as the original file size."
    else
      echo "Compressed file size is different from the original file size."
    fi

    # Clear the contents of the log file
    truncate -s 0 "$log_file"
    echo "Cleared the contents of $log_file"
  else
    echo "File $log_file does not exist. Skipping compression and clearing."
  fi
done

