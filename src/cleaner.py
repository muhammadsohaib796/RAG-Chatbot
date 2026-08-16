import re


def clean_text(text: str) -> str:
    """
    Clean text extracted from PDF documents.

    The cleaner removes obvious PDF extraction noise,
    normalizes whitespace, and preserves meaningful
    paragraph structure.
    """

    # Remove obvious PDF encoding / extraction noise
    text = re.sub(
        r"--`+[,`-]+",
        " ",
        text
    )

    # Remove table of contents leader dots
    # Example:
    # "Introduction ................. v"
    # becomes:
    # "Introduction v"
    text = re.sub(
        r"\.{4,}",
        " ",
        text
    )

    # Normalize tabs and repeated horizontal spaces
    text = re.sub(
        r"[ \t]+",
        " ",
        text
    )

    # Remove spaces immediately before newlines
    text = re.sub(
        r" +\n",
        "\n",
        text
    )

    # Remove excessive blank lines
    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text
    )

    return text.strip()


def clean_documents(documents):
    """
    Clean page content while preserving metadata.
    """

    for document in documents:
        document.page_content = clean_text(
            document.page_content
        )

    return documents