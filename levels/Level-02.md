# Bandit Level 2

## Goal

Read a file whose name contains spaces and also begins with `--`.

## Approach

After logging in as `bandit2`, I listed the files in the home directory using `ls -lah`.

I found this file:

```text
--spaces in this filename--
```

At first, I tried reading `spaces in this filename` without the leading and trailing `--`, so Linux reported that the file did not exist.

The filename has two things that need special handling:

1. It contains spaces. The shell normally treats spaces as separators between arguments.
2. It begins with `--`. Many Linux commands may interpret names beginning with `-` or `--` as command options.

To solve both problems, I used quotes around the filename and added `./` before it:

```bash
cat "./--spaces in this filename--"
```

The quotes keep the full filename together as one argument, while `./` tells the command that this is a file in the current directory rather than an option.

## Commands Used

```bash
ssh bandit2@bandit.labs.overthewire.org -p 2220
ls -lah
cat "./--spaces in this filename--"
```

An alternative way to handle the spaces is escaping them with backslashes:

```bash
cat ./--spaces\ in\ this\ filename--
```

## What I Learned

- Spaces separate command arguments in the shell unless they are quoted or escaped.
- Double quotes can be used to treat a filename containing spaces as one argument.
- A backslash (`\`) can escape individual spaces in a filename.
- Filenames beginning with `-` or `--` can be confused with command options.
- `./` means the current directory and makes it clear that the value is a file path.
- The exact filename matters, including symbols such as `--` at the beginning and end.

## Troubleshooting

These commands failed because I used the wrong filename:

```bash
cat spaces\ in\ this\ filename
more spaces\ in\ this\ filename
less spaces\ in\ this\ filename
```

The actual filename was `--spaces in this filename--`, not `spaces in this filename`.

## Notes

The password for the next level is intentionally not published.
