# Compile

To compile the main.tex and update the main.pdf a few commands are needed.

For everything to work as expected run the following commands before open the main.pdf file.

```
pdflatex main # Compile template

makeindex main.nlo -s nomencl.ist -o main.nls # Compile nomenclature

makeindex main # Compile index

biber main # Compile bibliography

pdflatex main # Compile template

makeglossaries main # Compile glossary

pdflatex main # Compile template
```

The following commands are simplified in only one in the Makefile. Instead of this list of command you can just use the following command to do all of them at the same time.

```
make compile
```
