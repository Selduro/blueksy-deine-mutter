import os

def create_cron_job():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    cronjob_command = f"0 20 * * * /usr/bin/python3 {current_directory}/create_post.py >> {current_directory}/cron_log.txt 2>&1\n" # creates a logfile for debugging


    with open('/tmp/cronjob_temp', 'w') as temp_file:
        temp_file.write(cronjob_command)

    os.system('crontab /tmp/cronjob_temp')

    os.remove('/tmp/cronjob_temp')

if __name__ == "__main__":
    create_cron_job()
