%define	module	File-Remove
%define	name	perl-%{module}
%define	version	0.34
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Remove files and directories
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/R/RS/RSOD/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}/
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
A Perl module to remove files and directories.

%prep
%setup -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/*/*


