# Bandit Level 16

## Goal

The next credentials are available from **one service on localhost** somewhere in the TCP port range `31000-32000`.

The task is to:

1. Find which ports in the range are open.
2. Determine which open services use SSL/TLS.
3. Distinguish the real credential service from echo services.
4. Submit the current password to the correct TLS service.
5. Retrieve the next-level credential.

> Passwords, private keys, and active credentials are intentionally not published.

---

## Step 1 — Scan the Port Range

My first attempts missed the `-p` option:

```bash
nmap 31000-32000 localhost
```

Without `-p`, Nmap treated `31000-32000` like a hostname instead of a port range.

The correct syntax was:

```bash
nmap -p 31000-32000 localhost
```

This found several open ports inside the requested range.

### What I Learned

- `-p` tells Nmap which ports to scan.
- `31000-32000` is a port range.
- `localhost` refers to the current machine, normally `127.0.0.1`.

---

## Step 2 — Identify the Services

Finding open ports was not enough because the challenge said some services use SSL/TLS and others do not.

I used service/version detection:

```bash
nmap -sV -p 31000-32000 localhost
```

The important result was that some ports were normal echo services, while two were detected as SSL/TLS services.

One TLS port was identified as an echo service, while another TLS service returned a message asking for the correct current password.

That difference was the clue that the second TLS service was the target.

### Useful Nmap Option

```text
-sV = probe open ports to identify the service/version
```

---

## Step 3 — Connect to the TLS Service

I connected with OpenSSL:

```bash
openssl s_client -connect localhost:<PORT>
```

The connection showed a self-signed certificate. That is normal in this training environment and did not prevent the TLS connection from working.

I also tested options such as:

```bash
-quiet
-no-interactive
```

but the important Bandit hint was about OpenSSL's **CONNECTED COMMANDS**.

Some input characters can be interpreted by `s_client` as interactive commands instead of being sent as normal data. The useful option here was:

```bash
-nocommands
```

This disables those interactive command letters while still allowing input data to be sent.

---

## Step 4 — Submit the Current Password

Instead of manually typing the current password, I piped it directly into the TLS connection:

```bash
cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:<TARGET_PORT> -quiet -nocommands
```

Command flow:

```text
cat current password
        ↓
       pipe |
        ↓
OpenSSL TLS connection
        ↓
correct localhost service
        ↓
next-level credential
```

The correct service returned an **OpenSSH private key** for the next level.

The private key is intentionally not included in this write-up.

---

## Why the Other Ports Were Wrong

The challenge specifically said that the other servers would simply return whatever was sent to them.

Nmap helped identify several of these as:

```text
echo
ssl/echo
```

An echo service is not giving new information; it just sends the same input back.

So the process was not simply:

```text
find an open port
```

It was:

```text
find open ports
   ↓
identify services
   ↓
find TLS services
   ↓
separate TLS echo from the real TLS service
   ↓
submit the password
```

---

## Commands Used

```bash
nmap -p 31000-32000 localhost
nmap -sV -p 31000-32000 localhost
openssl s_client -connect localhost:<PORT>
cat /etc/bandit_pass/bandit16 | openssl s_client -connect localhost:<TARGET_PORT> -quiet -nocommands
```

---

## What I Learned

- How to scan a specific TCP port range with Nmap.
- Why `-p` is required when specifying ports.
- How `-sV` helps identify services running on open ports.
- How to distinguish plain echo services from TLS services.
- How to use `openssl s_client` to interact with SSL/TLS services.
- Why `-nocommands` can matter when sending arbitrary text through OpenSSL.
- How pipes can send command output directly into another program.
- Why service behavior is just as important as whether a port is open.
- Why private keys must be treated as credentials and never published.

## Notes

This level combines **port scanning, service enumeration, TLS testing, and credential handling** in one workflow.

The final password/private key is intentionally not published.
