import xmltodict

def render(file_content: str):
    content = xmltodict(file_content)
