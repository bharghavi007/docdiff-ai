import gradio as gr
import difflib
from typing import List

def read_file(file_bytes):
    return file_bytes.decode("utf-8").splitlines()

def generate_summary(diff_text: str) -> str:
    """Generate a concise summary of the unified diff without using any external service."""
    if not diff_text.strip():
        return "No differences found between the files."

    additions = sum(
        1 for line in diff_text.splitlines() if line.startswith('+') and not line.startswith('+++')
    )
    deletions = sum(
        1 for line in diff_text.splitlines() if line.startswith('-') and not line.startswith('---')
    )

    parts: List[str] = []
    if additions:
        parts.append(f"{additions} addition{'s' if additions != 1 else ''}")
    if deletions:
        parts.append(f"{deletions} removal{'s' if deletions != 1 else ''}")

    return " and ".join(parts) + " detected between the two files." if parts else "Files are identical."

def compare_and_summarize(file1, file2):
    try:
        text1_lines = read_file(file1)
        text2_lines = read_file(file2)

        diff = list(difflib.unified_diff(
            text1_lines,
            text2_lines,
            fromfile="File 1",
            tofile="File 2",
            lineterm=""
        ))
        diff_text = "\n".join(diff)

        summary = generate_summary(diff_text)

        return diff_text, summary

    except Exception as e:
        return f"Error comparing files: {str(e)}", "Could not generate summary."

iface = gr.Interface(
    fn=compare_and_summarize,
    inputs=[
        gr.File(label="Upload File 1", type="binary"),
        gr.File(label="Upload File 2", type="binary")
    ],
    outputs=[
        gr.Textbox(label="Differences (Unified Diff)", lines=20),
        gr.Textbox(label="Local Summary", lines=8)
    ],
    title="📄 Document Comparator Tool",
    description="Upload two text files. See detailed differences and a locally-generated summary of changes."
)

if __name__ == "__main__":
    iface.launch()