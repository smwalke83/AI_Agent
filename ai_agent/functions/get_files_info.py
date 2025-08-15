import os

def get_files_info(working_directory, directory="."):
    joined_path = os.path.join(working_directory, directory)
    dir_path = os.path.abspath(joined_path)
    work_path = os.path.abspath(working_directory)
    if not dir_path.startswith(work_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(dir_path):
        return f'Error: "{directory}" is not a directory'
    try:
        dir_list = os.listdir(dir_path)
        dir_string = ""
        for file in dir_list:
            file_path = os.path.join(dir_path, file)
            size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            if dir_string == "":
                dir_string += f' - {file}: file_size={size} bytes, is_dir={is_dir}'
            else:
                dir_string += f'\n - {file}: file_size={size} bytes, is_dir={is_dir}'
        return dir_string
    except Exception as e:
        return f"Error listing files: {e}"


