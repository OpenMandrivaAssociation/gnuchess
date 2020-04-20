%define book_version 1.02
%define _disable_rebuild_configure 1

Summary:	The GNU chess program
Name:		gnuchess
Version:	6.2.6
Release:	1
Group:		Games/Boards
License:	GPLv2 and Public Domain
Url:		http://www.gnu.org/software/chess/
Source0:	http://ftp.gnu.org/pub/gnu/chess/%{name}-%{version}.tar.gz
Source1:	http://ftp.gnu.org/pub/gnu/chess/%{name}-%{version}.tar.gz.sig
Source2:	http://ftp.gnu.org/pub/gnu/chess/book_%{book_version}.pgn.gz
Source3:	http://ftp.gnu.org/pub/gnu/chess/book_%{book_version}.pgn.gz.sig

BuildRequires:	flex
BuildRequires:	pkgconfig(readline)
BuildRequires:	pkgconfig(ncurses)
Provides:	chessengine
Provides:	gnuchess-book

%description
The gnuchess package contains the GNU chess program.  By default,
GNUchess uses a text-based interface.  Alternatively, GNUchess can
be used in conjunction with other GUI interface, thus serving as a
chess engine.

You should install the gnuchess package if you would like to play
chess on your computer. If you'd like to use a graphical interface
with GNUchess, you'll also need to install other GUI interface,
such as xboard or eboard.

This package also includes opening book for gnuchess, containing many
historic games played between masters and grandmasters.

%prep
%setup -q
gzip -dc %{SOURCE2} > book.pgn

%build
%configure \
	--bindir=%{_gamesbindir} \
	--datadir=%{_gamesdatadir}
%make_build

# create book
./src/gnuchess --addbook book.pgn


%install
%make_install

%find_lang %{name}

install -m0644 book.pgn -D %{buildroot}%{_gamesdatadir}/gnuchess/book.pgn

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_gamesbindir}/*
%{_gamesdatadir}/gnuchess
%{_gamesdatadir}/games/plugins/*/gnuchess.png
%{_gamesdatadir}/games/plugins/xboard/gnuchess.eng
%{_infodir}/*
%{_mandir}/man1/*
