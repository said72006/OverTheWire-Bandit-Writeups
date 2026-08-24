# Bandit Level 10

## Goal

The challenge provides a `data.txt` file containing Base64-encoded data. The task is to decode the content and recover the readable text without publishing the resulting credential.

## Approach

I first listed the files in the home directory and found `data.txt`.

```bash
ls
```

Then I inspected the file contents:

```bash
cat data.txt
```

The output looked like Base64-encoded text rather than normal readable text.

Before decoding it, I checked the command help to understand the available options:

```bash
base64 --help
```

From the help output, I learned that `-d` (or `--decode`) tells `base64` to decode input data.

I then decoded the file directly:

```bash
base64 -d data.txt
```

This converted the Base64 text back into its original readable form.

## Command Breakdown

```bash
base64 -d data.txt
```

- `base64` — encodes or decodes Base64 data.
- `-d` — decode mode.
- `data.txt` — the input file containing the encoded text.

The decoded result is printed to standard output in the terminal.

## What I Learned

- Base64 is an **encoding format**, not encryption.
- Encoded text can look unreadable even though it can be reversed without a secret key.
- `base64 -d` decodes Base64 data back to its original form.
- Checking `--help` is a useful way to discover command options instead of guessing them.
- A command can read directly from a file and print the result to standard output.

## Notes

The decoded password/credential is intentionally not included in this write-up.
