import os

desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

for i in range(100):
    file_name = f'hacked_{i+1}.txt'
    file_path = os.path.join(desktop_path, file_name)
    
    with open(file_path, 'w') as file:
        file.write('You have been hacked!')
