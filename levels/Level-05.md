# Bandit Level 5

## Goal

Locate a file somewhere under the `inhere` directory that matches several properties: it is human-readable, has a specific size in bytes, and is not executable.

## Approach

I started by inspecting the `inhere` directory:

```bash
ls -lah
```

The top-level entries were directories, so I checked them with:

```bash
file ./*
```

This confirmed that the visible entries were directories rather than the target file.

Next, I searched recursively for regular files:

```bash
find . -type f
```

Because there were many results, I narrowed the search using the required file size:

```bash
find . -type f -size <SIZE_IN_BYTES>c
```

Here, `-type f` means regular files only, while the `c` suffix makes `find` interpret the size in bytes.

The filtered result pointed me to a hidden file inside one of the subdirectories. I used `ls -lah` in that directory to inspect its permissions and confirm that it was not executable, then read the candidate file with `cat`.

The exact target path and password are intentionally omitted.

## Commands Used

```bash
ls -lah
file ./*
find . -type f
find . -type f -size <SIZE_IN_BYTES>c
cat <candidate-file>
```

## What I Learned

- `find` searches recursively through directories.
- `-type f` filters the results to regular files only.
- `-size ...c` searches by an exact size in bytes.
- A missing `x` in file permissions means the file is not executable.
- Hidden files begin with `.` and are visible with `ls -a` or `ls -lah`.
- The shell wildcard `*` normally does **not** match hidden files whose names begin with `.`. This means `file ./*` can miss hidden files.
- Combining several file properties is much more efficient than manually checking every directory.

## Notes

Passwords, active credentials, and the exact target file are intentionally not published.
