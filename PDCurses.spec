Summary:	Public Domain Curses
Summary(pl):	Ogólnie dostêpna biblioteka Curses
Name:		PDCurses
Version:	2.6
Release:	1
Vendor:		Mark Hessling
Group:		Development/Languages
License:	Public Domain and LGPL
Source0:	http://dl.sourceforge.net/sourceforge/pdcurses/%{name}-%{version}.tar.gz
# Source0-md5:	a376c91c7fdfa0215f4c22024ca325f1
Patch0:		%{name}-DESTDIR.patch
URL:		http://pdcurses.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PDCurses is an implementation of the curses library for X11. It
provides the ability for existing text-mode curses programs to be
re-built as native X11 applications with very little modification.
PDCurses for X11 is also known as XCurses. For more information on
PDCurses, visit http://pdcurses.sourceforge.net/ .

%description -l pl
PDCurses jest implementacj± biblioteki curses dla X11. Umo¿liwia ona
przebudowanie istniej±cych programów tekstowych korzystaj±cych z
curses jako natywne aplikacjie X11 po jedynie niewielkich
podywikacjach. PDCurses dla X11 jest znana tak¿e jako XCurses. Wiêcej
informacji na temat PDCurses mo¿na znale¼æ na stronie
http://pdcurses.sourceforge.net/ .

%prep
%setup -q
%patch0

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.a
%{_includedir}/%{name}/*.h
%doc README TODO doc/
