import os
import markdown
def render(fn):
        with open(fn, 'r') as markdown_file:
                # Read the content of the file
                content = markdown_file.read()

                # Convert to HTML
                return markdown.markdown(content)