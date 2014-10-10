%define upstream_name	 Gtk2-Phat
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl interface to the Phat widget collection
License:	GPL+ or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-Gtk2
BuildRequires:	perl-Glib > 1.00
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	phat-devel
BuildRequires:	glitz-devel
BuildRequires:	gtkspell-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module allows a perl developer to access the widgets of the Phat widget 
collection which is geared toward pro-audio apps. The goal is to eliminate 
duplication of effort and provide some standardization.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find -type d -name CVS | rm -rf 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%{perl_vendorarch}/Gtk2
%{perl_vendorarch}/auto/Gtk2
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.80.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 403231
- rebuild using %%perl_convert_version

* Fri Oct 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2009.1
+ Revision: 294654
- update to new version 0.08

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.04-2mdv2009.0
+ Revision: 268520
- rebuild early 2009.0 package (before pixel changes)

* Mon Jun 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.0
+ Revision: 217095
- update to new version 0.04

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.03-2mdv2008.1
+ Revision: 152110
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Sat Oct 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2008.1
+ Revision: 98031
- update to new version 0.03
- update to new version 0.03


* Thu Mar 09 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdk
- new version
- spec cleanup

* Fri Sep 30 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.01-3mdk
- fix buildrequires

* Thu May 19 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.01-2mdk
- fix description & summary

* Thu May 19 2005 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.01-1mdk
- initial release

