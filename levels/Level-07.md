# Bandit Level 7

## Goal

Practice locating a specific piece of information inside a text file using command-line text searching.

## Approach

I first listed the files in the home directory and found a text file containing many lines of data.

Instead of opening the entire file and searching manually, I used `grep` to search directly for the required label and return only the matching line.

## Command Pattern Used

```bash
grep "search_term" file.txt
```

## How `grep` Works

`grep` searches text for a matching word or pattern.

In the command above:

- `grep` is the search command.
- `"search_term"` is the word or pattern I want to find.
- `file.txt` is the file to search inside.

If a matching line exists, `grep` prints that line to the terminal.

## What I Learned

- `grep` is much faster than manually reading a large text file.
- It can search for a specific word or pattern inside a file.
- The basic syntax is `grep PATTERN FILE`.
- Filtering output is an important Linux skill for working with large amounts of text.

## Notes

The exact challenge answer and credentials are intentionally not published.
