#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Mail
%define		pnam	Alias
Summary:	Mail::Alias - manipulates mail alias files of various formats
Summary(pl):	Mail::Alias - manipulacja plikami z aliasami pocztowymi w ró¿nych formatach
Name:		perl-Mail-Alias
Version:	1.12
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	01d42c11f3c4372088597f9c5c3d6af7
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows direct manipulation of various types of E-Mail Alias
files.  The primary use of Mail::Alias is for manipulating alias files
in the SENDMAIL alias file format.  Additionally, it's possible to read
some other formats and to convert between various alias file formats.

%description -l pl
Ten modu³ pozwala na bezpo¶redni± manipulacjê danymi o aliasach e-mail,
zawartymi plikach o ró¿nych formatach.  Podstawowym zastosowaniem modu³u
jest manipulacja plikami w formacie Sendmaila.  Dodatkowo, mo¿liwe jest
tak¿e korzystanie z kilku innych formatów oraz konwertowanie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp testscripts/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_vendorlib}/Mail/Alias.pm
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
