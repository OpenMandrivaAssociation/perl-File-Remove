%define	modname	File-Remove

Summary:	Remove files and directories
Name:		perl-%{modname}
Version:	1.61
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/File::Remove
Source0:	http://www.cpan.org/modules/by-module/File/File-Remove-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

%description
A Perl module to remove files and directories.

%prep
%autosetup -n %{modname}-%{version} -p1

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files 
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/man3/*
