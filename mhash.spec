Summary:	Hash library 
Summary(pl):	Biblioteka funkcji mieszaj±cych
Name:		mhash
Version:	0.8.13
Release:	1
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
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
Mhash to biblioteka dostarczaj±ca jednolity interfejs do duøej liczby
algorytmÛw mieszaj±cych. Te algorytmy mog± byÊ uøywane do liczenia sum
kontrolnych, oznaczeÒ komunikatÛw oraz innych sygnatur. Wsparcie dla
HMAC daje podstawy autentykacji komunikatÛw, zgodnie z RFC 2104.

%package devel
Summary:	Header files and development documentation for libmhash
Summary(pl):	Pliki nag≥Ûwkowe i dokumentacja do libmhash
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libmhash.

%description devel -l pl
Pliki nag≥Ûwkowe i dokumentacja programisty do libmhash.

%package static
Summary:	Static version of libmhash 
Summary(pl):	Statyczna wersja biblioteki libmhash
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):	Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:	%{name}-devel = %{version}

%description static
Static version of libmhash.

%description static -l pl
Statyczna wersja libmhash.

%prep
%setup -q

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
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
