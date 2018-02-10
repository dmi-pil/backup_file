import os, time, tarfile

def save_backup():
    temp = 0

    while temp < 3:

        patch_to_save_backup = input("please input the location where will save backup >> ")

        if os.path.exists(patch_to_save_backup) == True:
            print("ok")
            print("your locayion to save backup file >> ", patch_to_save_backup)
            return patch_to_save_backup

        else:
            print("patch doesn't exist")
            temp += 1
            if temp == 3:
                print(" goodbye")
                exit(0)

def save_file():
    temp = 0

    while temp < 3:

        patch_to_backup = input("please input location files for backup  >> ")

        if os.path.exists(patch_to_backup) == True:
            print("ok")
            print("your location for backup files >> ", patch_to_backup)
            return patch_to_backup
        else:
            print("patch doesn't exist")
            temp += 1
            if temp == 3:
                print(" goodbye")
                exit(0)


def tar(patch_to_save_backup, patch_to_backup):

    tar = tarfile.open(patch_to_save_backup + os.sep + "backup_" + time.strftime('%Y.%m.%d') + ".tar.gz", "w:gz")
    folder = os.chdir(patch_to_backup)
    folder_files = os.listdir(folder)
    print("********************************************")

    for files in folder_files:
        if os.path.isfile(files):
            print(" files append >> ", files)
            tar.add(files)
        if os.path.isdir(files):
            print(" dir append >> ", files)
            tar.add(files)
    tar.close()

patch_to_save_backup = save_backup()
patch_to_backup = save_file()
tar(patch_to_save_backup, patch_to_backup)

