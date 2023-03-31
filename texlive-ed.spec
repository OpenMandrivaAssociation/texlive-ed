Name:		texlive-ed
Version:	25231
Release:	2
Summary:	Editorial Notes for LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ed
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ed.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ed.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ed.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines a couple of editorial notes that simplify
collaboration on a LaTeX text. These allow authors to annotate
status information in the source. In draft mode, the
annotations are shown for communication, and in publication
mode these are suppressed.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ed/ed.sty
%doc %{_texmfdistdir}/doc/latex/ed/Makefile
%doc %{_texmfdistdir}/doc/latex/ed/README
%doc %{_texmfdistdir}/doc/latex/ed/ed.pdf
%doc %{_texmfdistdir}/doc/latex/ed/ed.sty.ltxml
#- source
%doc %{_texmfdistdir}/source/latex/ed/ed.dtx
%doc %{_texmfdistdir}/source/latex/ed/ed.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
