#import "template.typ": *

#set heading(numbering: "A.1.1")
#counter(heading).update(0)
#set math.equation(numbering: dependent-numbering("(A.1)"), supplement: [])

#include "appendix/section_1.typ"
