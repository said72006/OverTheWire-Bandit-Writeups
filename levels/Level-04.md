# Bandit Level 4

## Goal

Find the human-readable file inside the `inhere` directory and read its contents.

## Approach

I started by listing the home directory and entering `inhere`. The directory contained ten files named from `-file00` to `-file09`.

At first, I tried using `cd` on the files, but the shell showed that they were not directories. This helped me realize that I needed to inspect the files instead of trying to enter them.

Because every filename starts with `-`, I used `./` before the filenames so commands would treat them as file paths rather than command options.

I first checked one file with `file ./-file00`, then used `file ./*` to inspect all files at once. Most were reported as `data`, while `-file07` was identified as `ASCII text`. I then read that file with `cat`.

## Commands Used

```bash
ls
cd inhere/
ls
ls -lah

# These attempts helped confirm the entries were files, not directories
cd ./-file00

# Inspect one file
file ./-file00

# Inspect every non-hidden file in the current directory
file ./*

# Read the human-readable file
cat ./-file07
```

## What I Learned

- The first character in permissions such as `-rw-r-----` indicates a regular file; a directory would begin with `d`.
- `cd` works with directories, not regular files.
- Filenames beginning with `-` can be confused with command options, so prefixing them with `./` makes the path explicit.
- The `file` command identifies the type or format of a file based on its contents.
- `file ./*` is useful for checking many files at once: the shell expands `*` to the files in the current directory.
- `ASCII text` indicates a human-readable text file, while `data` usually means the content is not recognized as normal text.
- Failed commands can still help narrow down what an object is and which tool should be used next.

## Notes

The password for the next level is intentionally not published.
