import os

html_path = os.path.expanduser('~/iris-massage-klang/index.html')
if not os.path.exists(html_path):
    # Try finding any html file in iris-massage-klang
    for root, dirs, files in os.walk(os.path.expanduser('~/iris-massage-klang')):
        for f in files:
            if f.endswith('.html'):
                html_path = os.path.join(root, f)
                break

print(f"Using HTML path: {html_path}")
