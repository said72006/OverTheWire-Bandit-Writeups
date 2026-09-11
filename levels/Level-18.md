# Bandit Level 18

## Goal

Logging in to the next account with SSH immediately closes the interactive shell and prints:

```text
Byebye!
```

The goal is to retrieve the password stored in the remote `readme` file despite the shell exiting immediately.

> Passwords and active credentials are intentionally not published.

---

## What Happened

A normal SSH login authenticated successfully, but the remote session immediately terminated.

That meant the problem was **not the password**. Instead, the remote shell configuration was causing the interactive session to exit.

So instead of opening a normal shell, I used SSH to execute commands directly on the remote host.

---

## Step 1 — List the Remote Files

I ran:

```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 ls
```

After authenticating, SSH executed `ls` remotely without opening the normal interactive shell.

The output showed:

```text
readme
```

This confirmed that remote command execution still worked even though the normal shell immediately logged out.

---

## Step 2 — Read the File Directly

I then executed:

```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
```

After authentication, the remote `cat` command read the file and returned the credential for the next level.

The credential itself is intentionally not included here.

---

## Why This Works

SSH is not only used to open an interactive terminal.

It can also run a single command remotely:

```bash
ssh user@host command
```

The difference is:

```text
Normal SSH login
      ↓
starts remote interactive shell
      ↓
shell configuration exits
      ↓
Byebye!

SSH with remote command
      ↓
runs the requested command directly
      ↓
prints command output
      ↓
connection closes
```

This bypassed the problematic interactive-shell behavior without changing anything on the server.

---

## Commands Used

```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 ls
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
```

---

## What I Learned

- Successful authentication and an immediate logout are two separate things.
- SSH can execute commands remotely without opening an interactive shell.
- The general syntax is `ssh user@host command`.
- Remote commands can be used to inspect files and retrieve output even when the login shell is restricted or exits.
- Error messages and challenge notes can reveal whether the issue is authentication or shell behavior.

## Notes

The password for the next level is intentionally not published.
