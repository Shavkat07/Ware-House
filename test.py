# import os
#
#
# def open_folders_infinitely(folder_path):
#     try:
#         contents = os.listdir(folder_path)
#         for item in contents:
#             item_path = os.path.join(folder_path, item)
#             if os.path.isdir(item_path):
#                 print(f"Opening folder: {item_path}")
#                 open_folders_infinitely(item_path)
#             else:
#                 print(f"Found a file: {item_path}")
#     except Exception as e:
#         print(f"Error occurred while processing {folder_path}: {e}")
#
#
# # Usage example:
# folder_path = "C:/Users/shavk/Documents/folder"  # Replace this with the path of the folder you want to start from
# open_folders_infinitely(folder_path)


import os
#
#
# def open_remote_folders(remote_path, depth):
#     if depth == 0:
#         return
#
#     try:
#         # List contents of the current remote_path
#         contents = os.listdir(remote_path)
#
#         for item in contents:
#             item_path = os.path.join(remote_path, item)
#
#             if os.path.isdir(item_path):
#                 print(f"Opening folder: {item_path}")
#                 open_remote_folders(item_path, depth - 1)
#             else:
#                 print(f"Found a file: {item_path}")
#
#     except Exception as e:
#         print(f"Error occurred while processing {remote_path}: {e}")
#
#
# # Usage example:
# remote_path = "C:/Users/shavk/Documents/folder"
# depth_to_explore = 3  # Set the desired depth to explore the folders
# open_remote_folders(remote_path, depth_to_explore)

# current_file_path = os.path.abspath(__file__)
# print(f"The current location of the Python file is: {current_file_path}")


