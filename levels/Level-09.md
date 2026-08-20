# Bandit Level 9

## Goal

Identify the password inside `data.txt` where it appears among a small number of human-readable strings and is preceded by several `=` characters.

## Approach

The file contains a lot of non-readable data, so reading it directly is not useful. I first extracted only the printable, human-readable strings, then filtered those results to keep only lines containing the `=` character mentioned in the challenge.

This reduced a noisy file to a small set of relevant candidate lines.

## Commands Used

```bash
strings data.txt | grep =
```

### Command Breakdown

- `strings data.txt` extracts printable text sequences from the file and ignores most binary/non-readable content.
- `|` is a pipe. It sends the standard output of `strings` directly into the next command.
- `grep =` keeps only the lines that contain an equals sign (`=`).

The challenge specifically mentioned that the target text is preceded by several `=` characters, so filtering on `=` made the relevant line easy to identify without manually scanning all extracted strings.

## What I Learned

- `strings` is useful for extracting readable text from files that contain binary or mixed data.
- `grep` can be used after another command to narrow a large output to only relevant lines.
- Pipes (`|`) let multiple Linux commands work together as a filtering pipeline.
- Challenge clues can often be translated directly into useful command-line filters.

## Notes

The password and active credentials are intentionally not published.
