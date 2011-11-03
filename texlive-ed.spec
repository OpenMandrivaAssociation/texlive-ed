# revision 21084
# category Package
# catalog-ctan /macros/latex/contrib/ed
# catalog-date 2011-01-15 13:01:09 +0100
# catalog-license lppl
# catalog-version v1.7
Name:		texlive-ed
Version:	v1.7
Release:	1
Summary:	Editorial Notes for LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ed
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ed.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ed.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ed.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package defines a couple of editorial notes that simplify
collaboration on a LaTeX text. These allow authors to annotate
status information in the source. In draft mode, the
annotations are shown for communication, and in publication
mode these are suppressed.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ed/ed.sty
%doc %{_texmfdistdir}/doc/latex/ed/README
%doc %{_texmfdistdir}/doc/latex/ed/ed.pdf
%doc %{_texmfdistdir}/doc/latex/ed/ed.sty.ltxml
#- source
%doc %{_texmfdistdir}/source/latex/ed/ed.dtx
%doc %{_texmfdistdir}/source/latex/ed/ed.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}