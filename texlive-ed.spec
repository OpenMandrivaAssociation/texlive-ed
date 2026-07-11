%global tl_name ed
%global tl_revision 25231

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.8
Release:	%{tl_revision}.1
Summary:	Editorial Notes for LaTeX documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ed
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ed.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ed.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ed.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package defines a couple of editorial notes that simplify
collaboration on a LaTeX text. These allow authors to annotate status
information in the source. In draft mode, the annotations are shown for
communication, and in publication mode these are suppressed.

