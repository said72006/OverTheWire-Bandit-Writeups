# Bandit Level 15

## Goal

The challenge requires submitting the current level password to a service running on `localhost` port `30001`, but unlike the previous level, this connection must use **SSL/TLS encryption**.

> The password and active credentials are intentionally not published.

---

## Approach

I first inspected the available OpenSSL commands:

```bash
openssl
```

From the command list, I identified `s_client` as the OpenSSL client used for connecting to SSL/TLS services.

Then I checked its help page:

```bash
openssl s_client -help
```

The important option was:

```text
-connect val    TCP/IP where to connect
```

So I connected to the local TLS service on port `30001`:

```bash
openssl s_client -connect localhost:30001
```

After the TLS connection was established, I submitted the current level password through the connection and received the credential for the next level.

---

## Why Netcat Was Not Enough

In the previous level, a plain TCP connection worked with:

```bash
nc localhost 30000
```

This level specifically requires SSL/TLS encryption. `nc` can create a basic TCP connection, but it does not perform the TLS handshake required by this service.

That is why `openssl s_client` was the appropriate tool.

---

## Useful Troubleshooting Option

The challenge notes that OpenSSL can sometimes interpret interactive input as commands such as `DONE`, `RENEGOTIATING`, or `KEYUPDATE`.

From the help output, the following option can disable interactive command processing:

```bash
openssl s_client -connect localhost:30001 -quiet -no-interactive
```

This is useful if normal input is accidentally interpreted as an OpenSSL connected command.

---

## What I Learned

- `openssl s_client` can be used to manually connect to SSL/TLS-enabled network services.
- `-connect host:port` specifies the destination service.
- `localhost` refers to the current machine.
- A normal TCP connection and a TLS-protected TCP connection are not the same thing.
- TLS adds encryption and a handshake on top of the underlying TCP connection.
- Reading command help is often enough to identify the correct option instead of memorizing syntax.

---

## Notes

The password and other active credentials are intentionally omitted from this write-up.