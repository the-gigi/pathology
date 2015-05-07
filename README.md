# pathology
A subclass of pathlib's Path that adds a static script_dir() method to Path, which returns the Path to the directory of the calling script. It could have been just a standalone function, but for discoverability reasons it seems better to stick it on top of the pathlib's Path.
