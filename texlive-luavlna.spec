%global tl_name luavlna
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1n
Release:	%{tl_revision}.1
Summary:	Prevent line breaks after single letter words, units, or academic titles
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/generic/luavlna
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luavlna.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luavlna.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
In some languages, like Czech or Polish, there should be no single
letter words at the end of a line, according to typographical norms.
This package handles such situations using LuaTeX's callback mechanism.
In doing this, the package can detect languages used in the text and
insert spaces only in parts of the document where languages requiring
this feature are used. Another feature of this package is the inclusion
of non-breakable space after initials (like in personal names), after or
before academic degrees, and between numbers and units. The package
supports both plain LuaTeX and LuaLaTeX. BTW: "vlna" is the Czech word
for "wave" or "curl" and also denotes the tilde which, in TeX, is used
for "unbreakable spaces".

