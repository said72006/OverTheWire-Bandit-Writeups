# Bandit Level 13

## Goal

Use the SSH private key provided by the level to authenticate as the next Bandit user instead of using a password.

> The private key and any active credentials are intentionally not published.

---

## What I Found

Inside the home directory, I listed the available files:

```bash
ls
```

The important file was:

```text
sshkey.private
```

I checked its type with:

```bash
file sshkey.private
```

The result identified it as an **OpenSSH private key**.

This immediately told me that the next login should use SSH key authentication rather than a normal password.

---

## Important Hint From the Level

The level also included a `HINT` file. Reading it showed that logging in from one Bandit level directly to another through `localhost` is blocked in the current OverTheWire setup.

So instead of trying to SSH from the Bandit server itself, I had to:

1. Log out of Bandit.
2. Save the provided private key on my local Kali system.
3. Use that key from my own machine to connect to the next level.

---

## Step 1 — Save the Private Key Locally

I copied the full private key content into a local file named:

```text
bandit14.key
```

The actual key is not included in this write-up.

---

## Step 2 — Protect the Key File

SSH expects private keys to have restrictive permissions. I used:

```bash
chmod 600 ~/bandit14.key
```

`600` means:

```text
Owner: read + write
Group: no permissions
Others: no permissions
```

This is important because SSH may refuse to use a private key if other users can read it.

---

## Step 3 — Connect Using the Private Key

I used SSH with the `-i` option:

```bash
ssh -i ~/bandit14.key bandit14@bandit.labs.overthewire.org -p 2220
```

### Command Breakdown

- `ssh` starts the SSH client.
- `-i ~/bandit14.key` tells SSH which identity/private key file to use.
- `bandit14@bandit.labs.overthewire.org` specifies the target user and host.
- `-p 2220` connects to the custom SSH port used by Bandit.

After the key was accepted, I successfully reached the `bandit14` shell.

---

## Troubleshooting I Encountered

My first local attempt produced an error similar to:

```text
Warning: Identity file bandit14.key not accessible: No such file or directory.
```

Because SSH could not find the key file, it fell back to asking for a password.

The lesson was simple but important: `-i` does not contain the key itself. It points to a **real local file path**, so the key file must actually exist at that location before SSH can use it.

Using the absolute/home-relative path also makes the command clearer:

```bash
~/bandit14.key
```

---

## What I Learned

- SSH can authenticate with a private key instead of a password.
- The `-i` option selects the private key file used for authentication.
- Private keys should have restrictive permissions such as `chmod 600`.
- An `Identity file ... not accessible` error means SSH cannot find or read the specified local key file.
- If SSH cannot use the requested key, it may fall back to another authentication method such as a password.
- A private SSH key is a credential and should never be published in a repository.

---

## Notes

This level was different from the earlier password-based SSH levels because the authentication material was a private key file.

The key itself is intentionally omitted from this repository.