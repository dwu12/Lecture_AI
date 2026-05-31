from markdown_pdf import MarkdownPdf, Section


def generate_lecture_pdf(
    markdown_content: str,
    output_path: str,
    title: str | None = None,
):
    """
    Generate a PDF from a markdown string using markdown_pdf.

    Args:
        markdown_content: Full markdown text to convert.
        output_path: Path to save the PDF.
        title: Optional document title (used in PDF metadata).
    """
    custom_css = """
    body {
        font-family: 'Helvetica Neue', Arial, sans-serif;
        color: #333333;
        line-height: 1.6;
        font-size: 10.5pt;
        background-color: #FFFFFF !important;
    }
    div, section, article, span, a, label, mark, del, ins, s {
        background-color: #FFFFFF !important;
    }
    h1 {
        color: #1F4E79;
        border-bottom: 2px solid #1F4E79;
        padding-bottom: 6px;
        font-size: 18pt;
        margin-top: 24px;
        margin-bottom: 8px;
        background-color: #FFFFFF !important;
    }
    h2 {
        color: #2E75B6;
        font-size: 14pt;
        margin-top: 18px;
        margin-bottom: 6px;
        background-color: #FFFFFF !important;
    }
    h3 {
        color: #404040;
        font-size: 11pt;
        margin-top: 14px;
        margin-bottom: 4px;
        background-color: #FFFFFF !important;
    }
    p {
        margin-top: 4px;
        margin-bottom: 4px;
        background-color: #FFFFFF !important;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin-top: 12px;
        margin-bottom: 12px;
        font-size: 9.5pt;
    }
    th {
        background-color: #D9E2F3 !important;
        color: #1F4E79;
        font-weight: bold;
        border: 1px solid #BBBBBB;
        padding: 6px 10px;
        text-align: left;
    }
    td {
        border: 1px solid #BBBBBB;
        padding: 5px 10px;
        text-align: left;
        vertical-align: top;
    }
    tr:nth-child(even) {
        background-color: #F5F5F5;
    }
    tr:nth-child(odd) {
        background-color: #FFFFFF;
    }
    hr {
        border: none;
        border-top: 1px solid #DDDDDD;
        margin: 16px 0;
    }
    strong {
        color: #1F4E79;
    }
    em {
        color: #555555;
    }
    code {
        font-family: 'Courier New', Courier, monospace;
        background-color: #F5F5F5;
        padding: 1px 4px;
        border-radius: 3px;
        font-size: 9pt;
    }
    blockquote {
        border-left: 4px solid #2E75B6;
        padding-left: 12px;
        margin-left: 0;
        color: #555555;
        font-style: italic;
        background-color: #FFFFFF !important;
    }
    ul, ol {
        margin-top: 4px;
        margin-bottom: 4px;
        padding-left: 24px;
        background-color: #FFFFFF !important;
    }
    li {
        margin-top: 2px;
        margin-bottom: 2px;
        background-color: #FFFFFF !important;
    }
    li > ul, li > ol {
        margin-top: 2px;
        margin-bottom: 2px;
    }
    """

    pdf = MarkdownPdf()
    pdf.meta["title"] = title if title else "Lecture Notes"

    pdf.add_section(Section(markdown_content, toc=False), user_css=custom_css)
    pdf.save(output_path)
    return output_path
