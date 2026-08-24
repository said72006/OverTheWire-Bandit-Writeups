# Bandit Level 11

## Goal

Decode the contents of `data.txt`, where every uppercase and lowercase letter has been rotated by 13 positions using **ROT13**.

## Approach

I first checked the available options for `tr` and experimented with the command syntax.

Some early attempts treated `data.txt` as if it were a direct argument to `tr` and also used `-c`, but the help output clarified two important points:

- `tr` expects character sets such as `SET1` and `SET2` when translating.
- `-c` means **complement**, not decode.
- `tr` reads its input from standard input, so the file contents need to be piped or redirected into it.

Because ROT13 maps each letter to the letter 13 positions later in the alphabet, I translated the uppercase and lowercase ranges to their ROT13 equivalents.

## Commands Used

```bash
tr --help
whatis tr
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

An equivalent form using input redirection is:

```bash
tr 'A-Za-z' 'N-ZA-Mn-za-m' < data.txt
```

### Command Breakdown

- `tr` translates characters from one set into another.
- `'A-Za-z'` represents all uppercase and lowercase English letters.
- `'N-ZA-Mn-za-m'` represents the same letters shifted by 13 positions.
- `|` sends the output of `cat data.txt` into `tr` through standard input.
- `< data.txt` is another way to provide the file as standard input without using `cat`.

## What I Learned

- ROT13 is a simple substitution encoding where every letter is shifted by 13 positions.
- Applying ROT13 a second time returns the original text.
- `tr` works with character sets rather than filenames when translating.
- `tr` reads from standard input by default.
- The `-c` option in `tr` means complement and is unrelated to decoding.
- Pipes and input redirection can both be used to feed file contents into commands.

## Notes

The password and active credentials are intentionally not published.
