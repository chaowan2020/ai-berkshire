from pypdf import PdfReader
import sys

src, dst = sys.argv[1], sys.argv[2]
r = PdfReader(src)
text = "\n".join((p.extract_text() or "") for p in r.pages)
open(dst, "w").write(text)
print(src, "pages:", len(r.pages), "chars:", len(text))
