# Bandit Level 1

## Goal

Connect as `bandit1`, inspect the home directory, and read the file named `-` to obtain the password for the next level.

## Approach

I connected to the Bandit server using SSH with the `bandit1` account and the password obtained from Level 0.

After logging in, I used `ls -lah` to inspect the current directory in detail. I noticed an entry named `-` and confirmed that it was a regular file rather than a directory.

I then tried reading it with `more -`, which displayed the file contents successfully.

## Commands Used

```bash
ssh bandit1@bandit.labs.overthewire.org -p 2220
ls -lah
more -
```

## What I Learned

- How to reconnect to the Bandit server using the credentials from the previous level.
- How `ls -lah` shows detailed information about files, including permissions, size, and hidden files.
- A single dash (`-`) can actually be the literal name of a file.
- Some Linux commands treat `-` specially, so filenames like this can be confusing.
- `more` can be used to display text file contents one screen at a time.

## Notes

The password for the next level is intentionally not published.
