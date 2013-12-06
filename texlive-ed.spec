# revision 25231
# category Package
# catalog-ctan /macros/latex/contrib/ed
# catalog-date 2012-01-29 16:01:54 +0100
# catalog-license lppl1
# catalog-version 1.8
Name:		texlive-ed
Version:	1.8
Release:	3
Summary:	Editorial Notes for LaTeX documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ed
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ed.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ed.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ed.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 31 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.8-1
+ Revision: 770140
- Update to latest upstream package

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v1.7-2
+ Revision: 751323
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v1.7-1
+ Revision: 718305
- texlive-ed
- texlive-ed
- texlive-ed
- texlive-ed

