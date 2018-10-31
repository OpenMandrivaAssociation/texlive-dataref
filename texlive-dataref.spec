Name:		texlive-dataref
Version:	0.6
Release:	2
Summary:	Manage references to experimental data
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dataref
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dataref.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dataref.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/dataref
%doc %{_texmfdistdir}/doc/latex/dataref

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
