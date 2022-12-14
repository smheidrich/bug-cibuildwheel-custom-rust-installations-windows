#!/bin/bash
if ! cargo -V; then
  curl --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
else
  echo "Rust toolchain already installed, not downloading again"
fi

# dbg output
ls -la "$HOST_HOME_DIR"
ls -la "$HOST_HOME_DIR/.rustup"
cat "$HOST_HOME_DIR/.rustup/settings.toml"
rustc -V
echo "----------"
env
echo "----------"
python3 -c "import os; print(os.environ)"
echo "----------"
python3 -c "from subprocess import run; run(['rustc', '-V'])"
echo "----------"
#cargo -V
