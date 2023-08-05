import os, glob

dir_source_files = './dados-publicos'
dir_new_files = './dados-para-test'
total_lines = 200


for file_path in glob.glob(os.path.join(dir_source_files,r'*')):
    new_file_name = file_path.split('/')[-1]
    print('File Name:', new_file_name)

    with open(file_path, encoding = "latin-1") as file:
        for count, line in enumerate(file):
            pass

    with open(file_path, encoding = "latin-1") as file:
        limit_lines = total_lines if count + 1 >= total_lines else count + 1
        print('Total lines:', limit_lines)
        lines = [next(file) for _ in range(limit_lines)]

    with open(os.path.join(dir_new_files, new_file_name),  mode='w') as new_file:
        print('Starting writing...')
        # for _, row in zip(range(total_lines), lines):
        for row in lines:
            new_file.write(row)
        print('Ending writing.')