# revision 32438
# category Package
# catalog-ctan /macros/latex/contrib/dataref
# catalog-date 2013-12-17 23:27:23 +0100
# catalog-license other-free
# catalog-version 0.1
Name:		texlive-dataref
Version:	0.1
Release:	3
Summary:	Manage references to experimental data
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dataref
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dataref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dataref.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dataref.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a mechanism that maintains a fixed
symbolic reference to numerical results; such results may vary
as the project proceeds (and hence the project report
develops).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dataref/dataref.sty
%doc %{_texmfdistdir}/doc/latex/dataref/README
%doc %{_texmfdistdir}/doc/latex/dataref/dataref.pdf
#- source
%doc %{_texmfdistdir}/source/latex/dataref/dataref.dtx
%doc %{_texmfdistdir}/source/latex/dataref/dataref.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
