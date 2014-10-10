%define	modname	File-Remove
%define modver 1.52

Summary:	Remove files and directories
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/File/File-Remove-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
A Perl module to remove files and directories.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/man3/*


