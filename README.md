# pathology

Provide a a subclass of pathlib's Path that adds a static script_dir() method to Path, which returns the Path to the
directory of the calling script. It could have been just a standalone function, but for discoverability reasons it
seems better to stick it on top of pathlib's Path.

# Usage

It's a drop-in replacement to pathlib's Path:

```
from pathology import Path

print('The script dir is:', Path.script_dir())

```
