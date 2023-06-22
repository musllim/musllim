import base64

with open('lang-and-tools.svg', 'rb') as file:
    svg_data = file.read()

base64_encoded_data = base64.b64encode(svg_data).decode('utf-8')

print(f"![SVG Image](data:image/svg+xml;base64,{base64_encoded_data})")
