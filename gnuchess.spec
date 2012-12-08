%define	name	gnuchess
%define version 6.0.0

%define book_version 1.02

Summary:	The GNU chess program
Name:		%{name}
Version:	%{version}
Release:	%mkrel 3
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
echo -e 'book add book.pgn\nquit' | ./src/gnuchess -

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

install -m0644 book.pgn -D %{buildroot}%{_gamesdatadir}/gnuchess/book.pgn

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README
%{_gamesbindir}/*
%{_gamesdatadir}/gnuchess
%{_infodir}/*


%changelog
* Tue May 03 2011 Funda Wang <fwang@mandriva.org> 6.0.0-1mdv2011.0
+ Revision: 663902
- no more patches needed
- new version 6.0.0

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 5.07-16mdv2011.0
+ Revision: 605487
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 5.07-15mdv2010.1
+ Revision: 522740
- rebuilt for 2010.1

* Mon Oct 05 2009 Funda Wang <fwang@mandriva.org> 5.07-14mdv2010.0
+ Revision: 453794
- fix getline build

* Thu Feb 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.07-14mdv2009.1
+ Revision: 345174
- rebuild against new readline

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 5.07-13mdv2009.0
+ Revision: 221093
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 5.07-12mdv2008.1
+ Revision: 178954
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 05 2007 Adam Williamson <awilliamson@mandriva.org> 5.07-10mdv2008.0
+ Revision: 48447
- rebuild for 2008
- Import gnuchess



* Mon Sep 18 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 5.07-9mdv2007.0
- Rebuild

* Sat Dec 31 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 5.07-8mdk
- Rebuild

* Sat Jul 30 2005 Nicolas L�cureuil <neoclust@mandriva.org> 5.07-7mdk
- Patch 0 :Fix Build with Gcc4
- mkrel

* Thu Jan 20 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 5.07-6mdk
- rebuild for new readline

* Sun Nov 21 2004 Abel Cheung <deaddog@mandrake.org> 5.07-5mdk
- Use gzip tarball instead, for signature verification
- Include opening book, so prepare for a tougher engine ;-)

* Thu Jul 15 2004 Abel Cheung <deaddog@deaddog.org> 5.07-4mdk
- Add back Provides, quite a few frontends can use alternative
  chess engine (crafty and sjeng being a notable example),
  though other packages need fixed requirement

* Tue Jul 13 2004 Michael Scherer <misc@mandrake.org> 5.07-3mdk 
- remove useless Provides

* Thu Dec 11 2003 Abel Cheung <deaddog@deaddog.org> 5.07-2mdk
- add missing buildrequires (thx Stefan's bot)

* Thu Nov 06 2003 Abel Cheung <deaddog@deaddog.org> 5.07-1mdk
- 5.07

* Wed Oct 15 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 5.06-3mdk
- remove menu item, stupid me..

* Mon Jul 07 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 5.06-2mdk
- move binary to %%{_Gamesbindir} (closes #4149)
- use %%make macro
- added menu item (used the strategy section icon since it's a chess board:)

* Thu Jun  5 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 5.06-1mdk
- new version

* Fri Mar  7 2003 Guillaume Cottenceau <gc@mandrakesoft.com> 5.05-1mdk
- new version (fixes #2871)

* Wed Jul 24 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 5.04-2mdk
- rebuild for new readline

* Mon Apr  8 2002 Guillaume Cottenceau <gc@mandrakesoft.com> 5.04-1mdk
- new version
- spec cleanup, use our macros
- fix no-url-tag
- fix obsolete-tag Copyright
- fix use-of-RPM_SOURCE_DIR
- fix update-menus-*

* Sat Aug 11 2001 Jesse Kuang <kjx@mandrakesoft.com> 4.0.pl80-6mdk
- rebuild for cooker

* Sat Sep 23 2000 Stefan van der Eijk <s.vandereijk@chello.nl> 4.0.p180-5mdk
- BM
- macro's
- compress & strip files with spec helper
- use update_menus and clean_menus

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.0.pl80-4mdk
- automatically added BuildRequires

* Mon Apr 10 2000 Christopher Molnar <molnarc@mandrakesoft.com> 4.0.pl80-3mdk
- added menu files

* Thu Apr 06 2000 Christopher Molnar <molnarc@mandrakesoft.com> 4.0.pl80-2mdk
- changes in spec file for groups
- considered upgrading to version 5.00 (now renamed to chess-5.00)
- but this would have taken away some features (x, curses, etc).
  
* Wed Nov 10 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- update to 4.0pl80.
- provide chessprogram, don't require xboard.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 3)

* Mon Jan 23 1999 Michael Maher <mike@redhat.com>
- changed group name

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- rebuilt for 6.0, cleaned up spec file.

* Fri May 01 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Apr 15 1998 Erik Troan <ewt@redhat.com>
- built against new ncurses

* Fri Oct 17 1997 Donnie Barnes <djb@redhat.com>
- BuildRoot'ed

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
