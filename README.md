# FileBackup

## Overview

FileBackup is a Python program designed to automate the backup process for critical files and folders on Windows systems. It provides scheduled backups, ensuring that your important data is safely copied to a designated backup location at regular intervals.

## Features

- **Automated Backups:** Schedule backups at specified intervals (e.g., every 24 hours).
- **Directory Support:** Back up multiple directories, preserving the directory structure.
- **Simple Configuration:** Easily configure source directories and backup destinations.

## Requirements

- Python 3.x
- `schedule` package (install with `pip install schedule`)

## Usage

1. **Configure Directories:**

   Edit the `source_directories` list in the script to include the paths of the directories you want to back up. Set the `backup_directory` to the path where you want to store the backups.

   ```python
   source_directories = ["C:\\path\\to\\important\\files", "C:\\another\\critical\\folder"]
   backup_directory = "D:\\backups"
   ```

2. **Set Backup Interval:**

   Define the interval in hours for the backup schedule by modifying `backup_interval_hours`.

   ```python
   backup_interval_hours = 24
   ```

3. **Run the Script:**

   Execute the script using Python. The backup process will start immediately and run at the specified intervals.

   ```bash
   python file_backup.py
   ```

## Notes

- Ensure that the script has the necessary permissions to read from the source directories and write to the backup destination.
- The program will create a timestamped folder within the backup directory for each backup operation.
- The `schedule` library is used to handle the scheduling of the backup tasks.

## License

This project is licensed under the MIT License.