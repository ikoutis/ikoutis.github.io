# Set this to "off" to use normal LaTeX:
USE_PDFLATEX = true

MAINFILE = main.tex

SUBFILES = $(wildcard tex/*.tex) 

# xfig drawings to be included in the document
FIGFILES = $(wildcard fig/*.fig) $(wildcard tex/graphs/*.fig)

# other postscript files to be included in the document
EPSFILES = $(wildcard eps/*.eps) $(wildcard tex/graphs/*.eps)

BIBFILES = $(wildcard *.bib)

# constants

MAKE = gmake --no-print-directory 

MAIN = $(subst .tex,,$(MAINFILE))
MAINBBL = $(MAIN).bbl
MAINPS = $(MAIN).ps
MAINPDF = $(MAIN).pdf
ifeq ($(USE_PDFLATEX),true)
MAINDVI = $(MAIN).pdf
OUTPUT = $(MAINPDF)
else
MAINDVI = $(MAIN).dvi
OUTPUT = $(MAINPS)
endif
MAINAUX = $(MAIN).aux
MAINTOC = $(MAIN).toc
MAINLOG = $(MAIN).log

ifeq ($(USE_PDFLATEX),true)
latex = pdflatex
else
latex = latex
endif

bibtex = bibtex
fig2dev = fig2dev
printer = stone
gv = kghostview

# file where we measure our progress by bytes, words, lines and pages
WCLOGFILE = $(MAIN).wc
REBIBFLAG = $(MAIN).must_remake_bbl.flag


# COMMANDS

.PHONY: dvi ps print xdvi gv backup clean grep latex_doit bibtex_doit

all:	$(OUTPUT)

dvi:	$(WCLOGFILE)

ps:	dvi $(MAINPS)

pdf:	$(MAINPDF)

print:	ps
	lpr -P$(printer) $(MAINPS)
	lpq -P$(printer)

xdvi:	dvi
	xdvi -s 4 $(MAINDVI)

gv:	$(OUTPUT)
	$(gv) $<

acroread: pdf
	acroread $(MAINPDF)

backup:
	test -d backup || mkdir backup
	tar cvf backup/`date +%y-%m-%d`.tar Makefile NOTES $(MAINFILE) $(SUBFILES) $(FIGFILES) $(EPSFILES) $(BIBFILES) $(WCLOGFILE) ; gzip -f backup/*.tar

clean:	
	rm -f *.dvi
	rm -f *.aux
	rm -f *.log
	rm -f *.toc
	rm -f *.lof
	rm -f *.lot
	rm -f *.idx
	rm -f *.ind
	rm -f *.ilg
	rm -f *.bbl
	rm -f *.blg
	rm -f *.toc.copy
	rm -f $(FIGFILES:.fig=.eps)
	rm -f $(FIGFILES:.fig=.pdf)
	rm -f $(EPSFILES:.eps=.pdf)
	rm -f $(MAINPS)
	rm -f *~

# e.g. gmake grep string='traveling salesman'
grep:
	@echo '*****' Searching for '"'$(string)'"' in thesis files '*****'
	@fgrep -i -e '$(string)' $(MAINFILE) $(SUBFILES) $(BIBFILES)


# RULES

# kill some default rules
.SUFFIXES:

$(WCLOGFILE):	$(MAINDVI)
	./bin/wordcount $(MAIN) >> $(WCLOGFILE)
        # after every successful compile, log word count to WCLOGFILE.

$(MAINDVI):	$(MAINFILE) $(SUBFILES) $(EPSFILES:.eps=.pdf) $(FIGFILES:.fig=.eps) $(FIGFILES:.fig=.pdf) $(MAINBBL)
	@echo === Running LaTeX for the first time ===
	$(MAKE) latex_doit
	@echo === Checking if we need to rebuild bibliography ===
	@./bin/nowarning 'citation.*undefined' $(MAINLOG) || touch $(REBIBFLAG)
	@(test -f $(REBIBFLAG) && ( echo === Building bibliography === ; $(MAKE) -k bibtex_doit latex_doit)) || true
#       Rerun if the post-latex ToC is not identical to the pre-latex one.
	@diff $(MAINTOC) $(MAINTOC).copy > /dev/null || (echo === Re-running LaTeX to update table of contents === ; $(MAKE) latex_doit)
	@./bin/nowarning 'rerun' $(MAINLOG) || (echo === Re-running LaTeX === ; $(MAKE) latex_doit)
	@./bin/nowarning 'rerun' $(MAINLOG) || (echo === Re-running LaTeX === ; $(MAKE) latex_doit)
	@./bin/nowarning 'warning' $(MAINLOG) || (echo === Re-running LaTeX due to warnings === ; $(MAKE) latex_doit)
	@echo  === Checking for errors ===
	./bin/tex_error $(MAINLOG)
#	@echo === Checking for warnings ===
#	./bin/nowarning 'warning' $(MAINLOG)

$(MAINBBL): $(BIBFILES)
	@echo === BibTeX files updated, must rebuild bibliography ===
	@touch $(MAINBBL)
	@touch $(REBIBFLAG)

latex_doit:
	@touch $(MAINTOC) ; cp -p $(MAINTOC) $(MAINTOC).copy
	-$(latex) '\nonstopmode\input{$(MAINFILE)}' >/dev/null
	./bin/tex_error -nw $(MAINLOG)

bibtex_doit:
	$(bibtex) $(MAIN)
	@rm -f $(REBIBFLAG)

%.eps : %.fig
	$(fig2dev) -L eps $< $@

%.pdf : %.eps
	epstopdf $< --outfile=$@

%.ps : %.dvi
	@echo === Converting DVI file to PostScript ===
	dvips -Ppdf -o $@ $< 2>/dev/null

%.pdf : %.ps
	@echo === Converting PostScript file to PDF ===
	ps2pdf -dAutoRotatePages=/None $<
