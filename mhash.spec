Summary:	Hash library
Summary(pl):	Biblioteka funkcji mieszaj±cych
Name:		mhash
Version:	0.8.13
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://mhash.sourceforge.net/dl/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mhash is a library which provides a uniform interface to a large
number of hash algorithms. These algorithms can be used to compute
checksums, message digests, and other signatures. The HMAC support
implements the basics for message authentication, following RFC 2104.

%description -l pl
Mhash to biblioteka dostarczaj±ca jednolity interfejs do du¿ej liczby
algorytmów mieszaj±cych. Te algorytmy mog± byæ u¿ywane do liczenia sum
kontrolnych, oznaczeñ komunikatów oraz innych sygnatur. Wsparcie dla
HMAC daje podstawy autentykacji komunikatów, zgodnie z RFC 2104.

%package devel
Summary:	Header files and development documentation for libmhash
Summary(pl):	Pliki nag³ówkowe i dokumentacja do libmhash
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libmhash.

%description devel -l pl
Pliki nag³ówkowe i dokumentacja programisty do libmhash.

%package static
Summary:	Static version of libmhash
Summary(pl):	Statyczna wersja biblioteki libmhash
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libmhash.

%description static -l pl
Statyczna wersja libmhash.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

gzip -9nf ChangeLog AUTHORS NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%{_mandir}/man3/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
