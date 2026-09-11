# Bandit Level 19

## Goal

The home directory contains a **setuid (SUID) binary** that can be used to run commands as the next Bandit user.

The goal is to understand how the binary works and then use it to read the password for the next level from the usual location under `/etc/bandit_pass/`.

> Passwords and active credentials are intentionally not published.

---

## Step 1 — Inspect the Home Directory

I started with:

```bash
ls -lah
```

The important file was:

```text
-rwsr-x--- 1 bandit20 bandit19 ... bandit20-do
```

The key detail is the `s` in the owner's execute position:

```text
rws
  ^
  SUID bit
```

The file is owned by `bandit20`, so the SUID bit allows the program to run with the effective privileges of `bandit20`.

---

## Step 2 — Run the Binary Without Arguments

The challenge specifically said to execute the binary without arguments first:

```bash
./bandit20-do
```

It displayed usage information showing that it can run a command as another user.

Example:

```bash
./bandit20-do whoami
```

The output was:

```text
bandit20
```

This confirmed that commands passed through the SUID binary execute with the effective identity of `bandit20`.

---

## Step 3 — Understand the Password Directory

I first tried:

```bash
./bandit20-do cat /etc/bandit_pass
```

This failed because:

```text
/etc/bandit_pass
```

is a **directory**, not a file.

I also tried:

```bash
./bandit20-do cd /etc/bandit_pass
```

but that did not work.

The reason is that `cd` is a **shell builtin**, not a standalone executable in the same way as commands such as `cat` or `whoami`.

---

## Step 4 — Read the Correct Password File

The password files are stored using the username as the filename.

So I used the SUID helper to run `cat` as `bandit20`:

```bash
./bandit20-do cat /etc/bandit_pass/bandit20
```

Because the command was executed with the effective privileges of `bandit20`, it was able to read the password file for the next level.

The password itself is intentionally not included in this write-up.

---

## Why This Works

Normally, a process runs with the permissions of the user who launches it.

With a properly configured SUID executable:

```text
bandit19
   ↓
runs SUID binary owned by bandit20
   ↓
effective user becomes bandit20
   ↓
requested command runs with bandit20 privileges
   ↓
protected bandit20 file can be read
```

This is why SUID programs are security-sensitive: if they are designed incorrectly, they can allow privilege escalation.

---

## Commands Used

```bash
ls -lah
./bandit20-do
./bandit20-do whoami
./bandit20-do cat /etc/bandit_pass
./bandit20-do cd /etc/bandit_pass
./bandit20-do cat /etc/bandit_pass/bandit20
```

---

## What I Learned

- What the SUID permission bit looks like in `ls -l` output.
- How a SUID executable can run with the effective privileges of its owner.
- How to verify the effective identity by running `whoami`.
- The difference between a directory and a file when using `cat`.
- Why `cd` behaves differently from normal executables because it is a shell builtin.
- Why SUID binaries must be designed carefully because they can cross normal permission boundaries.
- How to use a deliberately provided SUID helper safely inside a CTF training environment.

## Notes

The next-level password is intentionally not published.
