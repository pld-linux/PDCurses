Summary:	Public Domain Curses
Summary(pl):	Ogólnie dostêpna biblioteka Curses
Name:		PDCurses
Version:	2.6
Release:	3
Vendor:		Mark Hessling
Group:		Libraries
License:	Public Domain and LGPL
Source0:	http://dl.sourceforge.net/pdcurses/%{name}-%{version}.tar.gz
# Source0-md5:	a376c91c7fdfa0215f4c22024ca325f1
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-Makefile.patch
URL:		http://pdcurses.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PDCurses is an implementation of the curses library for X11. It
provides the ability for existing text-mode curses programs to be
re-built as native X11 applications with very little modification.
PDCurses for X11 is also known as XCurses. For more information on
PDCurses, visit http://pdcurses.sourceforge.net/ .

%description -l pl
PDCurses jest implementacj± biblioteki curses dla X11. Umo¿liwia ona
przebudowanie istniej±cych programów tekstowych korzystaj±cych z
curses jako natywne aplikacje X11 po jedynie niewielkich
modyfikacjach. PDCurses dla X11 jest znana tak¿e jako XCurses. Wiêcej
informacji na temat PDCurses mo¿na znale¼æ na stronie
http://pdcurses.sourceforge.net/ .

%package devel
Summary:	Header files for PDCurses library
Summary(pl):	Pliki nag³ówkowe biblioteki PDCurses
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files for PDCurses library.

%description devel -l pl
Pliki nag³ówkowe biblioteki PDCurses.

%package static
Summary:	Static version of PDCurses library
Summary(pl):	Statyczna wersja biblioteki PDCurses
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of PDCurses library.

%description static -l pl
Statyczna wersja biblioteki PDCurses.

%prep
%setup -q
%patch0
%patch1 -p1

%build
cp -f /usr/share/automake/config.sub .
%{__autoconf}
%configure
%{__make} \
	LD_RXLIB2="-Wl,-soname=libXCurses.so -L/usr/X11R6/%{_lib} -lXaw -lXmu -lXt -lX11"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_libdir}/libXCurses.so

%files devel
%defattr(644,root,root,755)
%doc doc/*
%attr(755,root,root) %{_bindir}/xcurses-config
# this one is static-only
%{_libdir}/libXpanel.a
%{_includedir}/%{name}

%files static
%defattr(644,root,root,755)
%{_libdir}/libXCurses.a
