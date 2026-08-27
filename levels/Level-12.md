# Bandit Level 12

## Goal

The challenge provides `data.txt`, but the file is not the original data. It is a **hexdump** of a file that has been compressed several times using different formats.

The goal is to:

1. Work in a writable temporary directory.
2. Reverse the hexdump back into a binary file.
3. Identify the current file type.
4. Decompress or extract one layer at a time.
5. Repeat until the final file becomes readable text.

> The password itself is intentionally not published.

---

## The Main Idea

The most important thing I learned from this level is that I should **not guess the compression format**.

After every step, I used:

```bash
file <filename>
```

This tells me what the file actually is. Then I choose the correct tool for that type.

My workflow became:

```text
hexdump
   ↓ xxd -r
gzip
   ↓ gzip -d
bzip2
   ↓ bzip2 -d
gzip
   ↓ gzip -d
tar
   ↓ tar -xf
tar
   ↓ tar -xf
bzip2
   ↓ bzip2 -d
tar
   ↓ tar -xf
gzip
   ↓ gzip -d
ASCII text
```

So the challenge is really a chain of layers.

---

## Step 1 — Create a Temporary Working Directory

The Bandit home directory is not writable for creating arbitrary files, so I needed a directory under `/tmp`.

I first experimented with `mktemp` and learned that a custom template requires `X` characters. The simpler command was:

```bash
mktemp -d
```

It created a unique directory similar to:

```text
/tmp/tmp.XXXXXXXXXX
```

Then I entered it and copied the challenge file there:

```bash
cd /tmp/tmp.XXXXXXXXXX
cp ~/data.txt .
```

### Why this matters

- `/tmp` is intended for temporary files.
- `mktemp -d` creates a unique directory safely.
- `cp ~/data.txt .` copies `data.txt` from the home directory into the current directory.
- `.` means **the current directory**.

I did **not** need `sudo` for this level.

---

## Step 2 — Reverse the Hexdump

`data.txt` looked like this:

```text
00000000: 1f8b 0808 ...
00000010: ...
```

That is a hexdump, not the original binary file.

I checked `xxd`:

```bash
xxd -h
whatis xxd
```

The important option was:

```text
-r    reverse operation: convert hexdump into binary
```

So I used:

```bash
xxd -r data.txt > data.bin
```

### Command breakdown

- `xxd -r` reverses a hexdump.
- `data.txt` is the input.
- `>` redirects the binary output into `data.bin`.

Then I checked the real file type:

```bash
file data.bin
```

Result: **gzip compressed data**.

---

## Step 3 — First gzip Layer

Because `file` identified the file as gzip data, I renamed it with a `.gz` extension and decompressed it:

```bash
mv data.bin data.gz
gzip -d data.gz
```

Then:

```bash
file data
```

Result: **bzip2 compressed data**.

### Why rename it?

The contents determine the real file type, but using the expected extension makes commands such as `gzip` and `bzip2` easier to work with and keeps the process understandable.

---

## Step 4 — bzip2 Layer

The next layer was bzip2:

```bash
mv data data.bz2
bzip2 -d data.bz2
```

Then I checked again:

```bash
file data
```

Result: **gzip compressed data** again.

This showed me that the same compression type can appear more than once in the chain.

---

## Step 5 — Second gzip Layer

I repeated the gzip process:

```bash
mv data data.gz
gzip -d data.gz
file data
```

This time the result was:

```text
POSIX tar archive (GNU)
```

A tar archive is different from gzip/bzip2: it is an **archive container**, so I needed `tar` instead of a compression decoder.

---

## Step 6 — First tar Archive

Before extracting, I could inspect the archive contents with:

```bash
tar -tf data
```

Then extract it:

```bash
tar -xf data
```

### tar options

- `-t` = list files inside the archive.
- `-x` = extract files.
- `-f` = use the following archive file.

After extraction, a new file appeared: `data5.bin`.

I checked it:

```bash
file data5.bin
```

Result: another **POSIX tar archive**.

---

## Step 7 — Second tar Archive

I inspected it first:

```bash
tar -tf data5.bin
```

It contained:

```text
data6.bin
```

Then I extracted it:

```bash
tar -xf data5.bin
```

And checked the new file:

```bash
file data6.bin
```

Result: **bzip2 compressed data**.

---

## Step 8 — Second bzip2 Layer

I renamed and decompressed it:

```bash
mv data6.bin data6.bz2
bzip2 -d data6.bz2
```

Then:

```bash
file data6
```

Result: **POSIX tar archive**.

---

## Step 9 — Third tar Archive

I listed the archive contents:

```bash
tar -tf data6
```

It contained:

```text
data8.bin
```

Then extracted it:

```bash
tar -xf data6
```

Checking the new file:

```bash
file data8.bin
```

Result: **gzip compressed data**.

---

## Step 10 — Final gzip Layer

I decompressed the last gzip layer:

```bash
mv data8.bin data8.gz
gzip -d data8.gz
```

Then:

```bash
file data8
```

Result:

```text
ASCII text
```

That was the important sign that the compression chain was finished.

Finally, the readable content can be displayed with:

```bash
cat data8
```

The resulting password is intentionally omitted from this write-up.

---

## Commands Used

```bash
mktemp -d
cd
cp
ls
xxd -h
whatis xxd
xxd -r data.txt > data.bin
file data.bin
mv
gzip -d
bzip2 -d
tar -tf
tar -xf
cat
```

---

## What I Learned

### 1. File extensions are not enough

A filename such as `.bin` does not tell me what the file really contains. The `file` command inspects the content and identifies the actual format.

### 2. A hexdump is a representation, not the original file

`xxd -r` converts the hexadecimal representation back into the original binary bytes.

### 3. Compression can be nested

A file can contain another compressed file, which can contain another archive, and so on. I need to process one layer at a time.

### 4. Different formats need different tools

| File type | Tool used |
|---|---|
| Hexdump | `xxd -r` |
| gzip | `gzip -d` |
| bzip2 | `bzip2 -d` |
| tar archive | `tar -xf` |
| ASCII text | `cat` |

### 5. `file` was the key command

Instead of guessing what to do next, I repeatedly used:

```bash
file <new-file>
```

That made the challenge systematic:

```text
Identify → Process → Identify again → Process again
```

### 6. `tar` is not the same as gzip or bzip2

`gzip` and `bzip2` compress data. `tar` packages files into an archive. That is why the commands are different.

### 7. Temporary directories are useful

`mktemp -d` gave me a safe writable workspace without modifying the original challenge file.

---

## Mistakes That Helped Me Learn

I initially tried creating output files in the Bandit home directory and received:

```text
Permission denied
```

I also tried using `sudo`, but this environment does not allow it and it was not needed anyway.

Another important mistake was running `xxd` without `-r`. Normal `xxd` creates a hexdump, but the challenge already gave me a hexdump. I needed the **reverse** operation:

```bash
xxd -r
```

These mistakes helped make the purpose of `/tmp`, permissions, and `xxd -r` much clearer.

---

## Final Mental Model

For this level, I can remember one simple loop:

```text
1. Run file
2. Read the detected type
3. Use the matching extraction/decompression tool
4. Run file again
5. Repeat until it says ASCII text
```

That is the main lesson of Bandit Level 12.