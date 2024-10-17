%define upstream_name    Image-Imlib2
%define upstream_version 2.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	4

Summary:    Interface to the Imlib2 image library
License:    GPL+ or Artistic
Group:      Development/Perl
URL:        https://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Image/%{upstream_name}-%{upstream_version}.tar.gz

Buildrequires:  imlib2-devel
Buildrequires:  perl(Module::Build)
Buildrequires:  perl(ExtUtils::CBuilder)
Buildrequires:  perl(ExtUtils::XSBuilder)
Buildrequires:  perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
Image::Imlib2 is a Perl port of Imlib2, a graphics library that does image file
loading and saving as well as manipulation, arbitrary polygon support, etc. It
does ALL of these operations FAST. It allows you to create colour images using
a large number of graphics primitives, and output the images in a range of
formats.

Image::Imlib2::Polygon and Image::Imlib2::ColorRange are described following
Image::Imlib2 but may be referenced before their description.

Note that this is an early version of my attempt at a Perl interface to Imlib2.
Currently, the API is just to test things out. Not everything is supported, but
a great deal of functionality already exists. If you think the API can be
tweaked to be a bit more intuitive, drop me a line!

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build CFLAGS="%{optflags}"
./Build test

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorarch}/auto/Image
%{perl_vendorarch}/Image
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.30.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Fri Nov 27 2009 Jérôme Quelin <jquelin@mandriva.org> 2.30.0-1mdv2010.1
+ Revision: 470464
- update to 2.03

* Sun Aug 30 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.20.0-1mdv2010.0
+ Revision: 422414
- new perl version macro

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 2.02-2mdv2010.0
+ Revision: 405859
- bump mkrel to force rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 2.02-1mdv2010.0
+ Revision: 402542
- update to 0.56

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.02-1mdv2009.1
+ Revision: 309309
- update to new version 2.02

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.01-2mdv2009.0
+ Revision: 268532
- rebuild early 2009.0 package (before pixel changes)

* Mon Jun 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.01-1mdv2009.0
+ Revision: 217096
- update to new version 2.01

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 2.00-2mdv2008.1
+ Revision: 151419
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Dec 08 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.00-1mdv2008.1
+ Revision: 116442
- update to new version 2.00


* Thu Nov 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.13-1mdv2007.0
+ Revision: 84623
- new version
- Import perl-Image-Imlib2

* Sat Aug 26 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdv2007.0
- New version 1.12

* Sat Aug 05 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdv2007.0
- New version 1.11

* Fri Jun 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2007.0
- New version 1.10

* Sat Jun 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-2mdv2007.0
- buildrequires ExtUtils-XSBuilder and ExtUtils-CBuilder

* Wed Jun 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-1mdv2007.0
- New version 1.09
- %%mkrel
- fix build flags

* Thu Mar 02 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdk
- New release 1.08

* Tue Apr 26 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdk
- New release 1.07

* Fri Feb 04 2005 Guillaume Rousse <guillomovitch@mandrake.org> 1.04-1mdk 
- new version
- re-enable test

* Wed Jan 26 2005 Guillaume Rousse <guillomovitch@mandrake.org> 1.03-3mdk 
- rebuild for new imlib2
- fix url
- rpmbuildupdate aware
- disable test, seems broken

* Mon Nov 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.03-2mdk 
- rebuild for new perl

* Sun Jul 18 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.03-1mdk
- 1.03

* Sat Jun 05 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.02-1mdk
- 1.02

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.01-2mdk
- fixed dir ownership (distlint)

* Sun Dec 07 2003 Guillaume Rousse <guillomovitch@mandrake.org> 1.01-1mdk
- first mdk release

