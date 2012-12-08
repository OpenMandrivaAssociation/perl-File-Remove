%define	upstream_name	 File-Remove
%define	upstream_version 1.50

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:	Remove files and directories
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
A Perl module to remove files and directories.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
%makeinstall_std

%files 
%doc README Changes
%{perl_vendorlib}/File
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.500.0-3mdv2012.0
+ Revision: 765248
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.500.0-2
+ Revision: 763762
- rebuilt for perl-5.14.x

* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.500.0-1
+ Revision: 690261
- update to new version 1.50

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.490.0-2
+ Revision: 667144
- mass rebuild

* Mon Mar 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.490.0-1
+ Revision: 644749
- update to new version 1.49

* Sat Mar 12 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.480.0-1
+ Revision: 643997
- New version (Fixed a major bug in the 1.46 logic that works out what to change the cwd to when deleting while inside a directory.)

* Fri Feb 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.460.0-1
+ Revision: 638477
- update to new version 1.46

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.420.0-1mdv2010.1
+ Revision: 403177
- rebuild using %%perl_convert_version

* Fri Jul 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.42-1mdv2009.0
+ Revision: 233660
- update to new version 1.42

* Tue Jun 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.41-1mdv2009.0
+ Revision: 214511
- update to new version 1.41

* Mon Feb 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.40-1mdv2008.1
+ Revision: 174677
- update to new version 1.40

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Nov 17 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.39-1mdv2008.1
+ Revision: 109521
- update to new version 0.39

* Sun Oct 21 2007 Funda Wang <fwang@mandriva.org> 0.38-1mdv2008.1
+ Revision: 100833
- update to new version 0.38

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.37-1mdv2008.0
+ Revision: 52490
- update to new version 0.37

* Wed Jul 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2008.0
+ Revision: 48164
- new version


* Thu Dec 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2007.0
+ Revision: 96810
- new version
- Import perl-File-Remove

* Fri Jan 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.31-1mdk
- new version
- spec cleanup
- %%mkrel
- rpmbuildupdate aware

* Tue Aug 23 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.30-1mdk
- 0.30

* Wed Dec 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.29-1mdk
- 0.29

* Wed Nov 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.28-1mdk
- 0.28

* Thu Aug 05 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.21-1mdk
- 0.21.

* Thu Jan 29 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.20-2mdk
- bzip2

* Wed Jan 28 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.20-1mdk
- from Robin Rosenberg <robin.rosenberg@dewire.com> : 
	- initial contrib import. Needed for building Captive-NTFS

