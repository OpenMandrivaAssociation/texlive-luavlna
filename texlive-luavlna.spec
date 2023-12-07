Name:		texlive-luavlna
Version:	67442
Release:	1
Summary:	Prevent line breaks after single letter words, units, or academic titles
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/luavlna
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luavlna.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luavlna.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
In some languages, like Czech or Polish, there should be no
single letter words at the end of a line, according to
typographical norms. This package handles such situations using
LuaTeX's callback mechanism. In doing this, the package can
detect languages used in the text and insert spaces only in
parts of the document where languages requiring this feature
are used. Another feature of this package is the inclusion of
non-breakable space after initials (like in personal names),
after or before academic degrees, and between numbers and
units. The package supports both plain LuaTeX and LuaLaTeX.
BTW: "vlna" is the Czech word for "wave" or "curl" and also
denotes the tilde which, in TeX, is used for "unbreakable
spaces".

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/luatex/luavlna
%doc %{_texmfdistdir}/doc/luatex/luavlna

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
