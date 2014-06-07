J4S_DIR="$(dirname "$(readlink -f "$(command -v "$0")")")"
export PATH="$PATH:$J4S_DIR/bin"
unset J4S_DIR
