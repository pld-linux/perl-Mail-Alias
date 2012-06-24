%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	Alias
Summary:	%{pdir}::%{pnam} perl module
Summary(cs):	Modul %{pdir}::%{pnam} pro Perl
Summary(da):	Perlmodul %{pdir}::%{pnam}
Summary(de):	%{pdir}::%{pnam} Perl Modul
Summary(es):	M�dulo de Perl %{pdir}::%{pnam}
Summary(fr):	Module Perl %{pdir}::%{pnam}
Summary(it):	Modulo di Perl %{pdir}::%{pnam}
Summary(ja):	%{pdir}::%{pnam} Perl �⥸�塼��
Summary(ko):	%{pdir}::%{pnam} �� ����
Summary(no):	Perlmodul %{pdir}::%{pnam}
Summary(pl):	Modu� perla %{pdir}::%{pnam}
Summary(pt_BR):	M�dulo Perl %{pdir}::%{pnam}
Summary(pt):	M�dulo de Perl %{pdir}::%{pnam}
Summary(ru):	������ ��� Perl %{pdir}::%{pnam}
Summary(sv):	%{pdir}::%{pnam} Perlmodul
Summary(uk):	������ ��� Perl %{pdir}::%{pnam}
Summary(zh_CN):	%{pdir}::%{pnam} Perl ģ��
Name:		perl-%{pdir}-%{pnam}
Version:	1.12
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows direct manipulation of various types of E-Mail Alias
files.   The primary use of Mail::Alias is for manipulating alias files
in the SENDMAIL alias file format.  Additionally, it's possible to read
some other formats and to convert between various alias file formats.

%description -l pl
Ten modu� pozwala na bezpo�redni� manipulacj� danymi o aliasach e-mail,
zawartymi plikach o r�nych formatach.  Podstawowym zastosowaniem modu�u
jest manipulacja plikami w formacie Sendmaila.  Dodatkowo, mo�liwe jest
tak�e korzystanie z kilku innych format�w oraz konwertowanie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp testscripts/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%{perl_sitelib}/%{pdir}/%{pnam}.pm
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
%{_mandir}/man3/*
