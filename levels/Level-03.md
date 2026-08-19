# Bandit Level 3

## Goal

Read a file whose name contains spaces.

## Approach

Because spaces separate command arguments, I treated the entire filename as one argument by quoting it.

## Commands Used

```bash
ls
cat "spaces in this filename"
```

## What I Learned

- How Linux shells treat spaces in filenames.
- How quoting keeps a filename with spaces together as one argument.
- An alternative is escaping spaces with backslashes.

## Notes

The password is intentionally omitted.
