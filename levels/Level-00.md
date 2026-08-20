# Bandit Level 0

## Goal

Connect to the OverTheWire Bandit server using SSH, inspect the home directory, and find the password for the next level.

## Approach

I first connected to the Bandit server using SSH on port `2220` with the `bandit0` username.

After logging in with the official starting credentials, I used `ls` to list the contents of the current directory. I found a file named `readme`, so I used `cat readme` to read its contents.

The file displayed a welcome message and the password required for the next level.

## Commands Used

```bash
ssh bandit0@bandit.labs.overthewire.org -p 2220
ls
cat readme
```

## What I Learned

- How to connect to a remote Linux machine using `ssh`.
- How to specify a custom SSH port using `-p`.
- How to list files in the current directory using `ls`.
- How to display the contents of a text file using `cat`.
- A simple workflow for exploring a remote Linux environment after logging in.

## Notes

The password for the next level is intentionally omitted from this write-up.
