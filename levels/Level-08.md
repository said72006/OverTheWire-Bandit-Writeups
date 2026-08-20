# Bandit Level 8

## Goal

Identify the only line in `data.txt` that occurs exactly once.

## Approach

The file contains many repeated lines, so the useful strategy was to group identical lines together first, then count how many times each line appears.

I first used `sort` so duplicate lines would become adjacent. After that, I passed the sorted output directly into `uniq -c` using a pipe.

This made it easy to spot the single line whose count was `1`.

## Commands Used

```bash
sort data.txt
sort data.txt | uniq -c
```

## Command Breakdown

### `sort data.txt`

Sorts all lines in the file. This is important because `uniq` compares adjacent lines, so duplicates need to be next to each other first.

### `|`

The pipe sends the standard output of the command on the left directly into the standard input of the command on the right.

In this case:

```text
sort output → uniq input
```

### `uniq -c`

`uniq` processes repeated adjacent lines, while `-c` prefixes each resulting line with the number of times it occurred.

So the result becomes a frequency list, and the required line is the one with a count of `1`.

## What I Learned

- `sort` can prepare data for later filtering.
- `uniq` works best when duplicate lines are adjacent.
- `uniq -c` counts occurrences of each line.
- Pipes (`|`) allow Linux commands to be chained together.
- Combining simple commands is often more powerful than searching manually through large output.

## Notes

The password and exact target line are intentionally not published.
