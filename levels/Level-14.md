# Bandit Level 14

## Goal

Retrieve the password for the next level by submitting the current level password to a service listening on **port 30000 on localhost**.

> Passwords and active credentials are intentionally not published.

---

## Approach

The challenge gives two important pieces of information:

- The service is running on `localhost`, which means the same Bandit machine I am currently logged into.
- The service is listening on TCP port `30000`.

I used Netcat (`nc`) to connect to that local service and submit the current level password.

---

## First Attempt

I initially tried:

```bash
nc -p 30000
```

This returned the Netcat usage message.

The mistake was misunderstanding the `-p` option. In this implementation of `nc`, `-p` specifies the **local/source port**, not the destination port I want to connect to.

The command syntax shows that the destination host and port should be passed as positional arguments:

```text
nc [destination] [port]
```

---

## Correct Connection

I then connected to the service with:

```bash
nc localhost 30000
```

After the connection opened, I submitted the current Bandit password as input. The service validated it and returned the credential required for the next level.

---

## Command Breakdown

```bash
nc localhost 30000
```

- `nc` — Netcat, a simple command-line tool for reading from and writing to network connections.
- `localhost` — the current machine itself, normally resolved to the loopback interface.
- `30000` — the destination TCP port where the challenge service is listening.

The important distinction I learned is:

```text
-p 30000          -> chooses a source/local port
localhost 30000   -> connects to destination port 30000
```

---

## What I Learned

- `localhost` refers to the same machine I am currently using.
- Network services can listen on specific TCP or UDP ports.
- Netcat can be used to interact manually with simple TCP services.
- Command-line options are not interchangeable with positional arguments.
- Reading an error or usage message can reveal the exact syntax a command expects.
- A service may accept text input over a network connection and return a response directly in the terminal.

---

## Notes

This level introduced a basic but important networking idea: connecting to a service by specifying a **host and destination port**.

The credential returned by the service is intentionally not included in this write-up.
