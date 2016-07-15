MAINFILE := report
TEXSOURCES := $(wildcard *.tex) $(wildcard */*.tex)
BIBSOURCES := $(wildcard *.bib) $(wildcard */*.bib)
BBLFILES := $(subst bib,bbl,$(BIBSOURCES))

all: $(MAINFILE).pdf

clean:
	rm build/*

$(MAINFILE).pdf: $(MAINFILE).tex $(TEXSOURCES) $(BBLFILES)
	pdflatex -output-directory=build $(MAINFILE) build/$(MAINFILE).pdf
