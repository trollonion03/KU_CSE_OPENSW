import sys

if len(sys.argv) != 3:
    print("Usage: python copy_file.py [source_file_path] [destination_file_path]")
    sys.exit(1)
source_file_path = sys.argv[1]
destination_file_path = sys.argv[2]

with open(source_file_path, 'r') as f:
    with open(destination_file_path, 'w') as dest_f:
        for line in f:
            dest_f.write(line)

print("complete!")