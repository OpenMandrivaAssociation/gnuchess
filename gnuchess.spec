%define	name	gnuchess
%define version 5.07

%define book_version 1.01

Summary:	The GNU chess program
Name:		%{name}
Version:	%{version}
Release:	%mkrel 14
Source0:	ftp://ftp.gnu.org/pub/gnu/chess/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.gnu.org/pub/gnu/chess/%{name}-%{version}.tar.gz.sig
Source2:	ftp://ftp.gnu.org/pub/gnu/chess/book_%{book_version}.pgn.gz
Source3:	ftp://ftp.gnu.org/pub/gnu/chess/book_%{book_version}.pgn.gz.sig
Patch0:         gnuchess-5.07-gcc4.patch
Patch1:		gnuchess-5.07-getline.patch
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
%patch0 -p1
%patch1 -p1
gzip -dc %{SOURCE2} > book.pgn

%build
%configure2_5x	--bindir=%{_gamesbindir}
%make

# create book
echo -e 'book add book.pgn\nquit' | ./src/gnuchess -

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

install -m0644 book.dat -D %{buildroot}%{_gamesdatadir}/gnuchess/book.dat

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS doc/README
%{_gamesbindir}/*
%{_gamesdatadir}/gnuchess
