# Bandit Level 2

## Goal

Read the file whose filename is a single dash (`-`).

## Approach

A dash can be interpreted by many commands as standard input, so I referenced the file using a relative path.

## Commands Used

```bash
ls
cat ./-
```

## What I Learned

- Why filenames beginning with or equal to `-` can be special in Linux commands.
- How `./` can be used to explicitly reference a file in the current directory.

## Notes

The password is intentionally omitted.
