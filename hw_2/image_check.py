from latex_generator_for_tables_and_images.generator import table_generator, image_generator

table = [
    ["Name", "Age", "City"],
    ["Ivan", "25", "Moscow"],
    ["Andrew", "33", "Saint-Petersburg"],
    ["Ilya", "38", "Orenburg"]
]

start = "\\documentclass[12pt]{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage[english,russian]{babel}\n\\usepackage{color}\n\\usepackage{tikz}\n\\usepackage{graphicx}\n\\usepackage{amsmath}\n\\usepackage{amsthm}\n\\usepackage{amssymb}\n\\usepackage{caption}\n\\usepackage{listings}\n\\usepackage{xcolor}\n%\\usepackage{url}\n\\usepackage{hyperref}\n\\usepackage{wasysym}\n\\usepackage{enumitem}\n\\usepackage{subcaption}\n\\usepackage{imakeidx}\n\\usepackage[russian]{cleveref}\n\\usepackage[a4paper,left=15mm,right=15mm,top=30mm,bottom=20mm]{geometry}\n\\parindent=0mm\n\\parskip=3mm\n\\definecolor{bostonuniversityred}{rgb}{0.8, 0.0, 0.0}\n\\makeindex\n\\pagestyle{empty}\n\\title{}\n\\author{}\n\\date{}\n\\begin{document}\n\\maketitle\n\\thispagestyle{empty}\n"

end = "\\end{document}\n"

with open("table_image.tex", "w") as file:
    file.write(start)
    file.write(table_generator(table))
    file.write("\n")
    file.write(image_generator("1.png", "Picture", width=0.8))
    file.write("\n")
    file.write(end)
