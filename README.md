# Today.sh

A note taking app which extracts tags from a daily note file.

## Usage

```bash
today.sh
```

## Add tags

```markdown
[MISC] Had an important meeting where we discussed business and synergy.
[TODO] Do something.
[CODE] Made some important changes to my note-taking app.
```

- run `parse.py` and these will be copied to tags files if configured to do so.

## Configuration

`config.py`
```json
{
    "tags": ["TODO"], // anything listed here will be copied to a tags file
}
```

## Nvim

- to run parse on save, add this to your vim config:
```vim
vim.api.nvim_command("autocmd BufWritePost *.md :!python ./path/to/parse.py %")
```
