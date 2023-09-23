# A virtual representation of the file to be generated
class File:
    def __init__(self, file_path, file_content):
        self.file_path = file_path
        self.file_content = file_content

    # Write the file to the disk based on path and content
    def generate_html_file(self):
        if self.file_path.endswith(".md"):
            write_path = self.file_path.replace(".md", ".html")    
        else:
            write_path = self.file_path.replace(".txt", ".html")

        with open(write_path, "w") as file:
            file.write(self.file_content)
