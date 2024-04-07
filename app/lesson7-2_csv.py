import csv
import os
import pathlib
import glob
import shutil

with open('csv/text.csv', 'w', newline='') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': '1'})
    writer.writerow({'Name': 'B', 'Count': '2'})


print(os.path.exists("/usr/src/app/csv/text.csv"))

print(os.path.isfile('/usr/src/app/renamed.txt'))

print(os.path.isdir('design'))

# os.rename('test.txt', 'renamed.txt')

# os.mkdir('testdir')

# pathlib.Path('/usr/src/app/csv/empty.txt').touch()

# os.remove('/usr/src/app/csv/empty.txt')

# os.mkdir('test_dir')
# os.mkdir('test_dir/test_dir2')
print(os.listdir('/usr'))
print(glob.glob('/usr/src/app/*.py'))

shutil.copy('/usr/src/app/csv/text.csv', '/usr/src/app/csv/text2.csv')
print(glob.glob('/usr/src/app/csv/*'))

shutil.rmtree('/usr/src/app/csv')