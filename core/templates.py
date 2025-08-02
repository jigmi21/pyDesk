import os
def create_template (type,path):
    TEMPLATES = {
    "research": {
        "folders": ["data", "notebooks", "reports", "src"],
        "files": ["README.md", ".gitignore"]
    },
    "website": {
        "folders": ["html", "css", "js", "assets"],
        "files": ["index.html", "README.md"]
    }
}
    template = TEMPLATES.get(type)
    if not template:
        print("Invalid template type")
        return
    
    else: 
        root_dir = os.path.join(path, type)
        os.makedirs(root_dir, exist_ok = True)


    for key, value_list in template.items():
        for item in value_list:
            if key == "folders":
                os.makedirs(os.path.join(root_dir, item))
            elif key == "files":
                file_path = os.path.join(root_dir, item)
                with open (file_path, "w") as file:
                    pass

create_template("research", "user/pydesk")