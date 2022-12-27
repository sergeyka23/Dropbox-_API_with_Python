import dropbox
import os

dbx = dropbox.Dropbox('token')

dbx.users_get_current_account()
# Check the content of the account folders
for entry in dbx.files_list_folder('').entries:
    print(entry.name)

folder_path = "/Uploads"
# List the contents of the folder
folder_contents = dbx.files_list_folder(folder_path)

# Start the loop to go over the files we checked out
for entry in folder_contents.entries:
    if isinstance(entry, dropbox.files.FileMetadata):
        file_path = entry.path_lower
        file_name = entry.name

        # Split the file name for folder name and new date
        split_filename = file_name.split("_")
        folder_name = split_filename[0]
        # Rearenge the date to US type for the new file name
        date_us_split = [split_filename[3], split_filename[2], split_filename[1]]
        date_us_string = "_".join(date_us_split)
        time_original = split_filename[4]

        # Create the destination folder if it doesn't exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Download the file
        metadata, file_data = dbx.files_download(file_path)

        # Save the file to the local filesystem
        with open(os.path.join(folder_name, file_name), "wb") as f:
            f.write(file_data.content)

        # Rewrite the file name with rearenged date to US type
        new_name = folder_name + "_" + date_us_string + "_" + time_original
        # Get the current working directory
        cwd = os.getcwd()

        # Construct the full path to the file
        old_file_path = os.path.join(cwd, folder_name, file_name)
        new_file_path = os.path.join(cwd, folder_name, new_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)
