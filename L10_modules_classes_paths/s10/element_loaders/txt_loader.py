from pathlib import Path


def read_txt_file(filepath: Path) -> str:
    """_summary_

    Args:
        filepath (Path): _description_

    Raises:
        ValueError: _description_
        FileNotFoundError: _description_
        RuntimeError: _description_

    Returns:
        str: _description_
    """
    if filepath.suffix.lower() != '.txt':
        raise ValueError(f"Nem támogatott fájltípus: {filepath.suffix} (csak .txt engedélyezett)")

    if not filepath.exists():
        raise FileNotFoundError(f"A fájl nem található: {filepath}")

    try:
        with filepath.open('r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        raise RuntimeError(f"Hiba történt a fájl olvasása közben: {e}")
