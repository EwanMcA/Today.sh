import json
from datetime import datetime

def read_config():
    with open('config.json') as f:
        return json.load(f)


def read_today(tags):
    today = datetime.now().strftime('%b_%d_%y.md')
    additions = {}
    with open(today) as f:
        for line in f:
            for tag in tags:
                if line.startswith(f"[{tag}]"):
                    if tag in additions:
                        additions[tag].append(line)
                    else:
                        additions[tag] = [line]

    return additions


def filter_tags(additions):
    try:
        with open('.log', "r+") as f:
            loglines = f.readlines()
    except FileNotFoundError:
        return

    for tag in additions:
        for add in additions[tag]:
            if add in loglines:
                additions[tag].remove(add)


def write_tags(additions):
    # if file doesn't exist yet, add a heading
    for tag in additions:
        with open(f"{tag}.md", 'a+') as f:
            if f.read() == '':
                f.write(f"# {tag}\n\n")

    for tag in additions:
        with open(f"{tag}.md", 'a') as f:
            for add in additions[tag]:
                f.write(add)


def write_log(additions):
    with open('.log', 'a+') as f: 
        for tag in additions:
            for add in additions[tag]:
                f.write(add)

def main():
    config = read_config()
    tags = config.get('tags', [])
    additions = read_today(tags)
    filter_tags(additions)
    write_tags(additions)
    write_log(additions)
                    

if __name__ == '__main__':
    main()
