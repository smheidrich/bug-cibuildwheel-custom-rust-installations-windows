Resolution: Not a bug, I just didn't understand Windows and cibuildwheel:

- In `PATH` given to cibuildwheel, you *have to* separate path components with
  backslashes and paths with `;` instead of `:`.
  - Confusing when debugging: `bash` running on Windows *will* understand
    slashes in `PATH`, only Windows's native shell and whatever its `exec()`
    equivalent is won't. cibuildwheel uses the latter to run Python.
- Outputting env vars into `$GITENV` from bash causes them to be UNIX-formatted
  (in particular ones like `$PATH`) because MSYS's bash transforms them
  apparently. So don't do that.
- `$PWD` is always UNIX-formatted on Windows, even in its native shell AFAICT.
  Same for the output of `pwd` (presumably provided by MSYS). Just use
  `$GITHUB_WORKSPACE` instead, no idea what the proper way is to get cwd.
- Another confusing `PATH` quirk that made debugging harder: Windows will
  prefer executables ending in `.exe` even if they appear later in `PATH` than
  ones without. At least I think so. There is another env var called `PATHEXT`
  that determines the prioritization of suffixes.
