#
# Conditional build:
%bcond_without	tests	# don't perform "make check"
#
Summary:	Hash library
Summary(pl.UTF-8):	Biblioteka funkcji mieszających (skrótu)
Summary(pt_BR.UTF-8):	Interface uniforme para vários algoritmos hash
Name:		mhash
Version:	0.9.7.1
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/mhash/%{name}-%{version}.tar.bz2
# Source0-md5:	e2a7f6594d468c5d0edbfa788dbdca0f
URL:		http://mhash.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mhash is a library which provides a uniform interface to a large
number of hash algorithms. These algorithms can be used to compute
checksums, message digests, and other signatures. The HMAC support
implements the basics for message authentication, following RFC 2104.

%description -l pl.UTF-8
Mhash to biblioteka dostarczająca jednolity interfejs do dużej liczby
algorytmów mieszających (skrótu). Te algorytmy mogą być używane do
liczenia sum kontrolnych, oznaczeń komunikatów oraz innych sygnatur.
Obsługa HMAC daje podstawy dla uwierzytelniania wiadomości, zgodnie z
RFC 2104.

%description -l pt_BR.UTF-8
A biblioteca mhash provê uma interface uniforme para um grande número
de algoritmos hash. Estes algoritmos podem ser utilizados para
computar checksums, digests de mensagens, e outras assinaturas. O
suporte a HMAC implementa o básico para autenticação de mensagens,
seguindo o RFC 2104. Nas versões mais recentes foram adicionados
alguns algoritmos de geração de chaves, que utilizam algoritmos hash.
A biblioteca suporta os algoritmos CRC32, MD5, SHA1, HAVAL256, TIGER,
RIPEMD260, GOST, CRC32B, HAVAL224, HAVAL192, HAVAL160, HAVAL128,
TIGER128, TIGER160, MD4, SHA256, and ADLER32.

%package devel
Summary:	Header files and development documentation for libmhash
Summary(es.UTF-8):	Archivos de inclusión y bibliotecas de desarrollo
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do libmhash
Summary(pt_BR.UTF-8):	Arquivos de desenvolvimento para a biblioteca mhash
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and development documentation for libmhash.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja programisty do libmhash.

%description devel -l pt_BR.UTF-8
Esse pacote contém arquivos de desenvolvimento para a biblioteca
mhash.

%package static
Summary:	Static version of libmhash
Summary(es.UTF-8):	bibliotecas estaticas mhash
Summary(pl.UTF-8):	Statyczna wersja biblioteki libmhash
Summary(pt_BR.UTF-8):	Bibliotecas estáticas do mhash para desenvolvimento
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libmhash.

%description static -l pl.UTF-8
Statyczna wersja libmhash.

%description static -l pt_BR.UTF-8
Esse pacote contém arquivos de desenvolvimento estáticos para a
biblioteca mhash.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-static
%{__make}

%if %{with tests}
LD_LIBRARY_PATH=$(pwd)/lib/.libs; export LD_LIBRARY_PATH
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO doc/skid2-authentication
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_mandir}/man3/*
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
