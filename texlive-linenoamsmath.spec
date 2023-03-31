Name:		texlive-linenoamsmath
Version:	60655
Release:	2
Summary:	Use the lineno package together with amsmath
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/linenoamsmath
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linenoamsmath.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linenoamsmath.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/linenoamsmath.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package patches the amsmath package to work with the
lineno package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/linenoamsmath
%{_texmfdistdir}/tex/latex/linenoamsmath
%doc %{_texmfdistdir}/doc/latex/linenoamsmath

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
