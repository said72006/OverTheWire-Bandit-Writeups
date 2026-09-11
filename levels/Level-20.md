# Bandit Level 20

## Goal

Use the provided `suconnect` program to retrieve the password for the next level.

The program connects to a TCP port on `localhost`. If the service on the other side sends the correct current password, `suconnect` sends back the next password.

> Passwords and active credentials are intentionally not published.

---

## Understanding the Program

Running the program without arguments showed:

```bash
./suconnect
```

Output:

```text
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP.
If it receives the correct password from the other side, the next password is transmitted back.
```

The important point is that `suconnect` is the **client**. It expects another process to already be listening on a local TCP port.

---

## Step 1 — Start a TCP Listener

In a second SSH session, I started Netcat on a local port:

```bash
nc -l -p 12345
```

At first nothing appeared, which is expected because Netcat was simply waiting for an incoming TCP connection.

---

## Step 2 — Connect with suconnect

In the first SSH session, I ran:

```bash
./suconnect 12345
```

This made `suconnect` connect to the Netcat listener on `localhost:12345`.

---

## Step 3 — Send the Current Password

Back in the Netcat session, I typed the current Bandit password and pressed Enter.

Netcat sent that password across the TCP connection to `suconnect`.

Because the password was correct, `suconnect` transmitted the next-level password back through the same connection.

The credential itself is intentionally not included here.

---

## Why This Works

The two processes form a simple local TCP client/server connection:

```text
Netcat listener
localhost:12345
      ↑
      │ TCP connection
      │
./suconnect 12345
```

`nc -l` waits for a connection, while `suconnect` actively connects to the chosen port.

The data flow is:

```text
current password
      ↓
Netcat
      ↓
TCP connection
      ↓
suconnect verifies it
      ↓
next password
      ↓
TCP connection
      ↓
Netcat displays it
```

---

## Commands Used

```bash
./suconnect
nc -l -p 12345
./suconnect 12345
```

---

## What I Learned

- A TCP connection needs a listening side and a connecting side.
- `nc -l` makes Netcat listen for incoming connections.
- `suconnect` acts as the TCP client in this challenge.
- A program waiting with no output is not necessarily stuck; it may simply be listening for a connection.
- Two terminal sessions can be useful when testing client/server communication locally.
- Data can travel in both directions over one TCP connection.

## Notes

The next-level password is intentionally not published.
