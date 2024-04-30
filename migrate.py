import os
import config as global_config
print("\n","::"*9)
print("", "Creating folders ...")
print("","::"*9, '\n')
folders_to_create = []
for key, value in global_config.__dict__.items():
    if not key.startswith("__"):
        if (isinstance(value, str)):
            if value.endswith("/"):
                print(f"{key}'s folder : {value}")
                folders_to_create.append(value)

for folder in folders_to_create:
    os.makedirs(folder, exist_ok=True)

print("\n Folders created successfully. \n")
