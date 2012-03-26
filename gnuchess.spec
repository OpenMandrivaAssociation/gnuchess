%define book_version 1.02

Summary:	The GNU chess program
Name:		gnuchess
Version:	6.0.2
Release:	%mkrel 1
Source0:	ftp://ftp.gnu.org/pub/gnu/chess/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/pub/gnu/chess/%{name}-%{version}.tar.gz.sig
Source2:	ftp://ftp.gnu.org/pub/gnu/chess/book_%{book_version}.pgn.gz
Source3:	ftp://ftp.gnu.org/pub/gnu/chess/book_%{book_version}.pgn.gz.sig
Group:		Games/Boards
URL:		http://www.gnu.org/software/chess/
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL and Public Domain
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRequires:	flex
Provides:	chessengine
Obsoletes:	gnuchess-book
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
%configure2_5x	--bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

# create book
./src/%{name} --addbook book.pgn

%install
rm -rf %{buildroot}
%makeinstall_std

%__install -m0644 book.pgn -D %{buildroot}%{_gamesdatadir}/gnuchess/book.pgn

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS ChangeLog NEWS README COPYING
%{_gamesbindir}/*
%{_gamesdatadir}/gnuchess
%{_infodir}/*
