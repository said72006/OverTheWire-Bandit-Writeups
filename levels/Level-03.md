# Bandit Level 3

## Goal

Find the hidden file inside the `inhere` directory and read its contents to obtain the password for the next level.

## Approach

I first listed the files in my home directory and found a directory called `inhere`.

```bash
ls
cd inhere
```

Running normal `ls` did not show any files, so I tried showing hidden files:

```bash
ls -a
```

This revealed a hidden entry named:

```text
...Hiding-From-You
```

I also checked the help for `ls`. I first tried `ls -help`, which was incorrect, then used the correct long option:

```bash
ls --help
```

From the help output I confirmed that `-a` / `--all` shows files whose names begin with `.`.

Next I used a detailed listing:

```bash
ls -lah
```

The entry started with `-rw-r-----`, which showed me that `...Hiding-From-You` was a regular file, not a directory.

I still tried entering it with `cd`, which failed with `Not a directory`. That confirmed I needed to read the file instead:

```bash
cat ...Hiding-From-You
```

This displayed the password for the next level. The password itself is intentionally not published here.

## Commands Used

```bash
ls
cd inhere
ls
ls -a
ls -help
ls --help
ls -lah
cd ...Hiding-From-You
cat ...Hiding-From-You
```

## What I Learned

- Linux hides filenames beginning with `.` from normal `ls` output.
- `ls -a` or `ls --all` displays hidden files.
- Long options use two dashes, such as `--help`; `-help` is not the same thing.
- In `ls -l`, the first character indicates the file type. A leading `-` means a regular file, while `d` means a directory.
- `cd` only works with directories.
- `cat` can be used to read the contents of a regular text file.
- Failed commands can still be useful because their error messages help identify what an object is and what command should be used next.

## Notes

Passwords and active credentials are intentionally not published.
