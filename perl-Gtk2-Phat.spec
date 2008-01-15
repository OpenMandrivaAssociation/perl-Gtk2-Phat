%define module	Gtk2-Phat
%define name	perl-%{module}
%define version 0.03
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Perl interface to the Phat widget collection
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://search.cpan.org/CPAN/authors/id/F/FL/FLORA/%{module}-%{version}.tar.bz2
Url:            http://search.cpan.org/dist/%{module}/
BuildRequires:	perl-devel
BuildRequires:	perl-Gtk2
BuildRequires:	perl-Glib > 1.00
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-ExtUtils-PkgConfig
BuildRequires:	phat-devel
BuildRequires:	glitz-devel
BuildRequires:	gtkspell-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module allows a perl developer to access the widgets of the Phat widget 
collection which is geared toward pro-audio apps. The goal is to eliminate 
duplication of effort and provide some standardization.

%prep
%setup -q -n %{module}-%{version}
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
