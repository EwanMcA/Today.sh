import json
import os
import sys
import re
from datetime import datetime


def read_config(dir):
    with open(f"{dir}/config.json") as f:
        return json.load(f)


def read_today(fn, tags):
    additions = {}
    with open(fn) as f:
        for line in f:
            for tag in tags:
                if line.startswith(f"[{tag}]"):
                    if tag in additions:
                        additions[tag].append(line)
                    else:
                        additions[tag] = [line]

    return additions


def filter_tags(dir, additions):
    try:
        with open(f"{dir}/.log", "r+") as f:
            loglines = f.readlines()
    except FileNotFoundError:
        return

    removals = {}
    for tag in additions:
        for add in additions[tag]:
            if add in loglines:
                if tag not in removals:
                    removals[tag] = [add]
                else:
                    removals[tag].append(add)

    for tag in removals:
        for add in removals[tag]:
            additions[tag].remove(add)


def write_tags(additions):
    # if file doesn't exist yet, add a heading
    for tag in additions:
        with open(f"{tag}.md", 'a+') as f:
            if f.tell() == 0:
                f.write(f"# {tag}\n\n")
            for add in additions[tag]:
                f.write(add)


def write_log(dir, additions):
    with open(f"{dir}/.log", 'a+') as f:
        for tag in additions:
            for add in additions[tag]:
                f.write(add)

def main(fn):
    dir = os.environ.get("TODAY_DIR")
    if not dir:
        raise ValueError("TODAY_DIR not set")
    dir = re.sub(r'/$', '', dir)

    config = read_config(dir)
    tags = config.get('tags', [])
    additions = read_today(fn, tags)
    filter_tags(dir, additions)
    write_tags(additions)
    write_log(dir, additions)
                    

if __name__ == '__main__':
    main(sys.argv[1])
