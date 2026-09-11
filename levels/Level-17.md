# Bandit Level 17

## Goal

The home directory contains two files:

```text
passwords.old
passwords.new
```

The password for the next level is the **only line that changed** between these two files.

> Passwords and active credentials are intentionally not published.

---

## Approach

This level is about comparing two text files and identifying the line that is different.

The most direct tool for this is:

```bash
diff
```

I compared the old and new password files:

```bash
diff passwords.old passwords.new
```

The output from `diff` marks lines from the first file with:

```text
<
```

and lines from the second file with:

```text
>
```

Since the challenge says the next password is stored in `passwords.new`, the important changed line is the one prefixed with:

```text
>
```

That line is the new value.

---

## Commands Used

```bash
ls
diff passwords.old passwords.new
```

---

## Understanding the diff Output

For two files:

```bash
diff file1 file2
```

the symbols mean:

```text
<  line from file1
>  line from file2
```

In this challenge:

```text
file1 = passwords.old
file2 = passwords.new
```

So:

```text
<  old value
>  new value
```

The new line is the credential needed for the next level.

---

## Verification

After retrieving the new password, I used it to authenticate as the next Bandit user over SSH.

The SSH login succeeded, but the session immediately displayed:

```text
Byebye !
```

This does **not** mean the password is wrong. The Bandit level description warns that this behavior is related to the next level's shell configuration.

So successful authentication followed by `Byebye!` confirms that Level 17 was solved correctly.

---

## What I Learned

- How to compare two text files using `diff`.
- How to interpret `<` and `>` in standard `diff` output.
- Why the order of the files in a `diff` command matters.
- How to identify the updated value when comparing old and new files.
- That successful SSH authentication can still be followed by an immediate logout if the remote shell is configured that way.
- Why it is important to read the challenge notes before assuming an authentication failure.

## Notes

The password itself is intentionally not included in this write-up.
