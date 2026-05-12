import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, ListFlowable, ListItem
from reportlab.lib.enums import TA_CENTER, TA_LEFT


def generate_lecture_pdf(
    lecture_notes: str,
    task_summary: str,
    output_path: str,
    title: str = "Lecture Notes"
):
    """
    Generate a PDF from lecture notes and task summary.

    Args:
        lecture_notes: Markdown-formatted lecture notes
        task_summary: Task summary text
        output_path: Path to save the PDF
        title: Title for the document
    """
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    doc = SimpleDocTemplate(output_path, pagesize=letter)
    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontSize=24,
        spaceAfter=30,
    )

    heading1_style = ParagraphStyle(
        "CustomHeading1",
        parent=styles["Heading1"],
        fontSize=16,
        spaceAfter=12,
        spaceBefore=12,
    )

    heading2_style = ParagraphStyle(
        "CustomHeading2",
        parent=styles["Heading2"],
        fontSize=13,
        spaceAfter=8,
        spaceBefore=8,
    )

    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["BodyText"],
        fontSize=11,
        spaceAfter=6,
    )

    story = []

    # Title
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 0.2 * inch))

    # Parse and render lecture notes
    story.append(Paragraph("Lecture Notes", heading1_style))

    for line in lecture_notes.split("\n"):
        line = line.strip()
        if not line:
            story.append(Spacer(1, 0.1 * inch))
        elif line.startswith("# "):
            story.append(Paragraph(line[2:], heading1_style))
        elif line.startswith("## "):
            story.append(Paragraph(line[3:], heading2_style))
        elif line.startswith("### "):
            story.append(Paragraph(line[4:], styles["Heading3"]))
        elif line.startswith("- ") or line.startswith("* "):
            story.append(Paragraph(f"• {line[2:]}", body_style))
        elif line.startswith("  - ") or line.startswith("    * "):
            story.append(Paragraph(f"&nbsp;&nbsp;&nbsp;&nbsp;• {line[4:]}", body_style))
        else:
            story.append(Paragraph(line, body_style))

    # Task Summary Section
    if task_summary and task_summary.strip():
        story.append(PageBreak())
        story.append(Paragraph("Task Summary", heading1_style))
        story.append(Spacer(1, 0.1 * inch))

        for line in task_summary.split("\n"):
            line = line.strip()
            if not line:
                story.append(Spacer(1, 0.1 * inch))
            elif line.startswith("- ") or line.startswith("* "):
                story.append(Paragraph(f"• {line[2:]}", body_style))
            else:
                story.append(Paragraph(line, body_style))

    doc.build(story)
    return output_path