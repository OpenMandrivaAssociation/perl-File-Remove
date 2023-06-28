%define	modname	File-Remove
%define modver 1.61

Summary:	Remove files and directories
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	3
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://metacpan.org/pod/File::Remove
Source0:	http://www.cpan.org/modules/by-module/File/File-Remove-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)

%description
A Perl module to remove files and directories.

%prep
%autosetup -n %{modname}-%{modver} -p1

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


