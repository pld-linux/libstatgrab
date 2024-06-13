#
# Conditional build:
%bcond_without	log4cplus	# log4cplus based logging

Summary:	Easy-to-use interface for accessing system statistics and information
Summary(pl.UTF-8):	Łatwy w użyciu interfejs dostępu do statystyk i informacji o systemie
Name:		libstatgrab
Version:	0.92.1
Release:	2
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/libstatgrab/libstatgrab/releases/
Source0:	https://github.com/libstatgrab/libstatgrab/releases/download/LIBSTATGRAB_0_92_1/%{name}-%{version}.tar.gz
# Source0-md5:	af685494e985229e0ac46365bc0cd50e
URL:		https://libstatgrab.org/
BuildRequires:	autoconf >= 2.69
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	linux-libc-headers >= 7:2.6.11.1-2
%{?with_log4cplus:BuildRequires:	log4cplus-devel >= 1.0.5}
%{?with_log4cplus:Requires:	log4cplus >= 1.0.5}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libstatgrab library provides an easy-to-use interface for
accessing system statistics and information. Available statistics
include CPU, Load, Memory, Swap, Disk I/O, and Network I/O. It was
developed to work on Linux, FreeBSD, and Solaris. The package also
includes two tools: saidar provides a curses-based interface for
viewing live system statistics, and statgrab is a sysctl-like
interface to the statistics.

%description -l pl.UTF-8
Biblioteka libstatgrab dostarcza łatwego w użyciu interfejsu dostępu
do informacji i statystyk systemowych. Dostępne statystyki obejmują
CPU, obciążenie, pamięć swap, dyskowe i sieciowe operacje we./wy. .
libstatgrab został stworzony by działać na linuksie, FreeBSD i
Solarisie. Pakiet zawiera także dwa narzędzia: saidar dostarcza
bazującego na curses interfejsu do przeglądania statystyk systemu i
statgrab, który jest interfejsem podobnym do sysctl dla statystyk.

%package devel
Summary:	Header files for libstatgrab library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libstatgrab
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_log4cplus:Requires:	log4cplus-devel >= 1.0.5}

%description devel
Header files for libstatgrab library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libstatgrab.

%package static
Summary:	Static libstatgrab library
Summary(pl.UTF-8):	Statyczna biblioteka libstatgrab
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libstatgrab library.

%description static -l pl.UTF-8
Statyczna biblioteka libstatgrab.

%package -n statgrab
Summary:	sysctl-style interface to system statistics
Summary(pl.UTF-8):	Podobny do sysctl interfejs do statystyk systemu
License:	GPL v2+
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description -n statgrab
statgrab provides a sysctl-style interface to all the system
statistics available through libstatgrab. This is useful for
applications that don't want to make library calls, but still want to
access the statistics.

An example of such an application is mrtg, for which scripts are
provided to generate configuration files.

%description -n statgrab -l pl.UTF-8
statgrab udostępnia podobny do sysctl interfejs do wszystkich
statystyk systemu dostępnych poprzez libstatgrab. Jest to przydatne
dla aplikacji nie chcących wykonywać wywołań bibliotecznych, ale
chcących mieć dostęp do statystyk.

Przykładem takiej aplikacji jest mrtg, dla którego dostępne są
skrypty do generowania plików konfiguracyjnych.

%package -n saidar
Summary:	A curses-based tool for viewing system statistics
Summary(pl.UTF-8):	Oparte na curses narzędzie do oglądania statystyk systemu
License:	GPL v2+
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description -n saidar
saidar is a curses-based tool for viewing the system statistics
available through libstatgrab. Statistics include CPU, processes,
load, memory, swap, network I/O, disk I/O, and file system
information.

%description -n saidar -l pl.UTF-8
saidar to oparte na curses narzędzie do oglądania statystyk systemu
dostępnych poprzez libstatgrab. Statystyki obejmują informacje o
procesorach, procesach, obciążeniu, pamięci, swapie, operacjach we/wy
sieciowych i dyskowych oraz systemach plików.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-curses-prefix=/usr \
	--with-ncurses \
	--disable-setgid-binaries \
	--disable-setuid-binaries \
	%{?with_log4cplus:--enable-logging}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libstatgrab.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README PLATFORMS
%attr(755,root,root) %{_libdir}/libstatgrab.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libstatgrab.so.10

%files devel
%defattr(644,root,root,755)
%doc examples/*.c
%attr(755,root,root) %{_libdir}/libstatgrab.so
%{_includedir}/statgrab*.h
%{_pkgconfigdir}/libstatgrab.pc
%{_mandir}/man3/libstatgrab.3*
%{_mandir}/man3/sg_*.3*
%{_mandir}/man3/statgrab.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libstatgrab.a

%files -n statgrab
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/statgrab*
%if %{with log4cplus}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/statgrab.properties
%endif
%{_mandir}/man1/statgrab*.1*

%files -n saidar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/saidar
%if %{with log4cplus}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/saidar.properties
%endif
%{_mandir}/man1/saidar.1*
