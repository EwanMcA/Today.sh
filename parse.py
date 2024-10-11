import json
from datetime import datetime

def main():
    with open('config.json') as f:
        config = json.load(f)

    today = datetime.now().strftime('%b_%d_%y.md')

    additions = {}
    with open(today) as f:
        for line in f:
            for tag in config.get('tags', []):
                if line.startswith(f"[{tag}]"):
                    if tag in additions:
                        additions[tag] += f"\n{line}"
                    else:
                        additions[tag] = line

    for tag in config.get('tags', []):
        with open(f"{tag}.md", 'a') as f:
            f.write(additions[tag])
                    

if __name__ == '__main__':
    main()
