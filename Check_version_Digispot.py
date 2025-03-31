import csv
import os
import win32api


def get_file_version(filepath):
    try:
        info = win32api.GetFileVersionInfo(filepath, '\\')
        version = "%d.%d.%d.%d" % (
            info['FileVersionMS'] / 65536,
            info['FileVersionMS'] % 65536,
            info['FileVersionLS'] / 65536,
            info['FileVersionLS'] % 65536
        )
        return version
    except:
        return "N/A"


def find_version_2_in_same_folder(filepath):
    folder = os.path.dirname(filepath)
    filename = os.path.basename(filepath)

    for file in os.listdir(folder):
        if file.lower() == filename.lower():
            full_path = os.path.join(folder, file)
            if os.path.isfile(full_path):
                version = get_file_version(full_path)
                if version.startswith("2."):
                    return version
    return None


file_path = "Digispot-BackupDJin.csv"
output_file = "output.txt"
target_executables = ['djin.exe', 'mag2.exe', 'mediaplanner.exe', 'track2.exe', 'ddb.exe']

with open(file_path, newline='', encoding='utf-8', errors='replace') as csvfile, \
        open(output_file, 'w', encoding='utf-8') as outfile:
    reader = csv.reader(csvfile)

    for row in reader:
        if not row:
            continue
        path = row[0].strip()

        if os.path.exists(path):
            # Если это файл и он в списке целевых
            if os.path.isfile(path) and os.path.basename(path).lower() in target_executables:
                version = get_file_version(path)
                if not version.startswith("2."):
                    version_2 = find_version_2_in_same_folder(path)
                    if version_2:
                        version = version_2
                outfile.write(f"{path} {version}\n")

            # Если это папка, ищем файлы в ней
            elif os.path.isdir(path):
                for file in os.listdir(path):
                    if file.lower() in target_executables:
                        full_path = os.path.join(path, file)
                        if os.path.isfile(full_path):
                            version = get_file_version(full_path)
                            if not version.startswith("2."):
                                version_2 = find_version_2_in_same_folder(full_path)
                                if version_2:
                                    version = version_2
                            outfile.write(f"{full_path} {version}\n")