import schedule
import os
import shutil
import time

def job_time():
    main_dir = 'A'
    copy_path = os.path.join(address, main_dir)
    paste_path = 'Time @ 5 PM'

    files = ['a.txt', 'b.txt', 'c.txt', 'd.txt']
    os.mkdir(paste_path)
    
    for file in files:
        file_src = os.path.join(copy_path, file)
        file_dst = os.path.join(paste_path, file)
        shutil.copy(file_src, file_dst)
    
    split = os.path.split(paste_path)
    folder = split[1]
    add = split[0]
    print(f"Made a folder {folder} in {add}")


def job_minute():
    def new_paste_path(add, x):
        while True:
            dir_name = f'A_{x}_minute'
            paste_path = os.path.join(add, dir_name)
            if os.path.exists(paste_path):
                paste_path = new_paste_path(add, x+1)
                return paste_path
            return paste_path

    main_dir = 'A'
    copy_path = os.path.join(address, main_dir)
    paste_path = new_paste_path(address, 1)

    files = ['a.txt', 'b.txt', 'c.txt', 'd.txt']
    os.mkdir(paste_path)
    
    for file in files:
        file_src = os.path.join(copy_path, file)
        file_dst = os.path.join(paste_path, file)
        shutil.copy(file_src, file_dst)

    split = os.path.split(paste_path)
    folder = split[1]
    add = split[0]
    print(f"Made a folder {folder} in {add}")

def job_hour():
    def new_paste_path(add, x):
        while True:
            dir_name = f'A_{x}_hour'
            paste_path = os.path.join(add, dir_name)
            if os.path.exists(paste_path):
                paste_path = new_paste_path(add, x+1)
                return paste_path
            return paste_path

    main_dir = 'A'
    copy_path = os.path.join(address, main_dir)
    paste_path = new_paste_path(address, 1)

    files = ['a.txt', 'b.txt', 'c.txt', 'd.txt']
    os.mkdir(paste_path)
    
    for file in files:
        file_src = os.path.join(copy_path, file)
        file_dst = os.path.join(paste_path, file)
        shutil.copy(file_src, file_dst)

    split = os.path.split(paste_path)
    folder = split[1]
    add = split[0]
    print(f"Made a folder {folder} in {add}")

def job_day():
    def new_paste_path(add, x):
        while True:
            dir_name = f'A_{x}_day'
            paste_path = os.path.join(add, dir_name)
            if os.path.exists(paste_path):
                paste_path = new_paste_path(add, x+1)
                return paste_path
            return paste_path

    main_dir = 'A'
    copy_path = os.path.join(address, main_dir)
    paste_path = new_paste_path(address, 1)

    files = ['a.txt', 'b.txt', 'c.txt', 'd.txt']
    os.mkdir(paste_path)
    
    for file in files:
        file_src = os.path.join(copy_path, file)
        file_dst = os.path.join(paste_path, file)
        shutil.copy(file_src, file_dst)
    
    split = os.path.split(paste_path)
    folder = split[1]
    add = split[0]
    print(f"Made a folder {folder} in {add}")


def job_week():
    def new_paste_path(add, x):
        while True:
            dir_name = f'A_{x}_week'
            paste_path = os.path.join(add, dir_name)
            if os.path.exists(paste_path):
                paste_path = new_paste_path(add, x+1)
                return paste_path
            return paste_path

    main_dir = 'A'
    copy_path = os.path.join(address, main_dir)
    paste_path = new_paste_path(address, 1)

    files = ['a.txt', 'b.txt', 'c.txt', 'd.txt']
    os.mkdir(paste_path)
    
    for file in files:
        file_src = os.path.join(copy_path, file)
        file_dst = os.path.join(paste_path, file)
        shutil.copy(file_src, file_dst)

    split = os.path.split(paste_path)
    folder = split[1]
    add = split[0]
    print(f"Made a folder {folder} in {add}")

def job_month():
    def new_paste_path(add, x):
        while True:
            dir_name = f'A_{x}_month'
            paste_path = os.path.join(add, dir_name)
            if os.path.exists(paste_path):
                paste_path = new_paste_path(add, x+1)
                return paste_path
            return paste_path

    main_dir = 'A'
    copy_path = os.path.join(address, main_dir)
    paste_path = new_paste_path(address, 1)

    files = ['a.txt', 'b.txt', 'c.txt', 'd.txt']
    os.mkdir(paste_path)
    
    for file in files:
        file_src = os.path.join(copy_path, file)
        file_dst = os.path.join(paste_path, file)
        shutil.copy(file_src, file_dst)

    split = os.path.split(paste_path)
    folder = split[1]
    add = split[0]
    print(f"Made a folder {folder} in {add}")

print("Initializing Schedule...")
print('Waiting for a minute to make directory...')
# address of current directory
file_path = os.path.abspath(__file__)
split = os.path.split(file_path)
address = split[0]

# run the job every ...
schedule.every().day.at("17:00").do(job_time)
schedule.every(1).minute.do(job_minute)
schedule.every(1).hour.do(job_hour)
schedule.every(1).day.do(job_day)
schedule.every(1).week.do(job_week)
schedule.every(30).days.do(job_month)

while True:
    schedule.run_pending()
    time.sleep(1)

# file_path = os.path.abspath(__file__)
# split = os.path.split(file_path)
# address = split[0]
# print(address)

# main_dir = 'A'
# copy_path = os.path.join(address, main_dir)

# directory = 'D'
# paste_path = os.path.join(address, directory)

# files = ['a.txt', 'b.txt', 'c.txt', 'd.txt']

# os.mkdir(paste_path)

# for file in files:
#     file_src = os.path.join(copy_path, file)
#     file_dst = os.path.join(paste_path, file)
#     shutil.copy(file_src, file_dst)


# print(f'Directory {directory} created in {address}')
