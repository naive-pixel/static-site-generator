import os
import shutil

def copy_source_to_dest(source,dest):
    source_abs_path = os.path.abspath(source)
    dest_abs_path = os.path.abspath(dest)
    print("dest_abs_path: ", dest_abs_path)

    if os.path.exists(dest_abs_path):
        shutil.rmtree(dest_abs_path)
        os.mkdir(dest_abs_path)
    else:
        os.mkdir(dest_abs_path)
    source_folders = os.listdir(source)
    print("source_folder: ", source_folders)
    for src_fold in source_folders:
        print("src_fold: ", src_fold)
        folder_source_abs_path = os.path.join(source_abs_path,src_fold)
        folder_dest_abs_path = os.path.join(dest_abs_path,src_fold)
        print("folder_source_abs_path: ", folder_source_abs_path)
        print("folder_dest_abs_path: ", folder_dest_abs_path)

        if os.path.isfile(folder_source_abs_path):
            print("found file")
            shutil.copy(folder_source_abs_path,dest_abs_path)
            print("copied file")
        else:
            print("found folder")
            os.mkdir(folder_dest_abs_path)
            copy_source_to_dest(folder_source_abs_path,folder_dest_abs_path)
        #print(os.listdir(dest))


