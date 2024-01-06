import os


def rename_file(base_path, curr_name, new_name,extension):
    curr_path = os.path.join(base_path,curr_name+extension)
    new_path = os.path.join(base_path,new_name+extension)

    os.rename(curr_path,new_path)

    return


def list_dir(folder_path: str, extension: str):
    file_list = [file for file in os.listdir(folder_path) if file.endswith(extension)]
    return file_list



if __name__ == "__main__":

    test_folder = r"C:\Users\anand\Projects\Enefit\Reference Materials"

    print(list_dir(test_folder, ".pdf"))