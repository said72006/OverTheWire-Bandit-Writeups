# Bandit Level 6

## Goal

Locate a file somewhere on the server that matches three properties:

- owned by user `bandit7`
- owned by group `bandit6`
- exactly 33 bytes in size

Passwords and exact target paths are intentionally omitted.

## Approach

I first checked my home directory with `ls` and `ls -lah`, but the visible files there were owned by `root`, so the target was clearly not in the current directory.

I then started experimenting with `find` and gradually added the conditions from the challenge:

```bash
find -size 3c
find -type f -user bandit7 -group bandit6
find -type f -user bandit7 -group bandit6 -size 33c
```

These searches start from the current directory when no search path is supplied, so they did not find the server-wide target.

The important change was starting from the filesystem root:

```bash
find / -type f -user bandit7 -group bandit6 -size 33c
```

This searched the whole server and did locate a matching file, but it also printed a very large number of `Permission denied` messages because my user cannot read every directory on the system.

I also tried using `sudo`, but Bandit does not provide normal sudo privileges for this account. The search itself did not require sudo.

To make the useful result easier to see, I redirected the error output:

```bash
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

This produced a clean result containing the matching file without filling the terminal with permission errors.

After identifying the file, I read it with `cat` to obtain the credential for the next level. The credential and exact target path are not published here.

## Command Breakdown

```bash
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
```

- `find` — searches for filesystem entries.
- `/` — start from the root of the filesystem, so the search covers the server rather than only the current directory.
- `-type f` — only match regular files.
- `-user bandit7` — only match files owned by user `bandit7`.
- `-group bandit6` — only match files whose group owner is `bandit6`.
- `-size 33c` — only match files exactly 33 bytes in size. In `find`, the `c` suffix represents bytes.
- `2>/dev/null` — discard error messages while keeping normal results visible.

### Understanding `2>/dev/null`

Linux commands normally have separate output streams:

- file descriptor `1` = standard output (`stdout`)
- file descriptor `2` = standard error (`stderr`)

In this command:

```bash
2>/dev/null
```

- `2` selects the standard error stream.
- `>` redirects that stream somewhere else.
- `/dev/null` is a special device that discards anything written to it.

So the normal matching result still appears on the screen, while messages such as `Permission denied` are hidden.

This does **not** give extra permissions or bypass access controls. It only hides the error messages that the search generates while entering directories I am not allowed to read.

## What I Learned

- `find` can combine multiple filters in one search.
- A search path matters: `find / ...` searches from the filesystem root, while omitting `/` limits the search to the current location.
- Linux file ownership has both a **user owner** and a **group owner**.
- `-size 33c` means exactly 33 bytes.
- `Permission denied` is expected when searching the whole filesystem as an unprivileged user.
- `2>/dev/null` is useful when I want to suppress expected error output and focus on valid results.
- Redirecting errors is different from gaining privileges; it only changes where the errors are displayed.

## Notes

The failed attempts were useful because they showed me that the target was not in my home directory and that I needed to search from `/` instead of only the current directory.

Passwords, credentials, and the exact solution path are intentionally not published.