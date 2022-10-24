#!/bin/bash
if ! cargo -V; then
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
else
  echo "Rust toolchain already installed, not downloading again"
fi
