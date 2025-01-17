import os
import shutil
import time
import schedule
from datetime import datetime

def backup_files(source_dirs, backup_dir):
    """
    Copies files from source directories to a backup directory.

    :param source_dirs: List of directories to back up.
    :param backup_dir: Directory where backups will be stored.
    """
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    for source_dir in source_dirs:
        if os.path.exists(source_dir):
            for item in os.listdir(source_dir):
                s = os.path.join(source_dir, item)
                d = os.path.join(backup_dir, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d, dirs_exist_ok=True)
                else:
                    shutil.copy2(s, d)
        else:
            print(f"Source directory {source_dir} does not exist!")

def schedule_backup(source_dirs, backup_dir, interval):
    """
    Schedules the backup at a specified interval.

    :param source_dirs: List of directories to back up.
    :param backup_dir: Directory where backups will be stored.
    :param interval: Interval in hours for scheduling the backup.
    """
    def job():
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(backup_dir, f"backup_{current_time}")
        print(f"Starting backup at {current_time}")
        backup_files(source_dirs, backup_path)
        print(f"Backup completed at {current_time}")

    schedule.every(interval).hours.do(job)
    print(f"Backup scheduled every {interval} hours.")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    # Define the directories to back up and the backup destination
    source_directories = ["C:\\path\\to\\important\\files", "C:\\another\\critical\\folder"]
    backup_directory = "D:\\backups"

    # Schedule the backup to run every 24 hours
    backup_interval_hours = 24

    schedule_backup(source_directories, backup_directory, backup_interval_hours)