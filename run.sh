#!/usr/bin/env bash
set -euo pipefail

# --------------------------------------------------
# 各サービスのDockerビルドと実行をオーケストレーションするスクリプト
# Makefile.toml タスクに対して `cargo-make` を使って実行する
# --------------------------------------------------

info() {
  echo "\033[1;34m[INFO]\033[0m $*"
}

error() {
  echo "\033[1;31m[ERROR]\033[0m $*" >&2
}

# cargo-make (makers) がインストールされているか確認
if ! command -v makers &>/dev/null && ! command -v cargo-make &>/dev/null; then
  error "cargo-make (makers) is not installed. Please install with: cargo install cargo-make"
  exit 1
fi

# cargo-make がインストールされている場合は cargo make を使う
CARGO_MAKE_CMD="makers"
if ! command -v makers &>/dev/null; then
  CARGO_MAKE_CMD="cargo make"
fi

# ------------------------------------
# service_a
# ------------------------------------
info "Starting service_a containers via Makefile.toml..."

pushd service_a >/dev/null
# e.g. run-in-docker で proto生成 → docker compose up
$CARGO_MAKE_CMD run-in-docker
popd >/dev/null

# ------------------------------------
# service_b
# ------------------------------------
info "Starting service_b containers via Makefile.toml..."

pushd service_b >/dev/null
$CARGO_MAKE_CMD run-in-docker
popd >/dev/null

info "All services started!"
