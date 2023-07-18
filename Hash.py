import hashlib
import os
from datetime import datetime

def calculate_hash():
    choice = input("Enter 'F' to obtain a hash of the file or 'T' to obtain a hash of the text:")

    if choice.upper() == 'F':
        filename = input("Please enter the file path:")
        try:
            file_stats = os.stat(filename)
            file_size = file_stats.st_size
            with open(filename, 'rb') as file:
                data = file.read()
        except IOError:
            print("Unable to open the file.")
            return
    elif choice.upper() == 'T':
        text = input("Please enter the text:")
        data = text.encode()
        file_size = len(data)
        filename = "Text Input"
    else:
        print("Invalid input.")
        return

    md5_hash = hashlib.md5(data).hexdigest()
    sha1_hash = hashlib.sha1(data).hexdigest()
    sha256_hash = hashlib.sha256(data).hexdigest()
    sha512_hash = hashlib.sha512(data).hexdigest()
    sha3_256_hash = hashlib.sha3_256(data).hexdigest()
    sha3_512_hash = hashlib.sha3_512(data).hexdigest()

    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print("--------------------------------------------------")
    print("Date and Time:", current_datetime)
    print("File Path:", filename)
    print("File Name:", os.path.basename(filename))
    print("File Size:", file_size, "bytes")
    print("MD5 Hash:", md5_hash)
    print("SHA-1 Hash:", sha1_hash)
    print("SHA-256 Hash:", sha256_hash)
    print("SHA-512 Hash:", sha512_hash)
    print("SHA-3 (256-bit) Hash:", sha3_256_hash)
    print("SHA-3 (512-bit) Hash:", sha3_512_hash)
    print("--------------------------------------------------")

calculate_hash()