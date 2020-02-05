import csv
import sqlite3
import subprocess
from pathlib import Path

import click
from tqdm import tqdm


def define(word: str, dictionary="gcide") -> str:
    # word = unicodedata.normalize('NFKD',row[1]).encode('ascii','ignore')
    definition = subprocess.run(["dico", "-d", dictionary, word], capture_output=True)

    return definition.stdout.decode()


@click.command()
@click.option(
    "--vocab",
    help="Path to kindle vocab.db",
    required=True,
    type=click.Path(exists=True, readable=True),
)
@click.option(
    "--dictionary", help="dico dictionary server", default="gcide", required=True,
)
@click.option(
    "-o",
    "--ouput_file",
    help="Path to output file",
    required=True,
    type=click.Path(writable=True),
)
def run(vocab: str, dictionary: str, ouput_file: str):
    out = []
    conn = sqlite3.connect(vocab)
    query = "select word, stem from words where length(word)>4"  # don't care about accidentals
    rows = conn.execute(query).fetchall()

    for row in tqdm(rows):
        definition = define(word := row[0])
        if not definition:
            print(f"Couldn't find a definition for {word}")
        out.append((f"{word} ({row[1]})", definition))
    with open(ouput_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(out)


if __name__ == "__main__":
    run()
