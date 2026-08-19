# Bandit Level 4

## Goal

Find and read a hidden file inside the `inhere` directory.

## Approach

Normal `ls` does not show hidden files, so I used the `-a` option after entering the directory.

## Commands Used

```bash
cd inhere
ls -a
cat .hidden
```

## What I Learned

- Hidden files in Linux begin with `.`.
- `ls -a` displays hidden entries.
- How to move between directories using `cd`.

## Notes

The password is intentionally omitted.
