import os
import shutil

# The Perfect Pickup Line: copy the pre-written entry to the output dir.
# Stdlib only — no rendering, no generation, no network.
def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))

if __name__ == "__main__":
    main()
