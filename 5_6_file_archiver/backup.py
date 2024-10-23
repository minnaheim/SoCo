# git auf wish bestellt
# our backup lets us see the different files and the version
def backup(source_dir, dest_dir):
    manifest = hash_all(source_dir)
    timestamp = current_time()  # str
    # a manifest is a .csv file which provides meta info about other files (provides the connection between name and content)
    write_manifest(backup_dir, timestamp, manifest)
    copy_files(source_dir, backup_dir, manifest)
    return manifest
