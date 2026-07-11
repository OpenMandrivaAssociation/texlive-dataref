%global tl_name dataref
%global tl_revision 62942

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.7
Release:	%{tl_revision}.1
Summary:	Manage references to experimental data
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dataref
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dataref.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dataref.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides a mechanism that maintains a fixed symbolic
reference to numerical results; such results may vary as the project
proceeds (and hence the project report develops).

